#امروز در مورده متوده

#متود همون فانکشنه ولی داخل کلاس قرار گرفته

#چرا ما فانکشن هامون رو داخل کلاس قراریم ؟
#برای اینکه کدمون تمیز تر باشه

#مثال 

#class car:
    #def show():
        #print("this is metgod...")

#c1 = car()
#c1.show()
#همین
#کد بالایی  ارور مید چون ما داخل show هیچ مقداری ننوشتیم




#کد درستش



class car:
    def show(self):
        print("this is metgod...")

c1 = car()
c1.show()
#خروجی : this is metgod...


class car:
    def show(self):
        print("this is metgod...")

c1 = car()
c2 = car()

c1.show()
c2.show()
#خروجی : 
#this is metgod...
#this is metgod...

#همیشه پیشنهاد میشه در جای پرانتز اسم فانکشن self نوشته شود

#این متود show رو خودم ساختم
#بعضی متود های اماده رو خود پایتون ساخته تا کارمون رو راحت  ترکنه


#مثال


class lov:
    def __init__(self2):
        print("ammmmmmmmmmmmmmmmm")

a1 = lov()
a2 = lov()
#خروجی : 
#ammmmmmmmmmmmmmmmm
#ammmmmmmmmmmmmmmmm

#هر چه بیشتر ابجکت بسازی بیشتر برات چاپ میکنه

#کارش چیه ؟ کارش اینه
#مثال


class car2:
    def __init__(self3 , n , p):
        self3.name = n
        self3.price = p

    def jak(self4):
        print(f'{self4.name} costs {self4.price}')

b1 = car2('bmw', 14000)
b2 = car2('lambirgini' , 1000000)

print(b1.price)
#خروجی : 14000

print(f'{b1.name} costs {b1.price}')
#خروجی : bmw costs 14000

print(f'{b2.name} costs {b2.price}')
#خروجی : lambirgini costs 1000000

#میشه این دو خط کد رو هم بزاریب اداخل فانکشن

b1.jak()
#خروجی : bmw costs 14000

b2.jak()
#خروجی : lambirgini costs 1000000

#راستی میتونی متود jak  رو پاک کنی و مستقیما ببری داخل متود __init__

