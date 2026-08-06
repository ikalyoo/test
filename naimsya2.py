# =====================================================================
#  TUGAS: PROGRAM KASIR MINI
# =====================================================================
#
#  Kamu bakal bikin program kasir dari nol. Ada 8 langkah.
#
#  ATURAN MAIN:
#    1. Kerjain URUT. Jangan loncat.
#    2. Tiap selesai satu langkah, JALANIN dulu programnya.
#       Cocokin sama "HASIL YANG DIHARAPKAN".
#    3. Kalau belum cocok, jangan lanjut. Benerin dulu.
#    4. Tulis kodenya di bawah tulisan "KODE KAMU DI SINI".
#    5. Petunjuknya sengaja nggak ngasih jawaban jadi. Mikir dulu.
#
#  Cara jalanin:  python naimsya2.py
#
#  Kalau error, BACA pesan errornya. Baris terakhir itu yang penting.
#  Contoh: "NameError: name 'total' is not defined"
#          artinya kamu pakai variabel yang belum pernah dibuat.
#
# =====================================================================


# =====================================================================
#  LANGKAH 1 - SIMPAN DAFTAR MENU
# =====================================================================
#
#  TUJUAN
#    Bikin daftar menu beserta harganya.
#
#  KENAPA DICT?
#    List cuma bisa nyimpen satu hal: ["pizza", "ikan"].
#    Tapi kita butuh DUA hal yang berpasangan: nama + harga.
#    Itu tugasnya dict. Bentuknya:
#
#        nama_dict = {"kunci1": nilai1, "kunci2": nilai2}
#
#    Kuncinya nama makanan (string, pakai kutip).
#    Nilainya harga (angka, tanpa kutip).
#
#  YANG HARUS DIBIKIN
#    Variabel `menu` isinya 6 pasang ini:
#        pizza  = 300      ayam  = 200
#        ikan   = 200      sttik = 599
#        laptop = 1000     gelas = 100
#
#  CARA NGETES
#    Tambahin sementara:  print(menu)
#    Terus jalanin. Harus keluar semua isinya.
#    Kalau udah bener, hapus lagi print-nya.
#
#  HASIL YANG DIHARAPKAN
#    {'pizza': 300, 'ikan': 200, 'laptop': 1000, ...dst}
#
# ---------------------------------------------------------------------
# KODE KAMU DI SINI (langkah 1)




# =====================================================================
#  LANGKAH 2 - TAMPILKAN MENU KE LAYAR
# =====================================================================
#
#  TUJUAN
#    Cetak semua isi menu, satu baris satu makanan.
#
#  MASALAHNYA
#    `print(menu)` tadi jelek, numpuk jadi satu baris.
#    Kita mau dicetak satu-satu.
#
#  PETUNJUK
#    Buat jalan-jalan ke seluruh isi dict, pakai:
#
#        for key, value in menu.items():
#            print(...)
#
#    `key`   = nama makanannya
#    `value` = harganya
#    Dua-duanya ganti otomatis tiap putaran. Kamu nggak usah ngapa-ngapain.
#
#    Buat gabung teks sama variabel, pakai f-string:
#
#        print(f"{key} harganya {value}")
#
#    Perhatiin huruf `f` sebelum kutip. Itu wajib.
#
#  JANGAN LUPA
#    Kasih garis pembatas di atas dan bawah, biar rapi:
#        print("--------------Menu---------------")
#        ...loopnya di sini...
#        print("--------------....---------------")
#
#  HASIL YANG DIHARAPKAN (kira-kira, belum rapi)
#    --------------Menu---------------
#    pizza harganya 300
#    ikan harganya 200
#    laptop harganya 1000
#    ayam harganya 200
#    sttik harganya 599
#    gelas harganya 100
#    --------------....---------------
#
# ---------------------------------------------------------------------
# KODE KAMU DI SINI (langkah 2)




# =====================================================================
#  LANGKAH 3 - RAPIIN TAMPILANNYA
# =====================================================================
#
#  TUJUAN
#    Bikin titik duanya lurus sejajar, dan harganya pakai 2 angka koma.
#
#  MASALAHNYA
#    Nama makanan panjangnya beda-beda, jadi berantakan:
#        pizza harganya 300
#        laptop harganya 1000        <- nggak lurus
#
#  PETUNJUK - LEBAR TETAP
#    Di dalam f-string, tambahin titik dua terus angka lebarnya:
#
#        f"{key:5}"      <- dipaksa selebar 5 huruf
#
#    Kalau namanya kependekan, sisanya diisi spasi otomatis.
#    Kalau kepanjangan (kayak "laptop" yang 6 huruf), ya nggak dipotong.
#
#  PETUNJUK - 2 ANGKA DI BELAKANG KOMA
#        f"{value:.2f}"  <- 300 jadi 300.00
#
#    Artinya: f = format desimal, .2 = dua angka di belakang koma.
#
#  PETUNJUK - HURUF KECIL SEMUA
#    Tempel `.lower()` di ujung string, SETELAH kutip penutup:
#
#        print(f"....".lower())
#
#    Ini bikin SELURUH baris jadi huruf kecil, termasuk kata "Rupiah".
#
#  TUGASNYA
#    Ubah print di langkah 2 jadi format: nama, spasi, titik dua,
#    harga 2 koma, terus kata "Rupiah". Semua huruf kecil.
#
#  HASIL YANG DIHARAPKAN (persis kayak gini)
#    --------------Menu---------------
#    pizza : 300.00 rupiah
#    ikan  : 200.00 rupiah
#    laptop : 1000.00 rupiah
#    ayam  : 200.00 rupiah
#    sttik : 599.00 rupiah
#    gelas : 100.00 rupiah
#    --------------....---------------
#
#  PERTANYAAN BUAT DIPIKIR
#    Kenapa baris "laptop" tetep nggak lurus sama yang lain?
#    Coba ganti angka 5 tadi jadi angka lain. Ngerti sekarang?
#
# ---------------------------------------------------------------------
# (edit kode langkah 2 di atas, nggak usah nulis baru)


# =====================================================================
#  LANGKAH 4 - SIAPKAN WADAH BELANJAAN
# =====================================================================
#
#  TUJUAN
#    Bikin tempat nampung pesanan, dan tempat nyimpen total harga.
#
#  KENAPA HARUS DIBIKIN DULUAN?
#    Python nggak bisa masukin barang ke wadah yang belum ada.
#    Kalau langsung `cart.append("pizza")` tanpa bikin `cart` duluan,
#    hasilnya NameError.
#
#    Analoginya: mau naruh belanjaan tapi keranjangnya belum diambil.
#
#  YANG HARUS DIBIKIN
#    - `cart`  = list KOSONG        (bentuknya: [] )
#    - `total` = angka NOL          (bentuknya: 0  )
#
#    Kenapa cart pakai list bukan dict? Karena kita cuma butuh nyimpen
#    nama pesanannya doang, harganya udah ada di `menu`.
#
#  TARUH DI MANA?
#    Di ATAS kode yang nyetak menu. Wadah disiapin sebelum dipakai.
#
#  CARA NGETES
#    Belum keliatan apa-apa. Yang penting jalanin, jangan sampai error.
#
# ---------------------------------------------------------------------
# KODE KAMU DI SINI (langkah 4 - taruh di bagian atas file)




# =====================================================================
#  LANGKAH 5 - TANYA PESANAN TERUS-TERUSAN
# =====================================================================
#
#  TUJUAN
#    Program nanya "mau pesen apa?" berulang kali, sampai user ketik "q".
#
#  MASALAHNYA
#    Kalau cuma `input()` sekali, user cuma bisa pesen satu barang.
#    Kita nggak tau user mau pesen berapa banyak. Bisa 1, bisa 10.
#    Jadi harus diulang, tapi nggak tau berapa kali.
#
#  PETUNJUK - ULANG TANPA BATAS
#        while True:
#            # ini bakal jalan selamanya
#
#    `True` artinya selalu benar, jadi nggak pernah berhenti sendiri.
#
#  PETUNJUK - CARA BERHENTI
#        if food == "q":
#            break
#
#    `break` = keluar paksa dari loop.
#    TANPA INI PROGRAM KAMU BAKAL NGE-HANG SELAMANYA.
#    (kalau kejadian, tekan Ctrl+C buat maksa berhenti)
#
#  PETUNJUK - INPUT
#        food = input("mau pesen apa?: ").lower()
#
#    Kenapa `.lower()` ditempel? Biar user ketik "PIZZA", "Pizza",
#    atau "pizza" hasilnya sama semua. Nanti kepake di langkah 6.
#
#  URUTAN DI DALAM LOOP
#    1. tanya (input)
#    2. cek kalau "q" -> break
#    3. (langkah 6 nanti masuk sini)
#
#  CARA NGETES
#    Jalanin. Ketik apa aja beberapa kali, terus ketik q.
#    Program harus berhenti dengan tenang, bukan error.
#
# ---------------------------------------------------------------------
# KODE KAMU DI SINI (langkah 5)




# =====================================================================
#  LANGKAH 6 - CUMA TERIMA MENU YANG ADA
# =====================================================================
#
#  TUJUAN
#    Kalau user pesen yang ada di menu -> masukin ke cart.
#    Kalau nggak ada -> jangan dimasukin.
#
#  MASALAHNYA
#    Sekarang user bisa ketik "batu" dan program nerima aja.
#    Nanti pas ngitung harga -> error, karena "batu" nggak punya harga.
#
#  PETUNJUK - CEK ADA APA NGGAK
#        menu.get(food)
#
#    Ini nyari `food` di dalam menu.
#      - ketemu     -> balikin harganya, misal 300
#      - nggak ada  -> balikin None (artinya: kosong, nihil)
#
#    Kenapa nggak pakai `menu[food]` aja? Karena kalau nggak ketemu
#    dia langsung ERROR dan program mati. `.get()` lebih sopan,
#    dia cuma bilang None.
#
#    Jadi cara ngeceknya:
#        elif menu.get(food) is not None:
#            # berarti ada di menu
#
#    Baca pelan-pelan: "kalau menu.get(food) BUKAN None" = "kalau ketemu".
#
#  PETUNJUK - MASUKIN KE CART
#        cart.append(food)
#
#    `.append()` nambah satu item ke ujung list.
#
#  CARA NGETES
#    Sementara tambahin `print(cart)` di dalam loop.
#    Pesen: pizza, ikan, batu, q
#    Cart harus isi ['pizza', 'ikan'] doang. "batu" nggak boleh masuk.
#    Kalau udah bener, hapus print-nya.
#
# ---------------------------------------------------------------------
# (tambahin ke dalam loop langkah 5 di atas)


# =====================================================================
#  LANGKAH 7 - HITUNG TOTAL HARGA
# =====================================================================
#
#  TUJUAN
#    Jumlahin harga semua barang yang ada di cart.
#
#  MASALAHNYA
#    `cart` isinya NAMA doang: ['pizza', 'ikan'].
#    Yang kita butuh HARGA. Harganya ada di `menu`.
#    Jadi tiap nama harus ditukar dulu jadi harga.
#
#  PETUNJUK
#        for food in cart:
#            total = total + menu.get(food)
#
#    Bacanya: ambil nama satu-satu dari cart, cari harganya di menu,
#    tambahin ke total.
#
#    Bisa disingkat jadi:  total += menu.get(food)
#    Artinya persis sama.
#
#  TARUH DI MANA?
#    Di LUAR while, SETELAH loopnya selesai.
#    Perhatiin indentasinya (jarak dari kiri) - jangan masuk ke dalam while.
#
#  KENAPA `total` HARUS 0 DULUAN?
#    Karena baris `total = total + ...` butuh nilai `total` yang lama.
#    Kalau belum pernah diisi, Python bingung -> NameError.
#    Itu gunanya langkah 4 tadi.
#
#  CARA NGETES
#    Pesen pizza (300) + ikan (200), terus q.
#    print(total) harus keluar 500.
#
# ---------------------------------------------------------------------
# KODE KAMU DI SINI (langkah 7)




# =====================================================================
#  LANGKAH 8 - PAJAK DAN TAGIHAN AKHIR
# =====================================================================
#
#  TUJUAN
#    Hitung pajak 10%, terus cetak tagihannya.
#
#  PETUNJUK - PERSEN
#    10% itu sama dengan 0.10 dalam angka.
#    Jadi pajaknya:  total * 0.10
#    Tagihan akhir:  total + pajak
#
#    Simpan di dua variabel: `pajak` dan `after`.
#
#  PETUNJUK - CETAK
#    Pakai f-string kayak langkah 2, tapi isinya dua variabel.
#
#  CARA NGETES
#    Pesen pizza + ikan, terus q.
#
#  HASIL YANG DIHARAPKAN
#    your bill is 500 rupiah and with pajak jadi 550.0
#
#    (500 + 50 = 550. Kalau angkamu beda, cek lagi langkah 7.)
#
# ---------------------------------------------------------------------
# KODE KAMU DI SINI (langkah 8)




# =====================================================================
#  SELESAI - CEK SENDIRI
# =====================================================================
#
#  Jalanin sekali lagi dari awal, ketik: pizza, ikan, q
#  Harus keluar persis kayak gini:
#
#    --------------Menu---------------
#    pizza : 300.00 rupiah
#    ikan  : 200.00 rupiah
#    laptop : 1000.00 rupiah
#    ayam  : 200.00 rupiah
#    sttik : 599.00 rupiah
#    gelas : 100.00 rupiah
#    --------------....---------------
#    Pesen apa?
#    mau pesen apa?: mau pesen apa?: mau pesen apa?:
#    your bill is 500 rupiah and with pajak jadi 550.0
#
#  CHECKLIST:
#    [ ] menu tampil rapi, harga 2 angka koma, semua huruf kecil
#    [ ] bisa pesen berkali-kali
#    [ ] ketik "q" berhenti, nggak error
#    [ ] ketik makanan ngawur nggak bikin program mati
#    [ ] total harganya bener
#    [ ] pajak 10% kehitung
#
#
# =====================================================================
#  TANTANGAN TAMBAHAN (kerjain kalau 8 langkah udah kelar)
# =====================================================================
#
#  Program di atas masih ada kekurangan. Perbaiki satu-satu:
#
#  A. USER NGGAK DIKASIH TAU
#     Sekarang kalau ketik "batu", program diem aja. User bingung,
#     dikira udah masuk keranjang.
#     -> Tambahin `else:` yang nyetak "maaf, ga ada menu itu".
#
#  B. KERANJANGNYA NGGAK KELIATAN
#     User nggak tau udah pesen apa aja.
#     -> Sebelum cetak tagihan, tampilkan isi cart satu per satu.
#
#  C. KALAU NGGAK PESEN APA-APA
#     Coba langsung ketik "q" di awal. Tagihannya jadi aneh.
#     -> Kasih pesan "keranjang kosong" kalau cart masih [].
#        Petunjuk cek list kosong:  if len(cart) == 0:
#
#  D. BARANG SAMA DIPESEN 2X
#     Coba pesen pizza, pizza, q. Totalnya bener nggak?
#     Tapi tampilannya gimana? Bisa nggak jadi "pizza x2"?
#
#  E. ANGKANYA JELEK
#     "550.0" itu kurang enak dibaca. Bikin jadi "550.00"
#     atau bahkan "Rp 550".
#     -> Petunjuk: pakai format spec kayak langkah 3.
#
#  F. TYPO DI MENU
#     Ada satu nama makanan yang salah ketik. Cari, terus betulin.
#
# =====================================================================
