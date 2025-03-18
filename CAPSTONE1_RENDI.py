# Pada Capstone kali ini saya memilih case study data pasien di Rumah Sakit dengan nama RS HASAN SADIKIN
# Data hanya bersifat dummy, bukan data pasien asli
# kolom data yang ditampilkan adalah:
#   1. ID
#   2. Nama
#   3. Kamar pasien
#   4. Diagnosa sakit
#   5. No telp. keluarga pasien
#   6. Nama keluarga 

# Capstone kali ini akan membuat fitur:
#   1. Log-in dan log out user
#   2. Show database RS
#   3. Tambah database RS
#   4. delete database RS
#   5. update database RS

# Berikut adalah data set pasien

data_pasien = [
        {'ID':1,'nama pasien':'Ahmad Fadhil',
         'kamar pasien': 305,
         'diagnosa':'Demam berdarah',
         'no telp keluarga':'081234567890',
         'nama keluarga':'Siti Aminah'},
        {'ID':2,'nama pasien':'Liana Putri',
         'kamar pasien': 208,
         'diagnosa':'Radang tenggorokan',
         'no telp keluarga':'082233445566',
         'nama keluarga':'Andi Pratama'},
        {'ID':3,'nama pasien':'Budi Santoso',
         'kamar pasien': 405,
         'diagnosa':'Asma',
         'no telp keluarga':'083344556677',
         'nama keluarga':'Dewi Sartika'},
        {'ID':4,'nama pasien':'Rina Mariani',
         'kamar pasien': 101,
         'diagnosa':'Asma berat',
         'no telp keluarga':'085123456789',
         'nama keluarga':'Yudi Prakoso'}]

data_user = [{'ID':1,'user':'Admin','password':'Admin123'}]

# Setelah data ditampilkan diatas, langkah selanjutnya adalah membuat fitur dengan cara membuat dictionary sebagai berikut:

# Membuat dictionary sub menu dengan isi sebagai berikut
def submenu_show_data(data_pasien):
    print('--------------------------------------------')
    while True:
        print('''
MENU DATABASE PASIEN

Silahkan pilih menu dibawah ini: 
1. Show all data pasien
2. Pencarian data pasien
3. Show user dashboard
4. Kembali ke menu utama
--------------------------------------------\n''')
        user_input = input('Pilih menu angka diatas: ')
        if not user_input.isdigit():
            print('Perintah hanya berupa angka')
            continue

        user_input = int(user_input)    
        if user_input == 1:
            show_data(data_pasien)
        elif user_input == 2:
            search_data_pasien(data_pasien)
        elif user_input == 3:
            shows_data(data_user)
        elif user_input == 4:
            return
        else:
            print('Menu tidak tersedia! coba lagi')

#   1. Dictionary function pertama yaitu menampilkan seluruh data pasien dengan cara:
#       a. membuat keyword show data dengan object key data pasien
#       b. menampilkan header
#       c. menampilkan data dengan looping sejumlah data pasien  

def show_data(data_pasien):
    # Cek apakah ada data pasien di list
    if not data_pasien:
        print('Data Kosong\n')
        return
    # Jika ada, command lanjut
    # Print header tabel
    print('ID      | Nama Pasien           | Kamar Pasien  | Diagnosa                       | No Telp Keluarga      | Nama Keluarga')
    print('------- | --------------------- | ------------- | ------------------------------ | --------------------- | --------------------')
    
    # print data dengan looping sebanyak data yang ada, dengan range dari Len data pasien
    for pasien in data_pasien: 
        # Ambil data diagnosa dari pasien
        riwayat_diagnosa = pasien.get("diagnosa", "")
        if isinstance(riwayat_diagnosa, list):
            riwayat_diagnosa = ", ".join(riwayat_diagnosa)

        print(f'{pasien['ID']:<7} | {pasien['nama pasien']:<21} | {pasien['kamar pasien']:<13} | {riwayat_diagnosa:<30} | {pasien['no telp keluarga']:<21} | {pasien['nama keluarga']}')
    print('-------------------------------------------------------------------------------------------------------------------------------\n') # Print line kosong untuk memberi space baru
def shows_data(data_user):
    # Cek apakah ada data pasien di list
    if not data_user:
        print('Data Kosong\n')
        return
    # Jika ada, command lanjut
    # Print header tabel
    print('ID      | Username              | Password        ')
    print('------- | --------------------- | -------------   ')
    # print data dengan looping sebanyak data yang ada, dengan range dari Len data pasien
    for i in range(len(data_user)): 
        print(f'{data_user[i]['ID']:<7} | {data_user[i]['user']:<21} | {data_user[i]['password']:<13}')
    print('----------------------------------------------- \n') # Print line kosong untuk memberi space baru

#   2. Dictionary function kedua yaitu function untuk pencarian data pasien dengan cara:
#       a. Buat list kosong untuk menyimpan hasil pencarian
#       d. sistem mencari data yang cocok 

def find_data(data_pasien, value):
    # Buat list kosong untuk menyimpan hasil pencarian
    value = str(value).lower()
    hasil_pencarian = []  

    # Sistem akan membuat loop untuk mencari data baik key dan valuenya dari dictionary value_pasien dalam data_pasien
    # Apabila ditemukan kecocokan pada data_pasien, sistem akan menambahkan ke dalam list hasil_pencarian

    for pasien in data_pasien:
    # Cek setiap key dalam dictionary
        for val in pasien.values():
            if value in str(val).lower():
                hasil_pencarian.append(pasien)
                break 
    return hasil_pencarian if hasil_pencarian else None

#   3. Dictionary function ke-tiga yaitu pencarian data pasien dengan cara:
#       a. user meng-input data apapun yang ingin dicari
#       d. setelah menemukan data nya, sistem akan menampilkan table data pasien yang dimaksud

def search_data_pasien(data_pasien):
    while True:
        show_data(data_pasien)
        pencarian_value = input('Masukkan nilai yang ingin dicari (misalnya nama pasien, diagnosa, atau no telp): ')

        if not pencarian_value:
            print('Input tidak boleh kosong! Coba lagi.')
            continue

        # Cari data berdasarkan input dari pengguna
        hasil_pencarian = find_data(data_pasien, pencarian_value)

        # Tampilkan hasil pencarian
        if hasil_pencarian:
            print('Hasil pencarian:\n')
            show_data(hasil_pencarian)
        else:
            print('Data tidak ditemukan.')
        
        while True:
            input_user = input ('\n Apakah anda ingin melakukan pencarian lagi(Y/N)? ')
            if input_user.lower() == 'y':
                break
            elif input_user.lower() == 'n':
                return
            else:
                print ('Input salah, silahkan ketik (Y/N)')



# Membuat dictionary sub menu dengan isi sebagai berikut

def submenu_add_data(data_pasien):
    while True:
        print('''--------------------------------------------
MENU TAMBAH DATABASE

Silahkan pilih menu dibawah ini: 
1. Tambah data pasien
2. Bulk tambah data pasien
3. Tambah diagnosa pasien
4. Tambah User dashboard
5. Kembali ke menu utama
--------------------------------------------\n''')
        user_input = input('Pilih menu angka diatas: ')
        if not user_input.isdigit():
            print('Perintah hanya berupa angka')
            continue

        user_input = int(user_input)    
        if user_input == 1:
            add_data(data_pasien)
        elif user_input == 2:
            bulk_add_data(data_pasien)
        elif user_input == 3:
            tambah_diagnosa(data_pasien)
        elif user_input == 4:
            adds_data(data_user)
        elif user_input == 5:
            return
        else:
            print('Menu tidak tersedia! coba lagi')

#   4. Dictionary function keempat yaitu menambah data pasien dengan cara:
#       a. membuat keyword add data pasien
#       b. membuat kolom input data apa saja yang akan ditambah
#       c. menampilkan keterangan data sukses diinput

def add_data(data_pasien):
    # Membuat daftar kolom pasien, tipe string untuk input huruf dan tipe integer untuk input angka
    dictionary_pasien = {'nama pasien':'','kamar pasien':0,'diagnosa':'','no telp keluarga':0,'nama keluarga':''}
    
    # Menampilkan data pasien terlebih dahulu agar lebih user-friendy dengan dictionary ke-1
    show_data(data_pasien)
    print('--MENU TAMBAH DATA-- \n')

    # user melakukan input data diri pasien, khusus no kamar dan no hp melakukan looping apabila terjadi error input 
    input_ID = max([pasien['ID'] for pasien in data_pasien])+1
    while True:
        input_nama = input('Silahkan ketik nama pasien: ')
        if len(input_nama) > 21:
            print('Nama pasien terlalu panjang! Maksimal 21 karakter.')
            continue
        break

    while True:
        try:
            input_kamar_pasien = int(input('Masukan kamar pasien baru (maksimal 3 angka): '))
            if len(str(input_kamar_pasien)) > 3:
                print('Nomor kamar terlalu panjang! Maksimal 3 angka.')
                continue
            elif any(pasien['kamar pasien'] == input_kamar_pasien for pasien in data_pasien):
                print('Nomor kamar sudah terdaftar! Coba kamar lain.')
                continue
            break
        except ValueError:
            print('Input harus berupa angka! Coba lagi.')

    while True:
        input_diagnosa = input('Silahkan ketik diagnosa pasien: ')
        if len(input_diagnosa) > 30:
            print('Nama diagnosa terlalu panjang! Maksimal 30 karakter.')
            continue
        break
    
    while True:
        input_no_telp_keluarga = input('Masukan no telpon keluarga (dimulai dari 08): ')
        # Cek apakah input hanya berisi angka
        if not input_no_telp_keluarga.isdigit():
            print('Input harus berupa angka! Coba lagi.')
            continue
        # Cek apakah nomor sudah ada dalam database
        if any(pasien['no telp keluarga'] == input_no_telp_keluarga for pasien in data_pasien):
            print('no telp keluarga sudah terdaftar, silahkan input no telp lain.')
            continue
        # Cek apakah nomor dimulai dengan '08'
        if not input_no_telp_keluarga.startswith('08'):
            print('Angka harus dimulai dari 08, Coba lagi.')
            continue
        if len(input_no_telp_keluarga) > 15:
            print('Nomor telpon terlalu panjang! Maksimal 15 angka.')
            continue
        break
    
    while True:
        input_nama_keluarga = input('Silahkan ketik nama keluarga: ')
        if len(input_nama_keluarga) > 21:
            print('Nama keluarga terlalu panjang! Maksimal 21 karakter.')
            continue
        break
    # Data hasil input disimpan pada dictionary, lalu kemudian akan di tambahkan ke data pasien terbaru
    dictionary_pasien['ID'] = input_ID
    dictionary_pasien['nama pasien'] = input_nama
    dictionary_pasien['kamar pasien'] = input_kamar_pasien
    dictionary_pasien['diagnosa'] = input_diagnosa
    dictionary_pasien['no telp keluarga'] = input_no_telp_keluarga
    dictionary_pasien['nama keluarga'] = input_nama_keluarga
    show_data([dictionary_pasien])
    
    # Konfirmasi sebelum menambah
    # Jika iya, data akan ditambah, sistem akan kembali ke menu sub add data
    # Jika tidak, data batal ditambah, sistem akan kembali ke menu sub add data
    while True:
        konfirmasi = input('apakah data pasien ingin ditambah(Y/N)? ')
        if konfirmasi.lower() == 'y':
            data_pasien.append(dictionary_pasien)
            print('Data pasien berhasil ditambah\n')
            show_data(data_pasien)
            return
        elif konfirmasi.lower() == 'n':
            print('Penambahan data pasien dibatalkan\n')
            return
        else:
            print('Perintah salah! Silahkan pilih antara (Y/N)')

#   5. Dictionary function kelima yaitu menambah data pasien secara bulk dengan cara:
#       a. membuat berapa banyak pasien yang ditambah
#       b. isi kolom pasien
#       c. menampilkan keterangan data sukses diinput

def bulk_add_data(data_pasien):
    while True:
        try:
            jumlah_pasien = int(input('Masukkan jumlah pasien yang ingin ditambahkan: '))
            if jumlah_pasien <= 0:
                print('Jumlah pasien harus lebih dari 0! Coba lagi.')
                continue

    # Buat list pasien baru bulk
            pasien_baru = [] 

            for i in range(jumlah_pasien):
                print(f'\nMasukkan data pasien ke-{i+1}:')
                input_ID = len(data_pasien) + len(pasien_baru) + 1  # ID otomatis bertambah
                input_nama = input('Nama pasien: ')
                
                while True:
                    try:
                        input_kamar = int(input('Nomor kamar pasien (maksimal 3 angka): '))
                        if len(str(input_kamar)) > 3:
                            print('Nomor kamar terlalu panjang! Maksimal 3 angka.')
                            continue
                        elif any(pasien['kamar pasien'] == input_kamar for pasien in data_pasien + pasien_baru):
                            print('Nomor kamar sudah terdaftar! Coba kamar lain.')
                            continue
                        break
                    except ValueError:
                        print('Input harus berupa angka! Coba lagi.')

                while True:
                    input_diagnosa = input('Silahkan ketik diagnosa pasien: ')
                    if len(input_diagnosa) > 21:
                        print('Nama diagnosa terlalu panjang! Maksimal 30 karakter.')
                        continue
                    break

                while True:
                    input_no_telp = input('Nomor telepon keluarga (diawali 08): ')
                    if not input_no_telp.isdigit():
                        print('Input harus berupa angka!')
                        continue
                    elif not input_no_telp.startswith('08'):
                        print('Nomor harus diawali dengan 08!')
                        continue
                    elif any(pasien['no telp keluarga'] == input_no_telp for pasien in data_pasien + pasien_baru):
                        print('Nomor telepon sudah terdaftar! Coba nomor lain.')
                        continue
                    elif len(input_no_telp) > 15:
                        print('Nomor telpon terlalu panjang! Maksimal 15 angka.')
                        continue
                    else:
                        break

                input_nama_keluarga = input('Nama keluarga pasien: ')

                # Simpan data sementara ke list pasien_baru
                pasien_baru.append({
                    'ID': input_ID,
                    'nama pasien': input_nama,
                    'kamar pasien': input_kamar,
                    'diagnosa': input_diagnosa,
                    'no telp keluarga': input_no_telp,
                    'nama keluarga': input_nama_keluarga
                })

            # Menampilkan data pasien sebelum disimpan
            print('\nData pasien yang akan ditambahkan:\n')
            show_data(pasien_baru) 

            # Konfirmasi sebelum menyimpan
            while True:
                konfirmasi = input('\nApakah Anda yakin ingin menyimpan data ini? (Y/N): ')
                if konfirmasi.lower() == 'y':
                    data_pasien.extend(pasien_baru)  # Simpan ke data utama
                    print('Semua data pasien berhasil ditambahkan!\n')
                    break
                elif konfirmasi.lower() == 'n':
                    print('Penambahan pasien dibatalkan\n')
                    return   
                else:
                    print('Perintah salah! Coba lagi \n')
                    return
            break

        except ValueError:
            print('Input harus berupa angka! Coba lagi')

#   6. Dictionary function keenam yaitu menambah diagnosa dengan cara:
#       a. memilih ID
#       b. isi kolom diagnosa
#       c. menampilkan keterangan data sukses diinput

def tambah_diagnosa(data_pasien):
    show_data(data_pasien)  # Menampilkan data pasien agar user tahu ID yang benar

    while True:
        try:
            input_id = input('Masukkan ID pasien untuk menambahkan tambahan diagnosa: ')
            if not input_id.isdigit():
                print('ID harus berupa angka! Coba lagi.')
                continue

            input_id = int(input_id)

            # Mencari pasien berdasarkan ID
            pasien_terpilih = None
            for pasien in data_pasien:
                if pasien['ID'] == input_id:
                    pasien_terpilih = pasien
                    break
            if not pasien_terpilih:
                print('Pasien dengan ID tersebut tidak ditemukan!')
                continue
            print('Pasien ditemukan:')
            show_data([pasien_terpilih])
        
            diagnosa_baru = input('Masukkan tambahan diagnosa baru: ')

            if not diagnosa_baru:
                print('Isi diagnosa tidak boleh kosong!')
                return

        # Pastikan diagnosa tersimpan sebagai list
            if isinstance(pasien["diagnosa"], str):
                pasien["diagnosa"] = [pasien["diagnosa"]]  # Ubah ke list jika awalnya string
                konfirmasi = input(f"\nApakah Anda yakin ingin menambahkan diagnosa '{diagnosa_baru}' untuk {pasien['nama pasien']}? (Y/N): ").strip().lower()

                if konfirmasi == "y":
                    pasien["diagnosa"].append(diagnosa_baru)
                    print(f"\nTambahan diagnosa '{diagnosa_baru}' berhasil ditambahkan untuk pasien {pasien['nama pasien']}.\n")
                else:
                    print("\nPenambahan diagnosa dibatalkan.\n")
                    return

                print("\nData pasien setelah update:")
                show_data(data_pasien)
                break
        except ValueError:
            print("\nInput tidak valid! Harus berupa angka.\n")
#   7. Dictionary function ketujuh yaitu menambah user dengan cara:
#       a. ketik data diri user dan password
#       b. menampilkan keterangan data sukses diinput

def adds_data(data_user):
    print('\n-- Tambah User Dashboard --')
    
    while True:
        input_ID = max([user['ID'] for user in data_user])+1
        user_baru = input('Masukkan username baru: ')
        if len(user_baru) > 21:
            print('Nama User terlalu panjang! Maksimal 21 karakter.')
            continue
        # Cek apakah username sudah ada
        if any(user['user'] == user_baru for user in data_user):
            print('Username sudah terdaftar! Silakan gunakan username lain.')
            continue
        
        password_baru = input('Masukkan password: ')
        if len(password_baru) > 13:
            print('assword terlalu panjang! Maksimal 13 karakter.')
            continue
        konfirm_password = input('Konfirmasi password: ')
        
        # Validasi password jika tidak sesuai sistem akan minta ulang
        if password_baru != konfirm_password:
            print('Konfirmasi password tidak cocok! Coba lagi.')
            continue

        konfirmasi = input('apakah data user ingin ditambah(Y/N)? ')
        if konfirmasi.lower() == 'y':
            data_user.append({'ID': input_ID, 'user': user_baru, 'password': password_baru})
            print(f'User {user_baru} berhasil ditambahkan!\n')
            break
        elif konfirmasi.lower() == 'n':
            print('Penambahan data user dibatalkan\n')
            return
        else:
            print('Perintah salah! Silahkan pilih antara (Y/N)')
        



# Membuat dictionary sub menu dengan isi sebagai berikut

def submenu_delete_data(data_pasien):
    while True:
        print('''--------------------------------------------
MENU DELETE PASIEN

Silahkan pilih menu dibawah ini: 
1. Hapus data pasien
2. Kembali ke menu utama
--------------------------------------------\n''')
        user_input = input('Pilih menu angka diatas: ')
        if not user_input.isdigit():
            print('Perintah hanya berupa angka')
            continue

        user_input = int(user_input)    
        if user_input == 1:
            delete_data(data_pasien)
        elif user_input == 2:
            return
        else:
            print('Menu tidak tersedia! coba lagi')

#   8. Dictionary funtion ke-delapan yaitu menghapus data pasien dengan cara:
#       a. membuat input ID mana yang akan dihapus
#       b. Sistem akan otomatis menghapus satu baris ID tersebut
#       c. menampilkan keterangan data sukses diinput            

def delete_data(data_pasien):
    # Cek apakah data kosong sebelum mencoba mencari ID
    if not data_pasien:
        print('DATA EMPTY\n')
        return

    # user melakukan input no ID pasien dengan melakukan looping apabila terjadi error input
    # Menampilkan data pasien terlebih dahulu agar lebih user-friendy dengan dictionary ke-1
    show_data(data_pasien)
    while True:
        print('--MENU HAPUS DATA-- \n')
        try:
            input_ID_pasien = input('Ketik nomor ID pasien yang akan dihapus: ')
            if not input_ID_pasien.isdigit():
                print('Perintah hanya berupa angka')
                continue
    # Proses cek apakah ada data ID input di database
            input_ID_pasien = int(input_ID_pasien)
            pasien_dihapus = None
            for pasien in data_pasien:  
                if pasien['ID'] == input_ID_pasien:
                    pasien_dihapus = pasien
                    break
            if pasien_dihapus is None:
                print('Data tidak ditemukan, silahkan coba lagi\n')
                continue
            
            # Tampilkan data yang ingin dihapus            
            print('\nData yang akan dihapus:')
            show_data([pasien_dihapus])

            # Konfirmasi sebelum menghapus
            konfirmasi = input('Apakah anda ingin menghapus data pasien tersebut(Y/N)? ')
            if konfirmasi.lower() == 'y':
                data_pasien.remove(pasien)
                print('Data pasien berhasil dihapus\n')
                show_data(data_pasien)
                break
            elif konfirmasi.lower() == 'n':
                print('Penghapusan data pasien dibatalkan\n')
                return
            else:
                print('Perintah salah! Silahkan pilih antara (Y/N)')
                continue
            break
        except ValueError:
            print('Input harus berupa angka! Coba lagi.')

# Membuat dictionary sub menu dengan isi sebagai berikut
def submenu_update_data(data_pasien):
    while True:
            print('''--------------------------------------------
MENU UPDATE PASIEN

Silahkan pilih menu dibawah ini: 
1. Update data spesifik pasien
2. Kembali ke menu utama
--------------------------------------------\n''')
            user_input = input('Pilih menu angka diatas: ')
            if not user_input.isdigit():
                print('Perintah hanya berupa angka')
                continue

            user_input = int(user_input)    
            if user_input == 1:
                update_data(data_pasien)
            elif user_input == 2:
                return
            else:
                print('Menu tidak tersedia! coba lagi')


#   9. Dictionary function ke-sembilan yaitu update data pasien dengan cara:
#       a. user meng-input ID mana yang akan dirubah
#       b. setelah menemukan ID tersebut, user meng-input kolom mana yang akan dirubah
#       c. khusus no kamar tidak bisa duplikat, hanya bisa ditempati 1 pasien untuk 1 kamar
#       d. menampilkan keterangan data sukses diupdate

def update_data(data_pasien):
    # Menampilkan data pasien terlebih dahulu agar lebih user-friendy dengan dictionary ke-1
    show_data(data_pasien)
    print('--MENU UPDATE DATA-- \n')

    # user melakukan input no ID pasien dengan melakukan looping apabila terjadi error input
    while True:
        try:
            input_ID_pasien = input('Ketik nomor ID pasien yang akan diupdate: ')
            if not input_ID_pasien.isdigit():
                print('Perintah hanya berupa angka')
                continue
    # Proses cek apakah ada data ID input di database
            input_ID_pasien = int(input_ID_pasien)
            pasien_list = [pasien for pasien in data_pasien if pasien['ID'] == input_ID_pasien]
            pasien_update = pasien_list[0] if pasien_list else None
            
            if pasien_update is None:
                print("Data tidak ditemukan, silahkan coba lagi.")
            print('\nData pasien yang akan diupdate:')
            show_data([pasien_update])
            break
        
        except ValueError:
            print('Input tidak valid! Coba lagi.')

    kolom_valid = ['nama pasien', 'kamar pasien', 'diagnosa', 'no telp keluarga', 'nama keluarga']

    # user melakukan input kolom pasien ingin di-edit dengan melakukan looping apabila terjadi error input
    # Apabila sesuai dengan kolom yang ada, maka akan lanjut untuk input value
    # Apabila tidak sesuai dengan kolom yang ada, maka akan meminta kembali input kolom yang ingin di-edit
    while True:
        input_nama_kolom = input('Masukkan nama kolom yang ingin di-edit: ')
        if input_nama_kolom not in kolom_valid:
            print('Kolom tidak ada silahkan ulangi\n')
        else:
            break
        
    # User menginput update value sesuai dengan kolom yang telah diinput sebelumnya
    # Khusus no kamar dan no hp melakukan looping apabila terjadi error input 
    if input_nama_kolom.lower() == 'nama pasien':
        ubah_value = input('Ketik nama buah baru ')
    elif input_nama_kolom.lower() == 'kamar pasien':
        while True:
            try:
                ubah_value = int(input('Masukan kamar pasien baru (hanya angka): '))
                if any(pasien['kamar pasien'] == ubah_value for pasien in data_pasien):
                    print('Kamar pasien sudah terdaftar, silahkan input kamar lain.')
                else:
                    break
            except ValueError:
                print('Input harus berupa angka! Coba lagi.')

    elif input_nama_kolom.lower() == 'diagnosa':
        daftar_diagnosa = pasien_update.get("diagnosa", "")

        # Jika diagnosa masih dalam bentuk string, ubah menjadi list
        if isinstance(daftar_diagnosa, str):
            daftar_diagnosa = [diagnosa.strip() for diagnosa in daftar_diagnosa.split(",") if diagnosa.strip()]

        # Tambahkan diagnosa tambahan jika ada
        tambahan_diagnosa = pasien_update.get("tambah_diagnosa", [])
        if tambahan_diagnosa:
            daftar_diagnosa.extend(tambahan_diagnosa)

        # Tampilkan daftar diagnosa terbaru
        print("\nDiagnosa saat ini:")
        for nomor, diagnosa in enumerate(daftar_diagnosa, start=1):
            print(f"{nomor}. {diagnosa}")

        # Pilih diagnosa yang ingin diubah
        while True:
            try:
                nomor_ganti = int(input("\nMasukkan nomor diagnosa yang ingin diganti: "))
                if 1 <= nomor_ganti <= len(daftar_diagnosa):
                    break
                else:
                    print("Nomor tidak valid! Pilih sesuai daftar.")
            except ValueError:
                print("Input harus berupa angka!")

        # Input diagnosa baru
        diagnosa_baru = input("Masukkan diagnosa baru pasien: ")

        # Konfirmasi perubahan
        konfirmasi = input(f'\nAnda akan mengganti "{daftar_diagnosa[nomor_ganti - 1]}" dengan "{diagnosa_baru}". Confirm? (Y/N): ')
        if konfirmasi.lower() == 'y':
            daftar_diagnosa[nomor_ganti - 1] = diagnosa_baru  # Update diagnosa terpilih
            pasien_update["diagnosa"] = daftar_diagnosa  # Simpan ke data pasien
            print("\n SUKSES UPDATE DATA!\n")
            # Tampilkan data yang telah diperbarui
            show_data(data_pasien)
            return
        else:
            print("\n Perubahan dibatalkan.")     
       
    elif input_nama_kolom.lower() == 'no telp keluarga':
        while True:
            ubah_value = input('Masukan no telpon baru keluarga (dimulai dari 08): ')
            if ubah_value.isdigit() and ubah_value.startswith('08'):
                if any(pasien['no telp keluarga'] == ubah_value for pasien in data_pasien):
                    print('Nomor telepon keluarga sudah terdaftar, silahkan input nomor lain.')
                else:
                    break
            else:
                print('Angka harus dimulai dari 08, Coba lagi.')
    elif input_nama_kolom.lower() == 'nama keluarga':
        ubah_value = input('Silahkan ketik nama baru keluarga: ')
    
    print(f'\nanda akan merubah {pasien_update[input_nama_kolom]} menjadi {ubah_value}')
    while True:
        konfirmasi = input('Apakah anda yakin ingin mengubahnya?(Y/N): ')
        if konfirmasi.lower() == 'y':
            pasien_update[input_nama_kolom] = ubah_value
            print('\nSUKSES UPDATE DATA!\n')
            show_data(data_pasien)
            return
        elif konfirmasi.lower() == 'n':    
            print('Update dibatalkan')
            return
        else:
            print('\nPerintah salah! Coba lagi')
    
#       Dictionary menu login dengan flow seperti berikut:
#       a. user meng-input user dan password yang sesuai
#       d. menu login akan lanjutkan ke menu utama


def menu_login(data_pasien):
    while True:
        print('DASHBOARD RS HASAN SADIKIN')
        input_user = input('USER: ')
        input_password = input('PASSWORD: ')
        
        valid_user = None
        for user in data_user:
            if user['user'] == input_user and user['password'] == input_password:
                valid_user = user
                break
        if valid_user:
            print(f'''\nSELAMAT DATANG {input_user}
--------------------------------------------''')
            menu_utama(data_pasien)  
            break
        else:
            print('User atau Password salah! Silahkan coba lagi.\n')

# Membuat dictionary menu utama dengan isi sebagai berikut

def menu_utama(data_pasien):  
    while True:
        print('''\nSELAMAT DATANG DI RS HASAN SADIKIN
          
Silahkan pilih menu dibawah ini: 
1. Show database RS
2. Tambah database RS
3. delete database RS
4. update database RS
5. Log out
6. Exit Program
            ''')
        input_menu = input('Pilih menu angka diatas: ')
        if not input_menu.isdigit():
            print('Perintah hanya berupa angka')
            continue

        input_menu = int(input_menu)
        if input_menu == 1:
            submenu_show_data(data_pasien)
        elif input_menu == 2:
            submenu_add_data(data_pasien)
        elif input_menu == 3:
            submenu_delete_data(data_pasien)
        elif input_menu == 4:
            submenu_update_data(data_pasien)
        elif input_menu == 5:
            menu_login(data_pasien)
        elif input_menu == 6:
            print('Terima kasih telah menggunakan jasa RS HASAN SADIKIN')
            break
        else:
            print('Menu tidak tersedia! coba lagi')
            continue


#----------------PROMPTING WORKFLOW-------------------------#

menu_login(data_pasien)

# Catatan user: Admin Password: Admin123







