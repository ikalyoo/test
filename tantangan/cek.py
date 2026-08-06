# Auto-checker buat tantangan.py
# Jalanin dari folder Absensi:  python tantangan/cek.py

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tantangan as t

lolos = 0
total = 0
gagal_di = None


def cek(level, nama, dapat, harus):
    global lolos, total, gagal_di
    total += 1
    if dapat == harus:
        lolos += 1
        print(f"  [OK]    {nama}")
        return True
    print(f"  [SALAH] {nama}")
    print(f"          harusnya : {harus!r}")
    print(f"          dapatnya : {dapat!r}")
    if gagal_di is None:
        gagal_di = level
    return False


def coba(fn, *args):
    """Jalanin fungsi, tangkap error biar checker nggak mati."""
    try:
        return fn(*args)
    except Exception as e:
        return f"<ERROR: {type(e).__name__}: {e}>"


print()
print("=" * 56)
print(" CEK TANTANGAN ABSENSI")
print("=" * 56)

# --- LEVEL 1 ---------------------------------------------------
print("\nLEVEL 1 - total_hadir")
cek(1, 'total_hadir(["hadir", "alpha", "hadir", "izin"])',
    coba(t.total_hadir, ["hadir", "alpha", "hadir", "izin"]), 2)
cek(1, 'total_hadir(["hadir", "hadir", "hadir"])',
    coba(t.total_hadir, ["hadir", "hadir", "hadir"]), 3)
cek(1, 'total_hadir(["alpha", "izin"])',
    coba(t.total_hadir, ["alpha", "izin"]), 0)
cek(1, "total_hadir([])  <- list kosong",
    coba(t.total_hadir, []), 0)

# --- LEVEL 2 ---------------------------------------------------
print("\nLEVEL 2 - rekap_status")
cek(2, 'rekap_status(["hadir", "alpha", "hadir", "izin", "sakit", "hadir"])',
    coba(t.rekap_status, ["hadir", "alpha", "hadir", "izin", "sakit", "hadir"]),
    {"hadir": 3, "izin": 1, "sakit": 1, "alpha": 1})
cek(2, "rekap_status([])  <- semua key tetap ada",
    coba(t.rekap_status, []),
    {"hadir": 0, "izin": 0, "sakit": 0, "alpha": 0})
cek(2, 'rekap_status(["sakit", "sakit"])',
    coba(t.rekap_status, ["sakit", "sakit"]),
    {"hadir": 0, "izin": 0, "sakit": 2, "alpha": 0})

# --- LEVEL 3 ---------------------------------------------------
print("\nLEVEL 3 - persen_hadir")
cek(3, 'persen_hadir(["hadir", "alpha"])',
    coba(t.persen_hadir, ["hadir", "alpha"]), 50.0)
cek(3, 'persen_hadir(["hadir", "hadir", "alpha"])  <- bulatin 1 koma',
    coba(t.persen_hadir, ["hadir", "hadir", "alpha"]), 66.7)
cek(3, 'persen_hadir(["hadir"])',
    coba(t.persen_hadir, ["hadir"]), 100.0)
cek(3, "persen_hadir([])  <- JANGAN ZeroDivisionError",
    coba(t.persen_hadir, []), 0.0)

# --- LEVEL 4 ---------------------------------------------------
print("\nLEVEL 4 - daftar_nama & ambil_status")
data = [
    {"nama": "Budi", "status": "hadir"},
    {"nama": "Siti", "status": "alpha"},
    {"nama": "Agus", "status": "hadir"},
    {"nama": "Rina", "status": "alpha"},
]
cek(4, 'daftar_nama(data, "alpha")',
    coba(t.daftar_nama, data, "alpha"), ["Siti", "Rina"])
cek(4, 'daftar_nama(data, "hadir")',
    coba(t.daftar_nama, data, "hadir"), ["Budi", "Agus"])
cek(4, 'daftar_nama(data, "sakit")  <- nggak ada yang cocok',
    coba(t.daftar_nama, data, "sakit"), [])
cek(4, "ambil_status(data)",
    coba(t.ambil_status, data), ["hadir", "alpha", "hadir", "alpha"])
cek(4, "ambil_status([])",
    coba(t.ambil_status, []), [])

# --- LEVEL 5 ---------------------------------------------------
print("\nLEVEL 5 - buat_laporan")
total += 1
hasil = coba(t.buat_laporan, data, "2026-08-01")

if not isinstance(hasil, str):
    print("  [SALAH] buat_laporan harus RETURN string")
    print(f"          dapatnya : {hasil!r}")
    if gagal_di is None:
        gagal_di = 5
else:
    kurang = []
    for potongan, kenapa in [
        ("2026-08-01", "tanggal"),
        ("4", "total karyawan"),
        ("2", "jumlah hadir"),
        ("0", "jumlah izin/sakit"),
        ("50.0", "persen kehadiran"),
        ("Siti", "nama yang alpha"),
        ("Rina", "nama yang alpha"),
    ]:
        if potongan not in hasil:
            kurang.append(f"{potongan!r} ({kenapa})")

    if kurang:
        print("  [SALAH] laporan kurang lengkap, nggak nemu:")
        for k in kurang:
            print(f"            - {k}")
        print("\n          laporan kamu:")
        for baris in hasil.splitlines():
            print(f"            | {baris}")
        if gagal_di is None:
            gagal_di = 5
    else:
        lolos += 1
        print("  [OK]    laporan lengkap")
        print("\n          laporan kamu:")
        for baris in hasil.splitlines():
            print(f"            | {baris}")

# --- HASIL -----------------------------------------------------
print()
print("=" * 56)
print(f" SKOR: {lolos}/{total}")
if lolos == total:
    print(" SEMUA LOLOS. Lanjut ke bagian BONUS.")
else:
    print(f" Benerin dulu LEVEL {gagal_di}, baru lanjut ke bawahnya.")
print("=" * 56)
print()
