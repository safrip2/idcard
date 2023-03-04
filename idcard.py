from PIL import Image
import os
# Load the ID card design
idcard = Image.open("desain_idcard.png")

# Get the barcode filenames
import os
barcode_folder = "F:/KULIAH UNS/Lab/POSI/idcard/barcode"
barcode_filenames = os.listdir(barcode_folder)

# Loop through the barcode filenames
for filename in barcode_filenames:
    if filename.endswith(".png"):
        # Load the barcode image
        barcode = Image.open(os.path.join(barcode_folder, filename))
        
        # Resize the barcode image to fit on the ID card
        barcode = barcode.resize((200, 100))
        
        # Paste the barcode onto the ID card
        idcard.paste(barcode, (300, 300)) # Ganti koordinat x dan y sesuai dengan desain ID cardmu
        
        # Save the new ID card with barcode
        idcard.save("idcard_"+filename)
