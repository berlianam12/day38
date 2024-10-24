contacts = {}
def tampilkan_kontak():
    if contacts:
        print("\n--- Daftar Kontak ---")
        for id_kontak, info in contacts.items():
            print(f"ID: {id_kontak}, Nama: {info['nama']}, Nomor Telepon: {info['nomor']}")
    else:
        print("\nTidak ada kontak yang tersedia.")
def tambah_kontak():
    id_kontak = input("Masukkan ID kontak: ")
    if id_kontak in contacts:
        print("ID sudah ada. Gunakan ID lain.")
    else:
        nama = input("Masukkan nama: ")
        nomor = input("Masukkan nomor telepon: ")
        contacts[id_kontak] = {"nama": nama, "nomor": nomor}
        print("Kontak berhasil ditambahkan!")
def ubah_kontak():
    id_kontak = input("Masukkan ID kontak yang akan diubah: ")
    if id_kontak in contacts:
        print(f"Kontak ditemukan: {contacts[id_kontak]}")
        nama_baru = input("Masukkan nama baru: ")
        nomor_baru = input("Masukkan nomor telepon baru: ")
        contacts[id_kontak] = {"nama": nama_baru, "nomor": nomor_baru}
        print("Kontak berhasil diubah!")
    else:
        print("Kontak tidak ditemukan.")
def hapus_kontak():
    id_kontak = input("Masukkan ID kontak yang akan dihapus: ")
    if id_kontak in contacts:
        del contacts[id_kontak]
        print("Kontak berhasil dihapus!")
    else:
        print("Kontak tidak ditemukan.")
def aplikasi_kontak():
    while True:
        print("\n--- Aplikasi Contact List ---")
        print("1. Tampilkan semua kontak")
        print("2. Tambah kontak baru")
        print("3. Ubah kontak")
        print("4. Hapus kontak")
        print("5. Keluar")
        
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_kontak()
        elif pilihan == "2":
            tambah_kontak()
        elif pilihan == "3":
            ubah_kontak()
        elif pilihan == "4":
            hapus_kontak()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi Contact List.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")
aplikasi_kontak()
