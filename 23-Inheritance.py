# مبحث امروز در مورده inheritance

# به این کد دقت کنید


class car:
    wheel = 4

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'{self.name}ماشین\موتور خوبی است ')


class motor:
    wheel = 2

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'{self.name}موتور\ماشین خوبی است ')

# اینجا اجزای تشکیل دهنده کلاس موتور ب کلاس ماشین تکراری و شبیه هم هممستن و این  خوبی توی برنامه نویسی


# بجاش از این روش استفاده میکنیم

class motor2(car):
    wheel = 2

    # تمام


a = motor2('cb1300')

a.show()
# خروجی :
# cb1300ماشین\موتور خوبی است

print(a.wheel)
# خروجی : 2

help(a)
# class motor2(car)
# |  motor2(name)

# |  Method resolution order:
# |      motor2
# |      car
# |      builtins.object
# |
# |  Data and other attributes defined here:
# |
# |  wheel = 2
# |
# |  ----------------------------------------------------------------------
# |  Methods inherited from car:
# |
# |  __init__(self, name)
# |      Initialize self.  See help(type(self)) for accurate signature.
# |
# |  show(self)
# |
# |  ----------------------------------------------------------------------
# |  Data descriptors inherited from car:
# |
# |  __dict__
# |      dictionary for instance variables
# |
# |  __weakref__
# |      list of weak references to the object

# چند تا توضیح خوب در مورده کدمون


# خوببب

class car:
    wheel = 4

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'{self.name}ماشین\موتور خوبی است ')


class motor(car):
    wheel = 2


a = motor('honda')

# خوب اینجا من دوست دارم show رو چاپ نکنه و جمله دیگه چاپ کنه
# یه فانکشن دیگه تو کلاس موتور مینویسی


class motor(car):
    wheel = 2

    def kk(self):
        print(f'{self.name}موتور خوبی است')


a = motor('honda')

a.kk()
# خروجی : hondaموتور خوبی است

# میشه دو تا باهم هم چاپ کنی


class motor(car):
    wheel = 2

    def kk(self):
        print(f'{self.name}موتور خوبی است')
        print(f'{self.name}ماشین\موتور خوبی است ')


c = motor('honda')

c.kk()

# خروجی :
# hondaموتور خوبی است
# hondaماشین\موتور خوبی است


# اقا من دوس دارم هر هم فانکشن show داخل کلاس ماشین رو چاپ کنه هم فانکشن kk داخل کلاس موتور
# چیکار کنم؟
# از این روش استفاده کن

class motor(car):
    wheel = 2

    def kk(self):
        super().show()
        print(f'{self.name}موتور خوبی است')


r = motor('honda')

r.kk()
# خروجی :
# hondaماشین\موتور خوبی است
# hondaموتور خوبی است


# خوب ما توی کدمون میخاییم به اون کسی که موتور داریه بپرسیم ایا کلاه ایمنی داره یا نه؟

class car:
    wheel = 4

    def __init__(self, name, کلاه_ایمنی):
        self.name = name
        self.کلاه_ایمنی = کلاه_ایمنی

    def show(self):
        print(f'{self.name}ماشین\موتور خوبی است ')


class motor(car):
    wheel = 2


i = motor('cb', 'no')


# این روش خوبه یعنی به ما خروجی میده ولی از لحاظ منطقی درست نیست چون ماشین سواری نیاز به کلاه ایمنی نداره پس چی کار میکنی؟
# اجزای داخل کلاس ماشین رو کپی میکنی و داخل کلاس موتور پست میکنی


class car:
    wheel = 4

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'{self.name}ماشین\موتور خوبی است ')


class motor(car):
    wheel = 2

    def __init__(self, name, کلاه):
        self.name = name
        self.کلاه = کلاه


i = motor('cb', 'no')


i.show()

# خوب الان کدمون از لحاظ منطقی درسته


# روش ساده و بهتر دیگه ای هم داریم
class car:  # parent \ super class
    wheel = 4

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'{self.name}ماشین\موتور خوبی است ')


class motor(car):  # child \ subclass
    wheel = 2

    def __init__(self, name, کلاه):
        super().__init__(name)
        self.کلاه = کلاه


u = motor('cb', 'no')


u.show()
