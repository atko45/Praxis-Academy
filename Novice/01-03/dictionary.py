#DICTIONARY

	#Membuat Struktur data
tel = {'jack': 100, 'sape': 200} #Cara membuat struktur data yang ada pada dictionary

	#Menambahkan data
tel['guido'] = 300 #Cara 'menambahkan' sebuah data kedalam struktur data yang sudah kita buat sebelumnya
print(tel)

print('')

	#Memanggil data
print(tel['jack']) #Cara memanggil data yang dibutuhkan

print('')

	#Menghapus Data
del tel['sape'] #Quary untuk menghapus data yang ada pada struktur data 'tel'

tel['irv'] = 400 #Membuat data baru didalam struktur data 'tel'
print(tel)

print('')

	#Memanggil List Data
print(list(tel)) #Cara memanggil list 'key' pada data 'tel'

print('')

	#Mengurutkan data sesuai value
print(sorted(tel)) #Cara memanggil data sesuai abjad dan value

print('')

	#Memverifikasi lokasi data
print('guido' in tel) #Cara mengecek data apakah benar berada didalam struktur data 'tel' atau tidaks

print('')

print('guido' not in tel)

print('')

#BELUM PAHAM

	#Memperlajari 'Dict'
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

print('')

print({x: x**2 for x in (2, 4, 6)})

print('')

print(dict(sape=4139, guido=4127, jack=4098))