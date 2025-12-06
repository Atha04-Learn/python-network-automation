"""Soal 1: Configuration Generator (For Loop) Kamu diminta membuat script untuk mengamankan 3 interface sekaligus. Data: interfaces = ["Fa0/1", "Fa0/2", "Fa0/3"]

Buat loop yang menghasilkan output teks konfigurasi persis seperti ini untuk setiap interface:"""

Data=["Fa0/1","Fa0/2","Fa0/3"]
for secure in Data:
    print(f"interface {secure}")
    print("switchport mode access")
    print("switchport port-security")

"""Soal 2: Audit Status (Loop + If) Kamu melakukan scanning jaringan dan mendapatkan daftar status router dalam bentuk List: status_router = ["up", "up", "down", "up", "down"]

Tulis script yang melakukan loop pada list tersebut.

    Jika status "up", print: "Router aman".

    Jika status "down", print: "CRITICAL: Router Down!".

    (Bonus: Hitung berapa jumlah router yang "down" dan print angkanya di akhir)."""

status_router=["up","up","down","up","down"]
count=0
for status in status_router:
    if status=="up":
        print("Router aman")
    else:
        count+=1
        print("CRITICAL: Router Down!")
print(f"Terdapat {count} router yang down")

"""Soal 3: Filtering Data (Complex Logic) Kamu punya data mentah access list yang boleh lewat: allowed_ports = [80, 443, 22, 8080]

Tapi, kebijakan keamanan baru melarang port 22 (SSH) dan 80 (HTTP biasa). Buat loop untuk mengecek allowed_ports.

    Jika port adalah 22 atau 80, print: Block Port [nomor].

    Selain itu, print: Allow Port [nomor].

Kerjakan dengan teliti. Perhatikan indentasi (spasi di awal baris), karena di Python spasi itu nyawa
"""
allowed_port=[80,443,22,8080]
for allow in allowed_port:
    if allow==80 or allow ==22:
        print(f"Block Port [{allow}]")
    else:
        print(f"Allow Port [{allow}]")