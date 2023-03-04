from PIL import Image, ImageDraw, ImageFont
import os

# Open Resource
barcode_folder = "F:/KULIAH UNS/Lab/POSI/idcard/barcode"
idcard_image = "F:/KULIAH UNS/Lab/POSI/idcard/desain_idcard.png"

# size, color, dan font text nama
text_size = 35
text_color = (255, 255, 255)  # putih
font = ImageFont.truetype("Poppins-Medium.ttf", text_size)

# Baca gambar idcard
idcard = Image.open(idcard_image)

# Loop untuk menambahkan barcode dan nama mhs pada idcard
for barcode_file in os.listdir(barcode_folder):
    # Ambil nama siswa dari nama file barcode
    nama_siswa = os.path.splitext(barcode_file)[0]
    nama_siswa = nama_siswa.upper()
    
    # Memperpendek nama siswa jika lebih dari 3 kata
    words = nama_siswa.split()
    if len(words) > 3:
        initials = ''.join([word[0] for word in words[3:]])
        words = words[:3] + [initials]
        nama_siswa = ' '.join(words)
        
    # Menambahkan titik pada inisial ke-1 hingga ke-n-1
    words = nama_siswa.split()
    if len(words) > 3:
        initials = words[-1]
        new_initials = ''
        for i in range(len(initials)-1):
            new_initials += initials[i] + '.'
        new_initials += initials[-1]
        words[-1] = new_initials
        nama_siswa = ' '.join(words)
    
    # Read barcode
    barcode_path = os.path.join(barcode_folder, barcode_file)
    barcode = Image.open(barcode_path)

    # Resize gambar barcode agar sesuai dengan ukuran yang diinginkan
    barcode = barcode.resize((330, 330))
    
    # Place barcode
    idcard.paste(barcode, (154, 192))
    
    # init variabel draw
    draw = ImageDraw.Draw(idcard)

    text_width, text_height = draw.textsize(nama_siswa, font=font)
    
    # Text position
    idcard_width, idcard_height = idcard.size
    text_position = ((idcard_width - text_width) / 2, 633)
    
    # Draw text name
    draw.text(text_position, nama_siswa, font=font, fill=text_color)
    
    # Save idcard
    idcard.save(f"F:/KULIAH UNS/Lab/POSI/idcard/output/{nama_siswa}_idcard.png")
    
    del barcode

    # Reset Process
    idcard = Image.open(idcard_image)