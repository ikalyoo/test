def segitiga(tinggi):
    for i in range(1, tinggi + 1):
        spasi = " " * (tinggi - i)
        jumlah_bintang = 2 * i - 1
        baris = ""
        for j in range(jumlah_bintang):
            if j == 0 or j == jumlah_bintang - 1 or j == tinggi:
               baris += "*"
            else:
                baris += " "
        print(spasi + baris)

def persegi(sisi):
    for i in range(sisi):
        if i == 0 or i == sisi - 1:
            print("*" * sisi)
        else:
            print("*" + " " * (sisi - 2) + "*")

def piramida(tinggi):
    for i in range(tinggi):
        spasi = " " * (tinggi - i - 1)
        jumlah_bintang = "*" * (2 * i + 1)
        print(spasi + jumlah_bintang)

def piramida_terbalik(tinggi):
    for i in range(tinggi):
        spasi = " " * i
        jumlah_bintang = "*" * ((2 * tinggi - 1) - 2 * i)
        print(spasi + jumlah_bintang)

def pohon_natal(tinggi):
    for i in range(tinggi + 1):  
        if i == tinggi:
            jumlah_spasi = tinggi - 2
            jumlah_bintang = 3
        else:
            jumlah_spasi = tinggi - i - 1
            jumlah_bintang = 2 * i + 1
        for s in range(jumlah_spasi):
            print(" ", end="")
        for b in range(jumlah_bintang):
            print("*", end="")

        print()

def tengah(size):
    center = size // 2

    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print("N", end=" ")
            elif i == center and j == center:
                print("H", end=" ")
            else:
                print(" ", end=" ")
        print()
        

def percabangan():
    input_user = input("mau bidang apa? ")
    match input_user:
        case "segitiga":
            segitiga(10)
        case "persegi":
            persegi(4)
        case "piramida":
            piramida(10)
        case "piramida_terbalik":
            piramida_terbalik(10)
        case "pohon_natal":
            pohon_natal(10)
        case "ketupat":
            ketupat(10)
        case "segitiga_aneh":
            segitiga_aneh(10)
        case "tengah":
            tengah(10)
        case _:
            print("bidang tidak tersedia")
            
percabangan()