def awal(*range):
    print("Toko Buah Koperasi UNJANI Yogyakarta")
    jumlah_buah = int(input("Masukkan banyak buah yang dibeli : "))

    for i in range(jumlah_buah) :
        buah = input(f"Buah {i+1} : ")
        args += (buah,)

    print("Buah yang anda beli adalah : ")
    for i,buah in enumerete (args):
        print(f"{i+1}, {buah}")
    print("Terimakasih")
awal()