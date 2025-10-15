#1
def konversi_suhu(value, suhu):
    if suhu == 'C':
        #mengonversikan Celsius ke Fahrenheit
        return (value * 9/5) + 32
    elif suhu == 'F':
        #mengonversikan Fahrenheit ke Celsius
        return (value - 32) * 5/9
    else:
        raise ValueError("Suhu tidak valid. Gunakan" / " 'C' untuk Celsius atau 'F' untuk Fahrenheit.")
print(konversi_suhu(200, 'C'))
print(konversi_suhu(38, 'F'))

#no 2
luas_lingkaran = lambda jejari: 3.14 *jejari ** 2

n = float(input("Masukkan nilai jejari lingkaran: "))

print("Luas lingkaran dengan jejari", n, "adalah", luas_lingkaran(n))