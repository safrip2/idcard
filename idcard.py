from PIL import Image
import os

# Buka gambar desain id card
desain = Image.open("desain_idcard.png")

# Buka gambar barcode
barcode = Image.open("barcode_siswa1.png")

# Tentukan lokasi di mana barcode akan ditempelkan pada desain
x = 100
y = 200

# Tempelkan barcode pada desain
desain.paste(barcode, (x, y))

# Simpan gambar hasil penggabungan barcode dan desain
desain.save("idcard_siswa1.png")
