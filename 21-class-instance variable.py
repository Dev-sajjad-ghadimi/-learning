# ما امروز دوتا مبحث داریم
# که مورد متغییر ها هست
# اولی instance
# دومی class
# خوب ما تا الان  instance رو کار کردیم

# مثال

class car:
    def __init__(self, n, p):
        self.name = n
        self.price = p
        print(f"{self.name} costs {self.price}")


c1 = car('bmw', 100)
c2 = ('benz', 90)
# اینجا c1 و c2 متغییر instance هستن
# این تا اینجا

# خب توی instance ما نمیتونیم از طریق c1 به اطلاعات c2 دسترسی داشته باشیم ولی توی class برعکسه
# مثال


class bmw:
    wheel = 4

    def __init__(self2, n, p):
        self2.name = n
        self2.price = p
        print(f"{self2.name} {self2.wheel} تا لاستیک دارد")


a1 = bmw('bmw m3', 100)
# خروجی : bmw m3 4 تا لاستیک دارد


# ما برای اینکه بدونیم داخل یع ابجکت چه چیزی هایی وجود دارد از __dict__ استفاده میکنیم
print(a1.__dict__)
# خروجی : {'name': 'bmw m3', 'price': 100}
# اگه دقت کنیم اینجا بهمون wheel رو نشون ندارد
# ولی اگه ما کلاس رو دیکت کنیم بهمون نشون میده
print(bmw.__dict__)
# خروجی : {'__module__': '__main__', 'wheel': 4, '__init__'}

# خوب این تا اینجا
# خوب حالا مثال میزنیم یه بی ام و ام 3 اومده 5 تا لاستیک داره چی کار میکنی ؟
# از این روش استفاده میکنی


class benz:
    wheeel = 4

    def __init__(self3, n, p):
        self3.name = n
        self3.price = p

    def show_wheeel(self3):
        print(f"{self3.name} {self3.wheeel} تا لاستیک دارد")


b1 = benz('benz', 400)
b2 = benz('benz 2', 500)

b1.wheeel = 5

b1.show_wheeel()

# خروجی :
# benz 5 تا لاستیک دارد
# benz 2 4 تا لاستیک دارد


# حالا

print(b1.__dict__)
print(b2.__dict__)
print(benz.__dict__)
# خروجی ها
# اولی : {'name': 'benz', 'price': 400, 'wheeel': 5}
# دومی : {'name': 'benz 2', 'price': 500}
# سومی : <function benz.__init__ at 0x00000190D1E68EA0>, 'show_wheeel': <function benz.show_wheeel at 0x00000190D1E68F40>, '__dict__': <attribute '__dict__' of 'benz' objects>, '__weakref__': <attribute '__weakref__' of 'benz' objects>, '__doc__': None}

# اگه دقت کنید توی اولی wheeel هم اضافه کرد چرا؟
# چون ما از این خط کد اتفاتده کردیم :
# b1.wheeel = 5


# این از این
# قابلیت دیگش اینه که بهت میگه توی کلاست پن تا ابجکت داری
# مثال :
class lov:
    nums_abj = 0

    def __init__(self9, n, p):
        self9.name = n
        self9.price = p
        lov.nums_abj += 1


n1 = lov('benz', 400)
n2 = lov('benz 2', 500)
n3 = lov('pride', 100000000)
print(lov.nums_abj)
# خروجی : 3
