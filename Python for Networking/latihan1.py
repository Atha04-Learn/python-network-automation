"""
Soal 1: Manajemen IP (List) Kamu punya daftar IP address awal: ip_list = ["10.1.1.1", "10.1.1.2", "10.1.1.3"]. Buatlah kode untuk:

    Menambahkan IP "10.1.1.4" ke dalam list tersebut.

    Menghapus IP pertama ("10.1.1.1") dari list.

    Mencetak (print) isi list terakhir.
"""
ip_list=["10.1.1.1","10.1.1.2","10.1.1.3"]
ip_list.append("10.1.1.4")
ip_list.remove("10.1.1.1")
print(ip_list)

"""
Soal 2: Inventaris Device (Dictionary) Buatlah sebuah dictionary bernama switch_core yang merepresentasikan sebuah switch dengan data berikut:

    Hostname: "SW-Core-BDG"

    Lokasi: "Gedung A"

    VLANs: [10, 20, 30] (Perhatikan: valuenya adalah sebuah List!)

Setelah dibuat, tulis kode untuk mengubah lokasinya menjadi "Gedung B" dan print dictionary tersebut.
"""
swwitch_core={"Hostname":"SW-Core-BDG",
              "Lokasi":"Gedung A",
              "VLANs":[10,20,30]}
swwitch_core["Lokasi"]="Gedung B"
print(swwitch_core)

print("Hello Push")
print("Hallo world")
