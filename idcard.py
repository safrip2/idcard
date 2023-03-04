from PIL import Image, ImageDraw, ImageFont
import os

# Open Resource
barcode_folder = "F:/KULIAH UNS/Lab/POSI/idcard/barcode"
idcard_image = "F:/KULIAH UNS/Lab/POSI/idcard/desain_idcard.png"

# Ukuran dan letak teks nama siswa pada idcard
text_size = 50
text_color = (255, 255, 255)  # warna teks (putih)
text_position = (50, 50)  # koordinat letak teks (x, y)

# Buat objek font untuk menulis teks
font = ImageFont.truetype("Poppins-Medium.ttf", text_size)

# Baca gambar idcard
idcard = Image.open(idcard_image)

# Loop untuk menambahkan barcode dan nama siswa pada idcard
for barcode_file in os.listdir(barcode_folder):
    # Ambil nama siswa dari nama file barcode
    nama_siswa = os.path.splitext(barcode_file)[0]
    
    # Baca gambar barcode
    barcode_path = os.path.join(barcode_folder, barcode_file)
    barcode = Image.open(barcode_path)

    # Resize gambar barcode agar sesuai dengan ukuran yang diinginkan
    barcode = barcode.resize((200, 100))
    
    # Letakkan gambar barcode pada gambar idcard
    idcard.paste(barcode, (100, 200))
    
    # Buat objek draw untuk menulis teks pada gambar idcard
    draw = ImageDraw.Draw(idcard)
    
    # Tulis nama siswa pada gambar idcard
    draw.text(text_position, nama_siswa, font=font, fill=text_color)
    
    # Simpan gambar idcard yang sudah ditambahkan barcode dan nama siswa
    idcard.save(f"{nama_siswa}_idcard.png")
    
    # Hapus gambar barcode dari memori agar tidak menghabiskan memori
    del barcode
