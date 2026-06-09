import time
import random
from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.CYAN + "=== CONNECTING TO tokentoko.indomaret.co.id" + Style.RESET_ALL)

# ====================== ISI DATA INI ======================
nomor_list = [
    "2013050765",   # Ganti dengan 10 nomor virtual kamu
   "2013050765",
   "2013050765",
   "2013050765",
]

# Kode toko / kode referral / kode promo yang mau dimasukkan (bisa sama untuk semua atau beda)
kode_toko = "tokentoko.indomaret.co.id"   

print(Fore.YELLOW + f"TARGET: {kode_toko}" + Style.RESET_ALL)

# Fungsi daftar akun (sudah ditambah input kode toko)
def daftar_akun(nomor, nomor_urut, kode):
    print(f"\n{Fore.BLUE}[{nomor_urut}/10] Menargetkan NIK: {nomor}{Style.RESET_ALL}")
    
    time.sleep(random.uniform(1.5, 3.5))
    
    print(Fore.MAGENTA + f"   → Menargetkan server: {kode}" + Style.RESET_ALL)
    time.sleep(random.uniform(0.8, 1.8))
    
    # Simulasi sukses/gagal (70% success)
    if random.random() > 0.3:
        print(Fore.GREEN + f"✓ Sukses! Akun ke-{nomor_urut} terdaftar" + Style.RESET_ALL)
        print(Fore.GREEN + f"   → Server '{kode}' sudah dimasukkan" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"✗ NIK AS {nomor}" + Style.RESET_ALL)
        return False

# ====================== LOOPING UTAMA ======================
sukses = 0

for i in range(10):
    if i >= len(nomor_list):
        print(Fore.YELLOW + "\nNomor sudah habis!" + Style.RESET_ALL)
        break
    
    nomor = nomor_list[i]
    
    if daftar_akun(nomor, i+1, kode_toko):
        sukses += 1
    
    # Delay antar akun (lebih natural)
    if i < 9:
        delay = random.randint(7, 14)
        print(Fore.CYAN + f"⏳ Tunggu {delay} detik sebelum akun berikutnya..." + Style.RESET_ALL)
        time.sleep(delay)

# ====================== HASIL ======================
print(Fore.MAGENTA + "\n" + "="*60 + Style.RESET_ALL)
print(Fore.CYAN + f"SELESAI! Total sukses: {sukses}/10" + Style.RESET_ALL)
print(Fore.MAGENTA + f"Kode Toko yang dipakai: {kode_toko}" + Style.RESET_ALL)
print(Fore.MAGENTA + "="*60 + Style.RESET_ALL)