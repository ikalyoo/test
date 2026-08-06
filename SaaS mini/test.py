
tanggal = input("Tanggal (YYYY-MM-DD)   : ")
mati    = input("Ayam mati hari ini     : ")
afkir   = input("Ayam afkir hari ini    : ")
bagus   = input("Telur bagus (butir)    : ")
retak   = input("Telur retak (butir)    : ")

mati  = int(mati)
afkir = int(afkir)
bagus = int(bagus)
retak = int(retak)

pop_awal = 1000  
def hitung_populasi(pop_awal, mati, afkir):
    if pop_awal < mati + afkir:
        return "Error: Populasi awal tidak cukup untuk jumlah ayam mati dan afkir."
    pop_akhir = pop_awal - mati - afkir
    return pop_akhir

def hitung_total_telur(bagus, retak):
    total_telur = bagus + retak
    return total_telur

def insight (total_telur):
    if total_telur < 100:
        return "Produksi telur rendah, perlu evaluasi pakan dan kesehatan ayam."
    elif total_telur > 200:
        return "Produksi telur sedang, pertahankan kualitas pakan dan manajemen kandang."
    else: 
        return "produksi telur tinggi, gaskan ekspansi44"
print()  
print("===== RINGKASAN HARIAN =====")
print(f"Tanggal     : {tanggal}")
print(f"hitung populasi ayam akhir : {hitung_populasi(1000, mati, afkir)} ekor")
print(f"Total telur : {hitung_total_telur(bagus, retak)} butir")
print(f"Insight     : {insight(hitung_total_telur(bagus, retak))}")
