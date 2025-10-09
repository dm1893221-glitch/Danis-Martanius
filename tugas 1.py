from datetime import date

class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.koleksi_buku = []        # daftar buku di perpustakaan
        self.daftar_anggota = []      # daftar anggota perpustakaan
        self.daftar_peminjaman = []   # catatan peminjaman

    def tambah_buku(self, buku):
        self.koleksi_buku.append(buku)
        print(f"Buku '{buku.judul}' berhasil ditambahkan ke koleksi.")

    def tambah_anggota(self, anggota):
        self.daftar_anggota.append(anggota)
        print(f"Anggota '{anggota.nama}' berhasil didaftarkan.")

    def pinjam_buku(self, anggota, buku):
        if buku in self.koleksi_buku and not buku.dipinjam:
            buku.dipinjam = True
            peminjaman = Peminjaman(anggota, buku, date.today())
            self.daftar_peminjaman.append(peminjaman)
            print(f"{anggota.nama} meminjam buku '{buku.judul}'.")
        else:
            print(f"Buku '{buku.judul}' tidak tersedia untuk dipinjam.")

    def tampilkan_status_peminjaman(self):
        print("\nStatus Peminjaman:")
        if not self.daftar_peminjaman:
            print("Belum ada peminjaman.")
        else:
            for p in self.daftar_peminjaman:
                print(f"- {p.anggota.nama} meminjam '{p.buku.judul}' pada {p.tanggal_pinjam}")


class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.dipinjam = False   # status apakah buku sedang dipinjam


class Anggota:
    def __init__(self, nama):
        self.nama = nama


class Peminjaman:
    def __init__(self, anggota, buku, tanggal_pinjam):
        self.anggota = anggota
        self.buku = buku
        self.tanggal_pinjam = tanggal_pinjam


# ===== Program Utama (Testing) =====
if __name__ == "__main__":
    # 1. Membuat objek Perpustakaan, Buku, dan Anggota
    perpus = Perpustakaan("Perpustakaan Kampus")
    buku1 = Buku("Pemrograman Python", "Guido van Rossum")
    buku2 = Buku("Struktur Data", "Donald Knuth")
    anggota1 = Anggota("Budi")
    anggota2 = Anggota("Siti")

    # 2. Menambah buku ke perpustakaan
    perpus.tambah_buku(buku1)
    perpus.tambah_buku(buku2)

    # 3. Mendaftarkan anggota
    perpus.tambah_anggota(anggota1)
    perpus.tambah_anggota(anggota2)

    # 4. Meminjam buku oleh anggota
    perpus.pinjam_buku(anggota1, buku1)  # berhasil
    perpus.pinjam_buku(anggota2, buku1)  # gagal (sudah dipinjam)

    # 5. Menampilkan status peminjaman
    perpus.tampilkan_status_peminjaman()
