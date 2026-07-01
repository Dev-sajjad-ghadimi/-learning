# مبحث امروز درمورده property  هست

class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f'{fname}_{lname}@email.com'

    def full_name(self):
        return f'{self.fname} {self.lname}'


a = person('sajjad', 'ghadimi')

print(a.fname)
print(a.lname)
print(a.email)
print(a.full_name())

# خروجی :
# sajjad
# ghadimi
# sajjad_ghadimi@email.com
# sajjad ghadimi

# خوووبببببببببببببببببببب

print("هههه")


class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f'{fname}_{lname}@email.com'

    def full_name(self):
        return f'{self.fname} {self.lname}'


a = person('sajjad', 'ghadimi')

print(a.fname)
a.fname = 'mohmam'
print(a.lname)
print(a.email)
print(a.full_name())

# خروجی:
# sajjad
# ghadimi
# sajjad_ghadimi@email.com
# mohmam ghadimi

# همینجوری که میببنین اسم توی جیمیل تغییر نکرد و همون سحاد موند پس چی کار  کنیم ؟
# روش درست


class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def full_name(self):
        return f'{self.fname} {self.lname}'

    @property
    def email(self):
        return f'{self.fname}_{self.lname}@email.com'


a = person('sajjad', 'ghadimi')
a.fname = 'ali'
print(a.fname)
print(a.lname)
print(a.email)
print(a.full_name())
# خروجی :
# ali
# ghadimi
# ali_ghadimi@email.com
# ali ghadimi

# چون ما بالای فانکشن ایمل نوشتیم @property لازم موقع صدا زدن فانکشن از () استفاده کنیم

# مثال دیگه


class hu:
    def __init__(self, name):
        self.name = name

    @property
    def p(self):
        return f'hi {self.name}'


a = hu('sajjad')

print(a.p)
# خروجی : hi sajjad
# به همین اسونی
