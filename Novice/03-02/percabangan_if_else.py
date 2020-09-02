#	Percabangan IF, ELSE dan ELIF (Statements)

	#	Perintah 'IF'	--> If bisa digunakan sebagai perintah kondisi awal.

a = 33
b = 200

if b > a:
	print('Selamat Anda Menang !!!')
	print('')


	#	Perintah 'ELSE' --> Else tidak bisa diberi kondisi baru

a = 33
b = 200
if b < a:
	print('Ternyata Kamu Pecundang ')
else:
	print('Selamat Anda Menang !!!')
	print('')


	#	Perintah 'ELIF' --> Elif bisa diberi kondisi baru, tetapi tidak bisa digunakan untuk membuat kondisi awal

a = 33
b = 200

if b < a:
	print('Anda Sedang Rusak ')
elif b > a:
	print('Anda Sedang Sehat')


# 	NOTE : Jangan lupa 'INDENTATION' pada sebuah kode di python.