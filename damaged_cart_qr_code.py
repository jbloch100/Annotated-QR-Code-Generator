from PIL import Image, ImageDraw, ImageFont
import qrcode

def generate_qrcode():
	#Generate QR Code
	qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
	qr.add_data("https://jbloch100.github.io/Dragonfly_Comment/")
	qr.make(fit=True)
	qr_img=qr.make_image(fill='black', back_color='white').convert('RGB')

	#Define the font size and path
	font_size = 20
	font_path = "arial.ttf"
	font = ImageFont.truetype(font_path, font_size)
	text = "Damaged Cart QR Code"

	#Usa a dummy image to calculate text size with 'textbbox'
	dummy_img = Image.new('RGB', (1,1))
	draw = ImageDraw.Draw(dummy_img)
	left, top, right, bottom = draw.textbbox((0,0), text, font=font)
	text_width = right - left
	text_height = bottom - top

	#Create new image with space for text
	new_img_height = qr_img.height + text_height + 10 #Extra space for padding
	new_img = Image.new('RGB', (qr_img.width, new_img_height), 'white')

	#Calculate x coordinate to center the text
	text_x = (new_img.width - text_width) / 2

	#Draw the barcode text on the new image
	draw = ImageDraw.Draw(new_img)
	draw.text((text_x, 5), text, fill='red', font=font)

	# Paste the QR code below the text
	new_img.paste(qr_img, (0, text_height + 10))

	#Save the image
	filename = "Damaged_Cart_QRCode_QR.png"
	new_img.save(filename)
	print(f"QR code with barcode saved to {filename}.")

generate_qrcode()