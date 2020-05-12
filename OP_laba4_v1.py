def raise_size(path,coint,new_path):
	image_file = open(path, "rb")
	bmp = image_file.read(54)
	size = int.from_bytes(bmp[2:6],byteorder = 'little')
	width = int.from_bytes(bmp[18:22],byteorder = 'little')
	height = int.from_bytes(bmp[22:26],byteorder = 'little')
	bisize = int.from_bytes(bmp[34:38],byteorder = 'little')
	cointer1 = 0
	cointer2 = 0
	width1 = width
	width2 = width*coint*3
	while width2%4 != 0:
		cointer1 += 1
		width2 +=1
	while (width1*3)%4 != 0:
		width1 -=1
		cointer2 +=1
	new_head = bmp[0:2]
	new_head += (54 + height*width*4*(coint**2) +height*cointer1).to_bytes(4,byteorder = 'little')
	new_head += bmp[6:18]
	new_head += (width*coint).to_bytes(4,byteorder = 'little')
	new_head += (height*coint).to_bytes(4,byteorder = 'little')
	new_head += bmp[26:34]
	new_head += (54 + height*width*4*(coint**2)).to_bytes(4,byteorder = 'little')
	new_head += bmp[38::]
	copy_pixel(width,cointer1,cointer2,image_file,new_head,coint,new_path)
def copy_pixel(width,cointer1,cointer2,image_file,new_head,coint,new_path):
	new_image = open(new_path, 'wb')
	new_image.write(new_head)
	pixel_index = 0
	row = b''
	while True:
		if pixel_index == width:
			pixel_index = 0
			for q in range(cointer2):
				image_file.read(1)
			for i in range(coint):
				new_image.write(row + b'\x00'*cointer1)
			row = b''
		pixel_index += 1

		r = image_file.read(1)
		g = image_file.read(1)
		b = image_file.read(1)

		if len(r) == 0:
			break

		if len(g) == 0:
			break

		if len(b) == 0:
			break
		for i in range(coint):
			row += r + g + b
	new_image.close()
	image_file.close()
def main():
	path = input("Введіть шлях до файлу який слід збільшити: ")
	coint = int(input("В скільки раз збільшити зображення?:"))
	new_path = input("Записати результат в : ")
	if len(new_path) == 0:
		new_path = 'new_bmp.bmp'
	if len(path) == 0:
		path = 'bmp.bmp'
	raise_size(path,coint,new_path)
main()
