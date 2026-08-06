def segitiga(tinggi):
    for i in range( 1, tinggi + 1):
        bintang = "*" * (2 * i - 1)
        print(bintang)
segitiga(5)

print("ikan goreng")

def terbaik (tinggi):
    for i in range(3, 0, -1):
        bintang = "*" * (2 * i + 1 )
        print(bintang)
terbaik(2)

print("ikan bakar")

def persegi(tinggi):
    for i in range(1, tinggi + 1):
        bintang = "*" * 10
        print(bintang)
persegi(4)

print("ikan bakar")

def segitiga_terbalik(tinggi):
    for i in range(5, 0, -1):
        spasi = " " * (5 - i)
        bintang = "*" * (2 * i - 1)
        print(spasi + bintang)
segitiga_terbalik(5)

print("ikan bakar")

def piramida_terbalik(tinggi):
    for i in range(tinggi): 
        spasi = " " * i
        bintang = "*" * ((2 * tinggi - 1) - 2 * i)
        print(spasi + bintang)

piramida_terbalik(5)

def piramida(tinggi):
    for i in range(tinggi):
        spasi = " " * (tinggi - i - 1)
        bintang = "*" * (2 * i + 1)
        print(spasi + bintang)
piramida(5)

def final_boss(tinggi): 

    for i in range(tinggi):
        spasi = " " * (tinggi - i - 1)
        bintang = "*" * (2 * i + 1)
        print(spasi + bintang)

    for i in range(tinggi):
        spasi = " " * i
        bintang = "*" * ((2 * tinggi - 1) - 2 * i)
        print(spasi + bintang)

final_boss(5)

def final_boss_2(tinggi):

    for i in range(1, tinggi + 1):


        spasi = " " * (tinggi - i)
        jumlah_bintang = 2 * i - 1
        baris = ""

        for j in range(jumlah_bintang):
            if j == 0 or j == jumlah_bintang - 1 or i == tinggi:
                baris += "*"
            else:
                baris += " "

        print(spasi + baris)

def final_boss_2(tinggi):

    for i in range(1, tinggi + 1):

        spasi = " " * (tinggi - i)
        jumlah_bintang = 2 * i - 1
        baris = ""

        for j in range(jumlah_bintang):
           if j == 0 or j == jumlah_bintang - 1 or j == tinggi:
               baris += "*"
            else:
                baris += " "

final_boss_2(5)


