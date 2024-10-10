import random, time, os

class Kartun:
    # Encapsulation: atribut `kecepatan`, `namaKarakter`, `motivasi`, dan `posisi` disembunyikan dari akses luar.
    def __init__(self, kecepatan, namaKarakter, ikon):
        self.kecepatan = kecepatan
        self.namaKarakter = namaKarakter
        self.motivasi = 0
        self.posisi = 99
        self.icon = ikon

    def bergerak(self):
        # Abstraction: hanya memuat metode penting untuk memindahkan karakter tanpa memperlihatkan detail internal.
        self.motivasi = random.randint(0, 2)
        self.posisi -= self.kecepatan * self.motivasi


class Dora(Kartun):
    # Inheritance: `Dora` mewarisi atribut dan metode dari class `Kartun`.
    # Polymorphism: `Dora` memiliki atribut unik yang membedakan dari karakter lain.
    def __init__(self):
        super().__init__(2, "Dora", "🧳")  # Kecepatan lebih tinggi, menggunakan ikon ransel.


class SpongeBob(Kartun):
    def __init__(self):
        super().__init__(1, "SpongeBob", "🍍")  # SpongeBob berjalan lebih lambat, ikon nanas.


class Barbie(Kartun):
    def __init__(self):
        super().__init__(1, "Barbie", "👗")  # Barbie bergerak dengan kecepatan biasa.


class Masha(Kartun):
    def __init__(self):
        super().__init__(2, "Masha", "🐻")  # Masha lebih cepat, ditemani beruangnya.


class Shinchan(Kartun):
    def __init__(self):
        super().__init__(1, "Shinchan", "👶")  # Shinchan berjalan dengan kecepatan biasa.


class ManajerGame:
    # Encapsulation: `balapanSelesai` dan `pemenang` tidak bisa diakses langsung dari luar.
    def __init__(self):
        self.balapanSelesai = False
        self.pemenang = None
        self.karakter = []

        # Abstraction: menentukan siapa saja karakter yang akan ikut balapan, tanpa memperlihatkan detail cara karakternya dibuat.
        self.karakter.append(Dora())
        self.karakter.append(SpongeBob())
        self.karakter.append(Barbie())
        self.karakter.append(Masha())
        self.karakter.append(Shinchan())

        self.panjangLintasan = 100
        self.lintasan = 100 * "_"

    def balapan(self):
        # Polymorphism: metode `bergerak()` dijalankan oleh setiap objek kartun, baik itu `Dora`, `SpongeBob`, dll.
        while(not self.balapanSelesai):
            for karakter in self.karakter:
                karakter.bergerak()
                if(karakter.posisi <= 0):
                    self.balapanSelesai = True
                    self.pemenang = karakter
                lintasanKarakter = list(self.lintasan)
                lintasanKarakter[karakter.posisi] = karakter.icon
                lintasanKarakter = karakter.namaKarakter + " " + "".join(lintasanKarakter)
                print(lintasanKarakter)
            time.sleep(0.1)
            os.system("cls")

    def mulai(self):
        # Abstraction: memulai game dan menampilkan lintasan tanpa memperlihatkan detail cara karakter bergerak.
        for karakter in self.karakter:
            lintasanKarakter = list(self.lintasan)
            lintasanKarakter[99] = karakter.icon
            lintasanKarakter = "".join(lintasanKarakter)
            print(karakter.namaKarakter + " " + lintasanKarakter)

        self.balapan()
        
        print("Pemenang: " + self.pemenang.namaKarakter)


# Memulai permainan
game = ManajerGame()
game.mulai()
