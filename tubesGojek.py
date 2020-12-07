def namaBesar_(nama_):
    """ Program untuk membuat nama yang dicantumkan user menjadi kapital pada huruf awalnya """
    global nama
    nama_besar = []
    for n in nama:
        nama_besar += n 
    nama_besar[0] = nama_besar[0].upper()
    nama = ""
    for n in nama_besar:
        nama += n 
    return nama

def angkaDisplay(angka):
    """ Program untuk membuat angka angka yang akan ditampilkan pada prgram memiliki tanda koma sehingga lebih mudah untuk dibaca pengguna """
    list_ = []
    for a in angka:
        list_ += a
    list_ = list_[::-1] 
    x = 0
    y = 3
    koma = ","
    baru = []
    while True: 
        if len(list_) - 1 >= y  :
            potongan = list_[x:y]
            for p in potongan:
                baru += p
            baru += koma
        elif len(list_) - 1 < y : 
            potongan = list_[x:]
            for p in potongan:
                baru += p
            break
        x += 3
        y += 3 
    baru = baru[::-1]
    hasil = "" 
    for h in baru :
        hasil += h
        
    return hasil

def topUp_():
    """ Program untuk melakukan fitur top up pada aplikasi gojek """
    global gopay
    print(" ")
    print("-----" * 20)
    print(" ")
    print("Selamat menggunakan fitur Top Up")
    print(" ")
    jumlahTopup = 0
    print("Jumlah Top Up minimal Rp.10.000")
    while True:
        jumlahTopup = int(input("Masukkan nominal Top Up Anda: "))
        if jumlahTopup >= 10000:
            break
        else:
            print("Top up minimal Rp.10.000")
    bank = [[1,"BCA"],
        [2,"BNI"],
        [3,"BRI"],
        [4,"Mandiri"]]
    while True:
        noBank = 0
        for b in bank:
            print ("Tekan " + str(b[0]) + " untuk bank " + b[1])
        noBank = int(input("Pilih bank kartu debit : "))
        if noBank >= 1 and noBank <= 4:
            break
        else:
            print("Tolong pilih bank yang sesuai dengan nomor yang tertera")
    gopay += jumlahTopup
    print("Top Up sejumlah "+ str(jumlahTopup) + " dari bank " + bank[noBank-1][1] + " berhasil")
    print("Saldo gopay " + nama + " sekarang Rp." + angkaDisplay(str(gopay)))
    return gopay

def goride():
    """ Program untuk melakukan pemesanan goride """
    global gopay
    print(" ")
    print("-----" * 20)
    print(" ")
    harga = [[0,1,5000],
        [1,3,8000],
        [3,5,10000],
        [5,7,12000],
        [7,10,15000],
        [10,15,18000],
        [15,20,20000]]  
    print("Selamat menggunakan fitur goride")
    print(" ")
    print("Berikut biaya per Km:")
    for h in harga:
        angka = str(h[2])
        print("Jarak antara " + str(h[0]) + " km dan " + str(h[1]) + " km : Rp." + angkaDisplay(angka)) 
    print("Jarak lebih dari 20 km : Rp.1,000/km")
    jarak = int(input("Masukkan jarak perjalanan Anda: "))
    for h in harga: 
        if jarak >= h[0] and jarak <= h[1]:
            biayaTotal = h[2]
            break 
        elif jarak > 20:
            biayaTotal = jarak * 1000
            break  
    while True:
        if gopay < biayaTotal:
            while gopay < biayaTotal:
                print(" ")
                print("Mohon maaf, saldo gopay yang dimiliki "+ nama +" tidak mencukupi, "+ nama + " butuh gopay sebesar Rp." + angkaDisplay(str(biayaTotal)) )
                print("Gopay yang " + nama + " miliki hanyalah Rp." + angkaDisplay(str(gopay)))
                butuh = biayaTotal - gopay
                print("Silahkan " + nama + " melakukan top up gopay dengan nominal minimal sebesar Rp." + angkaDisplay(str(butuh))) 
                mau_topup = input("Apakah " + nama + " ingin melakukan top up gopay(y/n): ")
                if mau_topup == "y":
                    gopay = topUp_()
                elif mau_topup == "n":
                    break 
        if gopay >= biayaTotal:
            print(" ")
            print("Pemesanan goride atas nama "+ nama + " untuk perjalanan sejauh "+ str(jarak) +" km senilai Rp." + angkaDisplay(str(biayaTotal)) + " telah berhasil" )
            print("Driver yang dipesan " + nama + " akan segera datang\nDriver juga akan mengontak " + nama + " melalui nomor hp yang tercantum yaitu "+ nohape + " atau melalui email yaitu " + email)
            gopay = int(gopay) - biayaTotal 
            break 
        elif mau_topup == "n":
            break
    return

def gocar():
    """ Program untuk melakukan pemesanan gocar """
    global gopay
    print(" ")
    print("-----" * 20)
    print(" ")
    print("Selamat menggunakan fitur gocar")
    print(" ")
    print("Berikut mobil yang tersedia dengan biaya per km: ")
    tipemobil = [["Mobil Kecil",1, 4, 10000],
        ["Mobil Sedang",5,6,12000],
        ["Mobil Besar",7,8,14000]]
    for t in tipemobil:
        print(t[0] + " dapat menampung sebanyak " + str(t[1]) + " sampai " + str(t[2]) + " orang dengan biaya Rp." + angkaDisplay(str(t[3])))
    penumpang = int(input("Silahkan "+ nama +" memasukkan penumpang untuk layanan Gocar "+ nama +": "))
    while penumpang > 8:
        print("Maaf, kami tidak memiliki mobil yang dapat menampung sebanyak "+ str(penumpang) + " penumpang")
        penumpang = int(input("Silahkan "+ nama +" memasukkan penumpang untuk layanan Gocar "+ nama +": "))
    jarak = int(input("Masukkan jarak perjalanan Anda: "))
    for t in tipemobil:
        if penumpang >= t[1] and penumpang <= t[2]:
            biayaTotal = int(jarak) * int(t[3])
    while True:
        if gopay < biayaTotal:
            while gopay < biayaTotal:
                print(" ")
                print("Mohon maaf, saldo gopay yang dimiliki "+ nama +" tidak mencukupi, "+ nama + " butuh gopay sebesar Rp." + angkaDisplay(str(biayaTotal)) )
                print("Gopay yang " + nama + " miliki hanyalah Rp." + angkaDisplay(str(gopay)))
                butuh = biayaTotal - gopay
                print("Silahkan " + nama + " melakukan top up gopay dengan nominal minimal sebesar Rp." + angkaDisplay(str(butuh))) 
                mau_topup = input("Apakah " + nama + " ingin melakukan top up gopay(y/n): ")
                if mau_topup == "y":
                    gopay = topUp_()
                elif mau_topup == "n":
                    break 
        if gopay >= biayaTotal:
            print(" ")
            print("Pemesanan gocar atas nama "+ nama +" untuk perjalanan sejauh "+ str(jarak) +" km dengan biaya Rp." + angkaDisplay(str(biayaTotal)) + " telah berhasil" )
            print("Driver yang dipesan " + nama + " akan segera datang\nDriver juga akan mengontak " + nama + " melalui nomor hp yang tercantum yaitu "+ nohape + " atau melalui email yaitu " + email)
            gopay = int(gopay) - biayaTotal 
            break 
        elif mau_topup == "n":
            break
    return 

# -------------------- Program untuk meminta identitas user --------------------
print("-----" * 20)
print(" ")
print("Selamat datang di aplikasi Gojek versi beta 0.0") 
print("Silahkan masukkan data identitas Anda")
while True:
    nama = input("Masukkan nama Anda: ")
    if nama == "":
        print("Tolong isi kolom nama dengan sesuai")
    else: 
        break
while True:
    email = input("Masukkan email anda: ")
    cek = []
    for e in email:
        cek.append(e)
    if "@" in cek and cek[-4:] == [".","c","o","m"]: 
        break 
    else:
        print("Email yang Anda cantumkan harus mempunyai '@' dan diakhiri dengan '.com'")
while True:
    nohape = input("Masukkan nomor handphone Anda: ")
    if len(nohape) >= 11 :
        break
    else:
        print("Nomor handphone Anda tidak sesuai")
# -------------------- Program untuk meminta identitas user --------------------

# -------------------- Program untuk mencetak data identitas yang telah di-input user --------------------
gopay = 0
nama = namaBesar_(nama)
print("Hi " + nama + ", selamat menggunakan aplikasi gojek versi beta 0.0 ") 
print(" ")
print("Identitas Anda ")
data = [["Nama" , nama],
    ["Email",email],
    ["Nomor Handphone",nohape]]         
for d in data:
    print(d[0] + " : " + d[1]) 
# -------------------- Program untuk mencetak data identitas yang telah di-input user --------------------

# -------------------- Program untuk mencetak display awal --------------------
while True: 
    print(" ") 
    print("-----" * 20)
    print(" ")
    print("Saldo gopay " + nama + " : Rp " + angkaDisplay(str(gopay)))
    print(" ")
    print("Berikut fitur yang tersedia di aplikasi ini: ")
    fitur = ["Go-ride","Go-car","Top Up"]
    biayaTotal = 0
    for f in fitur:
        print(f)
        tekan = [["1","Go-ride"],
            ["2","Go-car"],
            ["3","Top Up"]] 
    print(" ")
    for t in tekan:
        print("Tekan " + t[0] + " untuk menggunakan fitur " + t[1])
    print("Tekan 4 untuk keluar dari aplikasi")
    while True:
        pilihFitur = input("Silahkan memilih fitur mana yang " + nama + " ingin pakai: ")
        if int(pilihFitur) in range(1,5):
            break  
        else:
            print("Tolong pastikan Anda mengetik fitur yang ingin Anda gunakan dengan benar")  
# -------------------- Program untuk mencetak display awal --------------------

# -------------------- Program untuk menjalankan program pemesanan goride --------------------
    if pilihFitur == "1": 
        goride()
# -------------------- Program untuk menjalankan program pemesanan goride --------------------

# -------------------- Program untuk menjalankan program pemesanan gocar --------------------
    elif pilihFitur ==  "2": 
        gocar()
# -------------------- Program untuk menjalankan program pemesanan gocar --------------------

# -------------------- Program untuk menjalankan program top up --------------------
    elif pilihFitur == "3":
        topUp_()
# -------------------- Program untuk menjalankan program top up --------------------

# -------------------- Program untuk menyelesaikan penggunaan program --------------------
    elif pilihFitur == "4": 
        print("Terima kasih telah menggunakan aplikasi gojek ini, selamat menjalani hari hari dengan bahagia \U0001f600") 
        break 
# -------------------- Program untuk menyelesaikan penggunaan program --------------------

# -------------------- Program untuk menanyakan kepada user apakah user masih ingin menggunakan fitur lainnya atau tidak --------------------
    print(" ")
    jawaban = input(f"Apakah {nama} masih ingin menggunakan fitur gojek lainnya(y/n)? ")
    if jawaban == "y":
        print(" ")
    elif jawaban == "n":
        print("Terima kasih telah menggunakan aplikasi gojek ini, selamat menjalani hari hari dengan bahagia \U0001f600") 
        break
# -------------------- Program untuk menanyakan kepada user apakah user masih ingin menggunakan fitur lainnya atau tidak --------------------