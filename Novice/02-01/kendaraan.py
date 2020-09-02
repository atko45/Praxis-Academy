# 	Properti : Ciri-ciri atau hal-hal yang dimiliki
# 	Method = Kemampuan, tugas atau aktifitas yang dapat dilakukan
			# Method Self = Perintah yang digunakan untuk mengakses semua yang ada di dalam 'Class'
			# Method Init = Perintah yang digunakan untuk menyiapkan object sebelum digunakan, diajalankan ketika membuat objectnya

#	CLASS
class Kendaraan:
	
#Properti = nilai awal									OBJECT ORIENTED PROGRAMING

	kecepatan = 0
	cc = 0

#Constructor

	def __init__(self):
		self.roda = 0


#Method

	def nyala(self):  #### Method 
		print('brum brum')

	def maju(self):
		if self.roda > 0:
			self.kecepatan = self.kecepatan + 10

	def mundur(self):
		pass

print('')

#Inheritence

class Motor(Kendaraan):
	pass


m1	= Motor()
m1.nyala()
m1.roda = 3
print(m1.roda)
print(Kendaraan)

print('')