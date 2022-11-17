


loop = "n"

user_id = 0 

# Membuat user dengan menggunakan list dan dictionary
users = [
    {
        "id": "1234",
        "no_rekening": "1234567890",
        "username": "juhari",
        "pin": "654321",
        "saldo": 0
    },
{
        "id": "4321",
        "no_rekening": "0987654321",
        "username": "Why Juhari",
        "pin": "123456",
        "saldo": 250000000
    }
]

# Fungsi cek login
def cek_login(p):
    for user in users:
        if user["pin"] == p:
            return user
    return False

# Fungsi cek User
def cek_user(id):
    for i in range(len(users)):
        if users[i]['id'] == str(id):
            return int(i)
    return -1

# Cek Rekening
def cek_rekening(no):
    for i in range(len(users)):
        if users[i]['no_rekening'] == no:
            return int(i)
    return -1


# Fungsi untuk mentransfer uang
def transfer_uang(uang, no_rekeing):
    index1 = cek_user(user_id)
    index2 = cek_rekening(no_rekeing)

    if index1 >= 0:
        if users[index1]['saldo'] >= int(uang):
            users[index1]['saldo'] = users[index1]['saldo'] - int(uang)  
            users[index2]['saldo'] = users[index2]['saldo'] + int(uang) 
            print("")
            print("=======================================")
            print(f"Anda berhasil mentransfer uang Rp. {int(uang):,}\n ke rekening {no_rekeing}")
            print(f"Sisa saldo anda adalah Rp. {users[index1]['saldo']:,}")
            print("=======================================")
        else:
            print("Ops Saldo Anda Tidak Cukup!")

# Fungsi untuk menarik uang
def tarik_uang(uang):
    index1= cek_user(user_id)

    if index1 >= 0:
        if users[index1]['saldo'] >= int(uang):
            users[index1]['saldo'] = users[index1]['saldo'] - int(uang)
            print("")
            print("=======================================")
            print(f"Anda berhasil menarik uang Rp. {int(uang):,}")
            print(f"Sisa saldo anda adalah Rp. {users[index1]['saldo']:,}")
            print("=======================================")
        else:
            print("")
            print("Ops Saldo Anda Tidak Cukup!")
            print("")


status_login = False
use_atm = "y"

while use_atm == "y":

    # Cek Login User Atm
    while not status_login:
        print("")
        print("=================================")
        print("== Silahkan Masukkan Pin Anda! ==")
        print("=================================")
        print("")
        pin = str(input("Masukkan PIN ATM : "))

        cek_L = cek_login(pin)

        if cek_L:
            print("")
            print("=======================================")
            print(f"====== Selamat Datang {cek_L['username']} ======")
            print("=======================================")
            user_id = cek_L['id']
            status_login = True
            loop = "y"
        else:
            print("="*19)
            print("Ops PIN anda salah!")
            print("="*19)

    # Bagian Menu Pada Atm
    while loop == "y" and status_login:
        u = users[cek_user(user_id)]
        print("")
        print("=======================================")
        print("== SELAMAT DATANG DI ATM SALAM ERROR ==")
        print("=======================================\n")
        print("=======================")
        print("== 1. Cek Saldo Anda ==")
        print("== 2. Transfer Uang  ==")
        print("== 3. Ambil Uang     ==")
        print("== 4. LogOut         ==")
        print("== 5. Keluat ATM     ==")
        print("=======================")

        menu = int(input("Silahkan Pilih Menu! : "))

        if menu == 1:
            print("=====================================")
            print(f"Saldo anda adalah Rp. {u['saldo']:,}")
            print("=====================================")
            loop = "n"
        elif menu == 2:
            print("=============================")
            print("Silahkan Masukkan No Rekening")
            norek_tujuan = input("Masukkan No Rekening Tujuan! : ")
            cek_norek = cek_rekening(norek_tujuan)
            
            if cek_norek >= 0:
                print("")
                print("Nomor Rekening Ditemukan, \nSilahkan Pilih Nominal\n Yang Akan DI Transfer")
                print("")

                print("===== JUMLAH TRANSFER ======")
                print("=============================") 
                print("1. 500.000 \t 2. 1.000.000")
                print("3. 2.000.000 \t 4. 3.000.000 ")
                print("5. 3.500.000 \t 6. Jumlah Yang Lain ")
                print("=============================") 
            
                pilih = int(input("Pilih Jumlah Transfer Diatas! : "))
                
                if pilih == 1:
                    transfer_uang(500000, norek_tujuan)
                elif pilih == 2:
                    transfer_uang(1000000, norek_tujuan)
                elif pilih == 3:
                    transfer_uang(2000000, norek_tujuan)
                elif pilih == 4:
                    transfer_uang(3000000, norek_tujuan)
                elif pilih == 5:
                    transfer_uang(3500000, norek_tujuan)
                elif pilih == 6:
                    nominal = input("Masukkan Nominal Yang Akan Di transfer! : ")
                    transfer_uang(nominal, norek_tujuan)
                    print("")
                    loop = "n"
                else:
                    print("Pilihan Tidak Tersedia")
            else:
                print("")
                print("Nomor Rekening Tidak Ditemukan, \n Atau Tidak Terdaftar")
                print("")
                loop = "n"
        
        elif menu == 3:
            print("")
            print("===== JUMLAH PENARIKAN ======")
            print("=============================") 
            print("1. 500.000 \t 2. 1.000.000")
            print("3. 2.000.000 \t 4. 3.000.000 ")
            print("5. 3.500.000 \t 6. Jumlah Yang Lain ")
            print("=============================") 
            
            pilih = int(input("Pilih Jumlah Penarikan Diatas! : "))
            if pilih == 1:
                tarik_uang(500000)
            elif pilih == 2:
                tarik_uang(1000000)
            elif pilih == 3:
                tarik_uang(2000000)
            elif pilih == 4:
                tarik_uang(3000000)
            elif pilih == 5:
                tarik_uang(3500000)
            elif pilih == 6:
                nominal = input("Masukkan Nominal Yang Akan Di Tarik! : ")
                tarik_uang(nominal)
            else:
                print("Pilihan Tidak Tersedia")

            print("")
            loop = "n"

        elif menu == 4:
            status_login = False
        
        elif menu == 5:
            status_login = False
            use_atm = "n"
            print("="*16)
            print("== ATM KELUAR ==")
            print("="*16)

        if status_login == True:
            input("Kembali ke menu (ENTER)\n")
            loop = "y"


