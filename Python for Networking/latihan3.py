"""Soal 1: VLAN Creator (Function with Print) Buatlah fungsi bernama buat_vlan yang menerima dua parameter: vlan_id dan vlan_name. Fungsi ini tidak perlu return, cukup print perintah Cisco-nya. Contoh penggunaan nanti: buat_vlan(10, "Sales") Output yang diharapkan:
"""
def buat_vlan(vlan_id,vlan_name):
    print(f"vlan {vlan_id}")
    print(f"name {vlan_name}")
    print("exit")
buat_vlan(10,"sales")

"""
Soal 2: Bandwidth Calculator (Function with Return) Buat fungsi bernama cek_speed yang menerima parameter string interface_type (misal "FastEthernet", "GigabitEthernet", atau "TenGig").
Jika input "FastEthernet", return angka 100.

Jika input "GigabitEthernet", return angka 1000.

Jika input "TenGig", return angka 10000.

Jika lainnya, return 0.

"""
def cek_speed(interface_type):
    if interface_type=="FastEtherner":
        return 100
    elif interface_type=="GigabitEthernet":
        return 1000
    elif interface_type=="TenGig":
        return 10000
    else:
        return 0
    
panggil=cek_speed("GigabitEthernet")
print(panggil)

"""
Soal 3: Security Check (Logic dalam Function) Buat fungsi cek_password yang menerima parameter password.

    Jika panjang password kurang dari 8 karakter, print: "Weak: Terlalu pendek".

    Jika password mengandung kata "cisco" (huruf kecil semua), print: "Weak: Jangan pakai default!".

    Selain itu, print: "Password Strong".
"""

def cek_password(password):
    if len(password)<8:
        print("Weak: Terlalu Pendek")
    elif "cisco" in password:
        print("Weak! Jangan pakai default!")
    else:
        print("Password Strong")

sandi=input("Masukkan Password: ")
cek_password(sandi)

