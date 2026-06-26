# خوب مبحث امروز در مورده class method ها هست

# method > 1.instance , 2.class , 3static

import datetime


class person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def show(self):
        print(f'{self.name} is {self.height}')


a1 = person('sajjad', 160)

a1.show()
# خروجی : sajjad is 160

# اینجا فانکشن show یه instance هست
# پس ما با instance اشنا شدیم


# خب حالا در مورده class
# من یه مثال بزنم


class person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f'{self.name} is {self.height} and {self.age} years old')

    @classmethod
    def from_birth(cls, name, height, age):
        return cls(name, height, datetime.datetime.now().year - age)


a1 = person.from_birth('sajjad', 160, 1990)

a1.show()
# خروجی : sajjad is 160 and 36 years old

# خوی اینجا ما برای ساخت یه فانکشن کلاس از @classmethod استفاده کردیم

# این هم از  کلاس متود

# خب الان در مورده static متد ها هستش

# مثال


class person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f'{self.name} is {self.height} and {self.age} years old')

    @classmethod
    def from_birth(cls, name, height, age):
        return cls(name, height, datetime.datetime.now().year - age)


def is_adult(age):
    if age > 18:
        print('yes')
    else:
        print('no')


is_adult(17)
# خروجی : no
is_adult(30)
# خروجی : yes

# خب الان این شرطمون بیرون از کدمون است
# پس چی کار کنیم ؟
# از این روش استفاده کن


class person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):  # instance متد
        print(f'{self.name} is {self.height} and {self.age} years old')

    @classmethod  # class متد
    def from_birth(cls, name, height, age):
        return cls(name, height, datetime.datetime.now().year - age)

    @staticmethod  # static متد
    def is_adult(age):
        if age > 18:
            print('yes')
        else:
            print('no')


person.is_adult(23)
# خروجی : yes
