def biodata(tahun, nama, asal):
    tahun_sekarang = 2020
    print("Perkenalkan Nama Saya :", nama)
    print("Umur Saya :", tahun_sekarang - tahun)
    print("Saya Adalah Angkatan :", tahun_sekarang)
    print("Asal Saya Dari :", asal)

tahun_lahir = int(input())
nama = input()
asal = input()
biodata(tahun_lahir, nama, asal)