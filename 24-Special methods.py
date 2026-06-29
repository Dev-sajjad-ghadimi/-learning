# خوب مبحث امروز در مورده Special methods

# الان  __init__ یه نوع Special method هست
# به متد های اینحوری __init__ که اول و اخرشون دوتا __ میگن dunder method

# اینجا میخوایم با دو نوع Special method اشنا شویم

# خب

class car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f'i have {self.name}')


a = car('pride', 100)
b = car('benz', 100000)

print(a)
# خروجی : <__main__.car object at 0x00000252FDDF1D60>
# این <__main__.car object at 0x00000252FDDF1D60> محل ذخیره ابجکت هست اگه بخوایی اطلاعات ابجکت چاپ بشه از این روش استفاده میکنیم
# یه Special درست قرار میدیم به نام __str__


class car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f'i have {self.name}')

    def __str__(self):
        return f'{self.name} - {self.price}'


a = car('pride', 100)
b = car('benz', 100000)

print(a)
# خروجی: pride - 100
print(b)
# خروجی : benz - 100000


# بعدی برای جمع کردنه
# برای جمع کردن دوتا ابجکته

# خوب ما نمیتونیم برای جمع کرن دوتا ابجکت از این روش استفاده کنیم
# print(a + b)
# قطعا ارور میده
# وما از این روش استفاده میکنیم


# مثلا میخوایم قیمت هارو حمع کنیم

class car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f'i have {self.name}')

    def __add__(self, other):
        return self.price + other.price
# self.price = a
# other.price = b


a = car('pride', 100)
b = car('benz', 100000)

print(a + b)
# خروجی : 100100

# خوب ما قبلا len رو یاد گرفتیم
# اگه بخواییم len یک ابجکت رو به این روش بگیریم ارور میده
# print(len(a))
# خروجی: ارور

# پس از این روش استفاده میکنیم


class car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f'i have {self.name}')

    def __len__(self):
        return len(self.name)


a = car('pride', 100)
b = car('benz', 100000)

print(len(a))
# خروجی : 5

print(len(b))
# خروجی: 4
