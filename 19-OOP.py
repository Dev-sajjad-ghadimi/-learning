#خوب مبحث امروز در مورد OPP هستش

#یا همون برنامه نویسی شی گرا

#مثال


class mashin:
    pass

a = mashin()
b = mashin()

a.name = 'bmw'
b.name = 'benz'

#میتونی بجای name  هر چیزی دلت بخواد میتونی بنویسی

a.gheimat = 140000
b.gheimat = 100000

#ال دبت میخاد میتونی بهش ویژگی بدی

#همین به این میگن برنامه نویسی شی گرا

#ولی ولی هنوزن ادامه دارهع

#خوب مثلا میخام قیمت بی ام و رو ببینم از این روش استفاده میکنم

print(a.gheimat)
#خروجی : 140000

#همینطوری برای بقیه ویژگی ها
print(b.name)
#خروجی : benz




#حالت fstring  هم میشه
#مثال

print(f'{a.name} costs {a.gheimat}')
print(f'{b.name} costs {b.gheimat}')
#خروجی :
#bmw costs 140000
#benz costs 100000


#مثاله دیگه ای از برنامه نویسی شی گرا


class person:
    pass

a = person()
b = person()

a.name = 'sajjad'
b.name = 'amir'

a.height = 155
b.height = 180

