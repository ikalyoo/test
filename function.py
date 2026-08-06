# building a machine to think

def result_total(price, discount, tax):
    return price * (1 - discount) * (1 + tax)


def total_bayar(ikan):
        total = 0
        for harga in ikan:
             total += harga
        return total
    

hasil = []



while True:
    harga = input("masukin harga ya, ketik q kalau selesai: ")
    if harga == "q":
        break

    hasil.append(result_total(float(harga), 0.11, 0.15))

print(f"barang yang harus kamu bayar adalah {hasil}")
print(f'total nya adalah {total_bayar(hasil)}')



