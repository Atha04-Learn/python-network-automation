"""
Soal 1: The IP Loader

    Buat file teks bernama router_list.txt di folder yang sama dengan scriptmu. Isi dengan 3 baris IP sembarang.

    Buat script Python yang membaca file tersebut, lalu gunakan For Loop (Level 2) untuk mencetak kalimat: "Targeting IP: [IP dari file]..." untuk setiap baris.
"""
with open("router_list.txt","r") as list_ip:
    daftar_ip=list_ip.read().splitlines()

for ip in daftar_ip:
    print(f"Targeting: [{ip}]")


"""
Soal 2: The Logger Buat script yang meminta input user: pesan = input("Masukkan catatan log: "). Lalu simpan pesan tersebut ke dalam file bernama syslog.txt.

    Gunakan mode Append ('a') supaya kalau script dijalankan 2 kali, catatan lama tidak hilang.
"""
pesan=input("Masukkan catatan log: ")
with open("syslog.txt","a") as log:
    logs=log.write(pesan+"\n")

"""
Gabungan Level 3 (Function) dan Level 4 (File).

    Buat file vlan_db.txt (isi 3 ID VLAN).

    Buat fungsi def create_vlan(vlan_id): yang me-return string config.

    Baca file vlan_db.txt, loop, dan print hasil config dari fungsi tersebut.
"""

with open("vlan_db.txt","r") as vlan:
    vlan_id=vlan.read().splitlines()
def create_vlan(vlan_id):
    for i in vlan_id:
        print(i)
create_vlan(vlan_id)

