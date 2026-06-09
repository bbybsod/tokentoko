from flask import Flask, jsonify, render_template
import psutil, sqlite3, time

app = Flask(__name__)

# DB setup
conn = sqlite3.connect("stats.db", check_same_thread=False)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS stats (
    time TEXT,
    cpu REAL,
    ram REAL,
    disk REAL
)
""")
conn.commit()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stats")
def stats():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    now = time.strftime("%H:%M:%S")

    # simpan ke database
    c.execute("INSERT INTO stats VALUES (?, ?, ?, ?)", (now, cpu, ram, disk))
    conn.commit()

    return jsonify({"time": now, "cpu": cpu, "ram": ram, "disk": disk})

@app.route("/history")
def history():
    rows = c.execute("SELECT * FROM stats ORDER BY rowid DESC LIMIT 20").fetchall()
    return jsonify(rows[::-1])  # dibalik biar urut

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)