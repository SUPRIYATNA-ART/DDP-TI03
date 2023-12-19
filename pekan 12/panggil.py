from Gempa import *

Gempa1 = Gempa("Banten", 1.2)
Gempa2 = Gempa("palu", 6.1)
Gempa3 = Gempa("Cianjur", 5.6)
Gempa4 = Gempa("Jayapura", 3.3)
Gempa5 = Gempa("Garut", 4.0)

# Memanggil fungsi dampak untuk setiap objek
hasil_dampak1 = Gempa1.dampak()
hasil_dampak2 = Gempa2.dampak()
hasil_dampak3 = Gempa3.dampak()
hasil_dampak4 = Gempa4.dampak()
hasil_dampak5 = Gempa5.dampak()

# Menampilkan hasil dampak
print(hasil_dampak1)
print(hasil_dampak2)
print(hasil_dampak3)
print(hasil_dampak4)
print(hasil_dampak5)