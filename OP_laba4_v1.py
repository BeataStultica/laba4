image = open("test5.bmp",'rb')
image.seek(54)
t = image.read()
print(t)
print('--------------')
print(len(t))

def read_rows(path):
	coint = int(input("В скільки раз збільшити зображення?:"))
	image_file = open(path, "rb")
	bmp = image_file.read(54)
	size = int.from_bytes(bmp[2:6],byteorder = 'little')
	print(bmp)
	print(bmp[2:6])
	print("Size: ", size)
	print((size).to_bytes(4,byteorder = 'little'))
	width = int.from_bytes(bmp[18:22],byteorder = 'little')
	print(width)
	height = int.from_bytes(bmp[22:26],byteorder = 'little')
	print(height)
	bisize = int.from_bytes(bmp[34:38],byteorder = 'little')
	print(bisize)
	rows = b''
	row = b''
	pixel_index = 0
	new_head = bmp[0:2]
	print(new_head)
	new_head += (54 + height*width*4*(coint**2)).to_bytes(4,byteorder = 'little')
	print('-----')
	print('old')
	print(bmp[2:6])
	print(size)
	print('new')
	
	new_head += bmp[6:18]
	new_head += (width*coint).to_bytes(4,byteorder = 'little')
	new_head += (height*coint).to_bytes(4,byteorder = 'little')

	new_head += bmp[26:34]
	new_head += (54 + height*width*3*(coint**2)).to_bytes(4,byteorder = 'little')
	new_head += bmp[38::]

	new_image = open("new_bmp.bmp", 'wb')
	new_image.write(new_head)
a = read_rows('test5.bmp')
