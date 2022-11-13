from datetime import datetime

tgl = datetime.now()
tanggal = tgl.strftime("%d-%m-%Y %H:%M:%S")
nama = input("Masukkan Nama :\n-> ")

def list_menu():    
    print("""
    ========================================

    Halo """+nama+""", Selamat Datang di Resto Rafi
    ========================================
    \nlist menu :
    1. Bebek goreng : Rp 25.000
    2. Nasi goreng : Rp 15.000
    3. Mi goreng : Rp 13.000
    4. Es teh : Rp 3.000
    """)

list_menu()

pilihan_user = str(input("Masukkan angka sesuai dengan menu yang tersedia =\n-> "))
jumlah_pesanan = int(input("Jumlah dibeli :\n-> "))

if pilihan_user == "1":
    nama_menu = "Bebek goreng"
    harga_menu = 25000
    harga = harga_menu*jumlah_pesanan
elif pilihan_user == "2":
    nama_menu = "Nasi goreng"
    harga_menu = 15000
    harga = harga_menu*jumlah_pesanan
elif pilihan_user == "3":
    nama_menu = "Mi goreng"
    harga_menu = 13000
    harga = harga_menu*jumlah_pesanan
elif pilihan_user == "4":
    nama_menu = "Es Teh"
    harga_menu = 3000
    harga = harga_menu*jumlah_pesanan
else:
    print("Maaf menu yang dipilih tidak tersedia di list menu")
    exit()

no_hp = input("Masukkan No HP :\n-> ")
alamat = input("Masukkan Alamat :\n-> ")





print("""
    ========================================
                    INVOICE
    ========================================
    """)
print("\nTanggal : "+tanggal)
print("\n\nNama : "+nama)
print("Alamat : "+alamat)
print("No HP : "+no_hp)
print("Menu :",nama_menu)
print("Jumlah Pesanan :", jumlah_pesanan)
print("------------------------------")
print(str(harga_menu)+" x "+str(jumlah_pesanan))
print("Harga :", harga)
print("------------------------------")