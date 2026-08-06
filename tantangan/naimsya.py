# =============================================================
#  TANTANGAN: SISTEM ABSENSI
# =============================================================
#  Cara main:
#    1. Isi fungsi yang ada tulisan TODO.
#    2. Jalanin:  python tantangan/cek.py
#    3. Ulangi sampai semua level PASS.
#
#  ATURAN:
#    - Fungsi TIDAK BOLEH nyomot variabel global.
#      Semua data harus masuk lewat parameter.
#    - Fungsi harus RETURN, bukan print (kecuali disuruh).
#    - Kerjain urut. Level atas dipakai lagi di level bawah.
# =============================================================


# -------------------------------------------------------------
# LEVEL 1 - hitung yang hadir
# -------------------------------------------------------------
# Dikasih list status, misal: ["hadir", "alpha", "hadir", "izin"]
# Return jumlah yang statusnya "hadir".  -> 2
#
# JEBAKAN: fungsi ini bakal dites pakai list yang beda-beda.
# Kalau kamu nyomot variabel global, langsung ketahuan.
# -------------------------------------------------------------

def total_hadir(daftar):
    # TODO
    pass


# -------------------------------------------------------------
# LEVEL 2 - rekap semua status
# -------------------------------------------------------------
# Input : ["hadir", "alpha", "hadir", "izin", "sakit", "hadir"]
# Output: {"hadir": 3, "izin": 1, "sakit": 1, "alpha": 1}
#
# Keempat key harus selalu ada, walau nilainya 0.
# List kosong -> {"hadir": 0, "izin": 0, "sakit": 0, "alpha": 0}
#
# Baru buat kamu: bikin dict di dalam fungsi, terus di-return.
# -------------------------------------------------------------

def rekap_status(daftar):
    # TODO
    pass


# -------------------------------------------------------------
# LEVEL 3 - persentase kehadiran
# -------------------------------------------------------------
# Return persen yang hadir, dibulatkan 1 angka di belakang koma.
#
#   ["hadir", "alpha"]                 -> 50.0
#   ["hadir", "hadir", "alpha"]        -> 66.7
#   []                                 -> 0.0
#
# JEBAKAN: list kosong. Kalau nggak dijaga -> ZeroDivisionError.
# Petunjuk: round(nilai, 1)
# -------------------------------------------------------------

def persen_hadir(daftar):
    # TODO
    pass


# -------------------------------------------------------------
# LEVEL 4 - data beneran (list of dict)
# -------------------------------------------------------------
# Sekarang datanya kayak gini:
#
#   data = [
#       {"nama": "Budi",  "status": "hadir"},
#       {"nama": "Siti",  "status": "alpha"},
#       {"nama": "Agus",  "status": "hadir"},
#       {"nama": "Rina",  "status": "alpha"},
#   ]
#
# 4a. daftar_nama(data, status)
#     Return LIST nama yang statusnya sesuai, urutan tetap.
#     daftar_nama(data, "alpha") -> ["Siti", "Rina"]
#     Kalau nggak ada yang cocok -> []
#
# 4b. ambil_status(data)
#     Return LIST status doang -> ["hadir", "alpha", "hadir", "alpha"]
#     Ini jembatan biar fungsi level 1-3 bisa dipakai ke data baru.
#
# Baru buat kamu: dict di dalam list. Ambilnya orang["nama"].
# -------------------------------------------------------------

def daftar_nama(data, status):
    # TODO
    pass


def ambil_status(data):
    # TODO
    pass


# -------------------------------------------------------------
# LEVEL 5 - FINAL BOSS: laporan
# -------------------------------------------------------------
# buat_laporan(data, tanggal) -> RETURN string (jangan di-print!)
#
# Wajib pakai ulang fungsi level 1-4. Jangan ngitung ulang dari nol.
#
# Contoh hasil (formatnya bebas, yang penting isinya ada):
#
#   === ABSENSI 2026-08-01 ===
#   Total karyawan : 4
#   Hadir          : 2
#   Izin           : 0
#   Sakit          : 0
#   Alpha          : 2
#   Kehadiran      : 50.0%
#   Yang alpha     : Siti, Rina
#
# Syarat yang dicek:
#   - tanggalnya muncul
#   - angka total, hadir, izin, sakit, alpha muncul
#   - persen kehadiran muncul (misal "50.0")
#   - nama yang alpha muncul semua
#   - kalau nggak ada yang alpha -> tulis "-" atau "tidak ada"
#
# Petunjuk gabung nama jadi satu string:  ", ".join(list_nama)
# Petunjuk bikin string banyak baris   :  laporan += "...\n"
# -------------------------------------------------------------

def buat_laporan(data, tanggal):
    # TODO
    pass


# -------------------------------------------------------------
# BONUS (opsional) - baru kerjain kalau 1-5 udah PASS
# -------------------------------------------------------------
# Bikin program interaktif di bawah sini:
#   - tanya nama + status berulang sampai user ketik "q"
#   - status harus salah satu dari: hadir / izin / sakit / alpha
#     kalau salah, tanya lagi (jangan crash)
#   - terakhir, print buat_laporan(...)
#
# Taruh di dalam if __name__ ini, biar cek.py nggak ikut kena input().
# -------------------------------------------------------------

if __name__ == "__main__":
    pass
