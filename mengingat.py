# =============================================================
# KODE LAMA (ada bug) - dinonaktifkan karena SyntaxError di baris terakhir.
# Disimpan sebagai pembanding saja.
# =============================================================
#
# tanggal = input("Tanggal (YYYY-MM-DD)   : ")
# mati    = input("Ayam mati hari ini     : ")
# afkir   = input("Ayam afkir hari ini    : ")
# bagus   = input("Telur bagus (butir)    : ")
# retak   = input("Telur retak (butir)    : ")
#
# mati  = int(mati)
# afkir = int(afkir)
# bagus = int(bagus)
# retak = int(retak)
#
# pop_awal = 1000
#
# def hitung_populasi(pop_awal, mati, afkir):
#     pop_awal -= mati + afkir
#     return pop_awal
#
# def hitung_total_telur(bagus, retak):
#     total_telur = bagus - retak
#     return total_telur
#
# def insight (hitung_populasi):
#     if hitung_populasi < 500:
#         return "Populasi ayam rendah, perlu evaluasi pakan dan kesehatan ayam."
#     elif hitung_populasi > 800:
#         return "Populasi ayam tinggi, pertahankan kualitas pakan dan manajemen kandang."
#     else:
#         return "Populasi ayam sedang, pantau terus kondisi kandang."
#
# def insight_telur (hitung_total_telur):
#     if hitung_total_telur_siap_jual < 100:
#         return "Produksi telur rendah, perlu evaluasi pakan dan kesehatan ayam."
#     elif hitung_total_telur > 200:
#         return "Produksi telur sedang, pertahankan kualitas pakan dan manajemen kandang."
#     else:
#         return "produksi telur tinggi, gaskan ekspansi44"
#
# print(f"Tanggal     : {tanggal}")
# print(f"hitung populasi ayam akhir : {hitung_populasi} ekor")
# print(f"Total telur : {hitung_total_telur(bagus, retak)} butir")
# print(f"insight_telur : {insight_telur(hitung_total_telur(bagus, retak))}")
# print(f"Insight     : {insight((pop_awal, mati, afkir))}")43


# =============================================================
# VERSI 1 - PERBAIKAN MINIMAL
# Struktur dan gaya kode dibiarkan sama seperti aslinya.
# Yang diubah cuma bug-nya.
# =============================================================

POP_AWAL = 1000


def hitung_populasi(pop_awal, mati, afkir):
    return pop_awal - (mati + afkir)


def hitung_total_telur(bagus, retak):
    # FIX: total = bagus + retak (dulu dikurangi, itu selisih bukan total)
    return bagus + retak


def insight(populasi):
    # FIX: parameter dinamai `populasi`, bukan `hitung_populasi`.
    # Dulu nama parameter menutupi nama fungsi, bikin bug susah kelihatan.
    if populasi < 500:
        return "Populasi ayam rendah, perlu evaluasi pakan dan kesehatan ayam."
    elif populasi > 800:
        return "Populasi ayam tinggi, pertahankan kualitas pakan dan manajemen kandang."
    else:
        return "Populasi ayam sedang, pantau terus kondisi kandang."


def insight_telur(total):
    # FIX: pakai `total` (dulu baris ini menyebut nama yang tidak ada -> NameError)
    if total < 100:
        return "Produksi telur rendah, perlu evaluasi pakan dan kesehatan ayam."
    # FIX: label "sedang" dan "tinggi" dulu ketuker
    elif total > 200:
        return "Produksi telur tinggi, gaskan ekspansi!"
    else:
        return "Produksi telur sedang, pertahankan kualitas pakan dan manajemen kandang."


def versi_1():
    tanggal = input("Tanggal (YYYY-MM-DD)   : ")
    mati    = int(input("Ayam mati hari ini     : "))
    afkir   = int(input("Ayam afkir hari ini    : "))
    bagus   = int(input("Telur bagus (butir)    : "))
    retak   = int(input("Telur retak (butir)    : "))

    populasi = hitung_populasi(POP_AWAL, mati, afkir)
    total    = hitung_total_telur(bagus, retak)

    print()
    print(f"Tanggal          : {tanggal}")
    # FIX: fungsinya dipanggil pakai kurung, dulu yang tercetak objek fungsinya
    print(f"Populasi akhir   : {populasi} ekor")
    print(f"Total telur      : {total} butir")
    # FIX: yang dikirim ke insight() hasil hitungnya, bukan tuple (pop_awal, mati, afkir)
    print(f"Insight populasi : {insight(populasi)}")
    print(f"Insight telur    : {insight_telur(total)}")


# =============================================================
# VERSI 2 - VERSI RAPI
# Hasilnya sama, tapi input divalidasi, perhitungan dipisah dari
# tampilan, dan laporannya dirakit di satu tempat.
# =============================================================

POPULASI_AWAL = 1000
BATAS_POPULASI_RENDAH = 500
BATAS_POPULASI_TINGGI = 800
BATAS_TELUR_RENDAH = 100
BATAS_TELUR_TINGGI = 200


def tanya_angka(pesan):
    """Terus tanya sampai user isi bilangan bulat >= 0."""
    while True:
        jawaban = input(pesan).strip()
        if jawaban.isdigit():
            return int(jawaban)
        print("  -> Isi dengan angka bulat (contoh: 12). Coba lagi.")


def buat_laporan(tanggal, mati, afkir, bagus, retak):
    """Kembalikan dict berisi semua angka hasil hitungan."""
    total_telur = bagus + retak
    persen_retak = (retak / total_telur * 100) if total_telur else 0.0

    return {
        "tanggal": tanggal,
        "populasi_awal": POPULASI_AWAL,
        "mati": mati,
        "afkir": afkir,
        "populasi_akhir": POPULASI_AWAL - mati - afkir,
        "telur_bagus": bagus,
        "telur_retak": retak,
        "total_telur": total_telur,
        "persen_retak": persen_retak,
    }


def insight_populasi_v2(populasi):
    if populasi < BATAS_POPULASI_RENDAH:
        return "Populasi rendah - evaluasi pakan dan kesehatan ayam."
    if populasi > BATAS_POPULASI_TINGGI:
        return "Populasi tinggi - pertahankan kualitas pakan dan manajemen kandang."
    return "Populasi sedang - pantau terus kondisi kandang."


def insight_telur_v2(total_telur):
    if total_telur < BATAS_TELUR_RENDAH:
        return "Produksi telur rendah - evaluasi pakan dan kesehatan ayam."
    if total_telur > BATAS_TELUR_TINGGI:
        return "Produksi telur tinggi - gaskan ekspansi!"
    return "Produksi telur sedang - pertahankan kualitas pakan dan manajemen kandang."


def cetak_laporan(data):
    print()
    print("=" * 52)
    print(f" LAPORAN HARIAN KANDANG - {data['tanggal']}")
    print("=" * 52)
    print(f" Populasi awal    : {data['populasi_awal']:>6} ekor")
    print(f" Mati             : {data['mati']:>6} ekor")
    print(f" Afkir            : {data['afkir']:>6} ekor")
    print(f" Populasi akhir   : {data['populasi_akhir']:>6} ekor")
    print("-" * 52)
    print(f" Telur bagus      : {data['telur_bagus']:>6} butir")
    print(f" Telur retak      : {data['telur_retak']:>6} butir")
    print(f" Total telur      : {data['total_telur']:>6} butir")
    print(f" Persen retak     : {data['persen_retak']:>6.1f} %")
    print("-" * 52)
    print(f" Insight populasi : {insight_populasi_v2(data['populasi_akhir'])}")
    print(f" Insight telur    : {insight_telur_v2(data['total_telur'])}")
    print("=" * 52)


def versi_2():
    tanggal = input("Tanggal (YYYY-MM-DD)   : ").strip()
    mati    = tanya_angka("Ayam mati hari ini     : ")
    afkir   = tanya_angka("Ayam afkir hari ini    : ")
    bagus   = tanya_angka("Telur bagus (butir)    : ")
    retak   = tanya_angka("Telur retak (butir)    : ")

    cetak_laporan(buat_laporan(tanggal, mati, afkir, bagus, retak))


# =============================================================
# Ganti ke versi_2() kalau mau pakai versi rapi.
# =============================================================

if __name__ == "__main__":
    versi_1()
