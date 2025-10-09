class Pelanggan:
    def __init__(self, nama, email):                 # Constructor kelas Pelanggan
        self.nama = nama                             # Nama pelanggan
        self.email = email                           # Email pelanggan
        self.keranjang = Keranjang()                 # Setiap pelanggan punya 1 keranjang
        self.riwayat_pesanan = []                    # Menyimpan riwayat pesanan

    def buat_pesanan(self):                          # Metode untuk membuat pesanan dari isi keranjang
        if not self.keranjang.daftar_item:           # Jika keranjang kosong
            print("Keranjang masih kosong!")
            return None

        pesanan = Pesanan(self)                      # Buat objek pesanan baru

        for item in self.keranjang.daftar_item:      # Tambahkan setiap item dari keranjang ke pesanan
            pesanan.tambah_item(item)

        self.riwayat_pesanan.append(pesanan)         # Simpan ke riwayat pesanan pelanggan
        self.keranjang.kosongkan()                   # Kosongkan keranjang setelah memesan

        print(f"\nPesanan untuk {self.nama} berhasil dibuat!")
        return pesanan                               # Kembalikan objek pesanan


class Produk:
    def __init__(self, nama, harga, stok):           # Constructor kelas Produk
        self.nama = nama                             # Nama produk
        self.harga = harga                           # Harga produk
        self.stok = stok                             # Jumlah stok tersedia


class Keranjang:
    def __init__(self):                              # Constructor kelas Keranjang
        self.daftar_item = []                        # List untuk menyimpan item yang ditambahkan

    def tambah_produk(self, produk, jumlah):         # Tambahkan produk ke dalam keranjang
        if produk.stok >= jumlah:                    # Periksa apakah stok cukup
            item = ItemPesanan(produk, jumlah)       # Buat objek item pesanan
            self.daftar_item.append(item)            # Masukkan ke daftar item keranjang
            print(f"{produk.nama} (x{jumlah}) ditambahkan ke keranjang.")
        else:
            print(f"Stok {produk.nama} tidak mencukupi!")  # Jika stok tidak cukup

    def kosongkan(self):                             # Kosongkan isi keranjang
        self.daftar_item = []


class Pesanan:
    def __init__(self, pelanggan):                   # Constructor kelas Pesanan
        self.pelanggan = pelanggan                   # Pemilik pesanan
        self.item_pesanan = []                       # Daftar item yang dipesan
        self.total = 0                               # Total harga awal = 0

    def tambah_item(self, item):                     # Tambahkan item ke dalam pesanan
        self.item_pesanan.append(item)
        self.total += item.subtotal()                # Tambahkan subtotal ke total pesanan

    def tampilkan_detail(self):                      # Menampilkan detail isi pesanan
        print(f"\n=== Detail Pesanan untuk {self.pelanggan.nama} ===")
        for item in self.item_pesanan:
            print(f"{item.produk.nama} x{item.jumlah} = Rp{item.subtotal()}")
        print(f"Total Harga: Rp{self.total}")


class ItemPesanan:
    def __init__(self, produk, jumlah):              # Constructor kelas ItemPesanan
        self.produk = produk                         # Produk yang dibeli
        self.jumlah = jumlah                         # Jumlah pembelian

    def subtotal(self):                              # Hitung subtotal harga
        return self.produk.harga * self.jumlah


# ===============================================
# PROGRAM UTAMA (TESTING)
# ===============================================
if __name__ == "__main__":
    # 1️⃣ Membuat beberapa produk
    produk1 = Produk("Laptop", 8000000, 5)           # Produk 1
    produk2 = Produk("Mouse", 150000, 10)            # Produk 2
    produk3 = Produk("Keyboard", 300000, 8)          # Produk 3

    # 2️⃣ Membuat pelanggan
    pelanggan1 = Pelanggan("Budi", "budi@example.com")

    # 3️⃣ Menambahkan produk ke keranjang pelanggan
    pelanggan1.keranjang.tambah_produk(produk1, 1)   # Tambah 1 laptop
    pelanggan1.keranjang.tambah_produk(produk2, 2)   # Tambah 2 mouse
    pelanggan1.keranjang.tambah_produk(produk3, 1)   # Tambah 1 keyboard

    # 4️⃣ Membuat pesanan dari keranjang
    pesanan_budi = pelanggan1.buat_pesanan()         # Buat pesanan

    # 5️⃣ Menampilkan detail pesanan dan total harga
    if pesanan_budi:
        pesanan_budi.tampilkan_detail()              # Tampilkan isi pesanan
