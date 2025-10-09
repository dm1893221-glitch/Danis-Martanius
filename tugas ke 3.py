# KELAS PERUSAHAAN
class Perusahaan:
    def __init__(self, nama):  # Konstruktor untuk inisialisasi data perusahaan
        self.nama = nama                  # Nama perusahaan
        self.proyek_list = []             # Daftar proyek yang dimiliki perusahaan
        self.tim_list = []                # Daftar tim yang ada di perusahaan

    # Membuat proyek baru
    def buat_proyek(self, nama_proyek, deskripsi):
        proyek = Proyek(nama_proyek, deskripsi)  # Membuat objek Proyek
        self.proyek_list.append(proyek)           # Menyimpan ke daftar proyek
        print(f"Proyek '{nama_proyek}' berhasil dibuat.")
        return proyek                             # Mengembalikan objek proyek

    # Membuat tim baru
    def buat_tim(self, nama_tim):
        tim = Tim(nama_tim)                # Membuat objek Tim
        self.tim_list.append(tim)          # Menyimpan ke daftar tim
        print(f"Tim '{nama_tim}' berhasil dibuat.")
        return tim                         # Mengembalikan objek tim

# KELAS PROYEK
class Proyek:
    def __init__(self, nama, deskripsi):
        self.nama = nama                   # Nama proyek
        self.deskripsi = deskripsi         # Deskripsi singkat proyek
        self.tugas_list = []               # Daftar tugas dalam proyek

    # Menambahkan tugas ke proyek
    def tambah_tugas(self, deskripsi_tugas):
        tugas = Tugas(deskripsi_tugas)     # Membuat objek Tugas baru
        self.tugas_list.append(tugas)      # Menambahkan ke daftar tugas
        print(f"Tugas '{deskripsi_tugas}' ditambahkan ke proyek '{self.nama}'.")
        return tugas                       # Mengembalikan objek tugas

    # Menampilkan status seluruh tugas dalam proyek
    def tampilkan_status(self):
        print(f"\n📋 Status Proyek: {self.nama}")
        for tugas in self.tugas_list:
            tugas.status()                 # Memanggil method status() pada setiap tugas

# KELAS TIM
class Tim:
    def __init__(self, nama):
        self.nama = nama                   # Nama tim
        self.developer_list = []           # Daftar developer dalam tim

    # Menambahkan developer ke dalam tim
    def tambah_developer(self, developer):
        self.developer_list.append(developer)
        print(f"Developer '{developer.nama}' ditambahkan ke tim '{self.nama}'.")

# KELAS DEVELOPER
class Developer:
    def __init__(self, nama, keahlian):
        self.nama = nama                   # Nama developer
        self.keahlian = keahlian           # Bidang keahlian (contoh: Python, Java, dll.)


# KELAS TUGAS
class Tugas:
    def __init__(self, deskripsi):
        self.deskripsi = deskripsi         # Deskripsi tugas yang harus dikerjakan
        self.developer = None              # Developer yang ditugaskan (default = None)

    # Menugaskan tugas ke developer tertentu
    def tugaskan_ke(self, developer):
        self.developer = developer
        print(f"Tugas '{self.deskripsi}' ditugaskan ke {developer.nama}.")

    # Menampilkan status tugas (apakah sudah ditugaskan atau belum)
    def status(self):
        if self.developer:
            print(f"- {self.deskripsi} → Dikerjakan oleh {self.developer.nama} ({self.developer.keahlian})")
        else:
            print(f"- {self.deskripsi} → Belum ada developer yang ditugaskan")


# BAGIAN TESTING PROGRAM

# 1️⃣ Membuat perusahaan baru
perusahaan = Perusahaan("Tech Crop")

# 2️⃣ Membuat tim baru dan menambah developer ke dalam tim
tim1 = perusahaan.buat_tim("Tim Backend")
dev1 = Developer("Andi", "Python")   # Developer pertama
dev2 = Developer("Budi", "Java")     # Developer kedua
tim1.tambah_developer(dev1)
tim1.tambah_developer(dev2)

# 3️⃣ Membuat proyek baru dan menambahkan beberapa tugas ke dalamnya
proyek1 = perusahaan.buat_proyek("Sistem E-Commerce", "Membangun platform belanja online")
tugas1 = proyek1.tambah_tugas("Buat API Login")
tugas2 = proyek1.tambah_tugas("Integrasi Database")
tugas3 = proyek1.tambah_tugas("Fitur Pembayaran")

# 4️⃣ Menugaskan beberapa tugas ke developer
tugas1.tugaskan_ke(dev1)   # Tugas 1 dikerjakan Andi
tugas2.tugaskan_ke(dev2)   # Tugas 2 dikerjakan Budi
# Tugas 3 belum ditugaskan ke siapa pun

# 5️⃣ Menampilkan status proyek dan semua tugas
proyek1.tampilkan_status()
