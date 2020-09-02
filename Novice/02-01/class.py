#	SIMPLEST CLASS
print('')



class Person:
    pass  # An empty block
    #pass

p = Person()
print(p)


print('')



#	METHODS = Kemampuan, tugas atau aktifitas yang dapat dilakukan

class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()


print('')



#	INIT

class Person:
    def __init__(self, names):
        self.name = names

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()