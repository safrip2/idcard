from PIL import Image, ImageDraw
import os 
# Baca desain idcard dari file
img = Image.open('desain_idcard.png')

# Loop untuk setiap siswa
for nama_file in ['amanda.png', 'ryan.png', 'arab.png']:
    # Baca barcode dari file
    barcode_img = Image.open(nama_file)

    # Tentukan koordinat x dan y untuk menempelkan barcode pada desain idcard
    x = 100
    y = 200

    # Tempelkan barcode pada desain idcard
    img.paste(barcode_img, (x, y))

    # Simpan hasilnya dengan nama file yang sesuai
    nama_idcard_file = nama_file.split('.')[0] + '_idcard.png'
    img.save(nama_idcard_file)
