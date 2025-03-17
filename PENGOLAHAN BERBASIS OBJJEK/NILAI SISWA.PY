class Siswa:
    def __init__(self, nama, nis):
        self.nama = nama
        self.nis = nis
        self.nilai_ujian = []
    
    def tambah_nilai(self, nilai):
        self.nilai_ujian.append(nilai)
    
    def hitung_rata_rata(self):
        if len(self.nilai_ujian) == 0:
            return 0
        return sum(self.nilai_ujian) / len(self.nilai_ujian)
    
    def tampilkan_info(self):
        rata_rata = self.hitung_rata_rata()
        print(f"Nama: {self.nama}, NIS: {self.nis}, Nilai Ujian: {self.nilai_ujian}, Rata-rata: {rata_rata:.1f}")

# Contoh penggunaan
siswa1 = Siswa("Andi", "123456789")
siswa1.tambah_nilai(80)
siswa1.tambah_nilai(90)
siswa1.tambah_nilai(85)

siswa2 = Siswa("Budi", "987654321")
siswa2.tambah_nilai(70)
siswa2.tambah_nilai(75)
siswa2.tambah_nilai(80)

siswa3 = Siswa("DIMAS", "4567891112")
siswa3.tambah_nilai(77)
siswa3.tambah_nilai(90)
siswa3.tambah_nilai(80)

print("Informasi Siswa")
siswa1.tampilkan_info()
siswa2.tampilkan_info()
siswa3.tampilkan_info()

# NAMA= DIAHIRO CIPTANING NOVENDRIA
# NIM= 23.01.4958