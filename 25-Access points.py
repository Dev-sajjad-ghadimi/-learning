# خوب مبحث امروز درمورده Access points هست

# Access points = publid > protected > private

class person:
    name = "sajjad"  # publid
    _age = 15  # protected
    __height = 160  # private


class male(person):
    pass


print(person.name)
# خروجی : sajjad


class male(person):
    def show(self):
        print(self._age)


a = male()
a.show()
# خروجی : 15


print(person._age)
# خروجی : 15

# print(person.__height)
# خروجی : ارور

# class male(person):
# def show(self):
# print(self.__height)

# a = male()
# a.show()

# خروجی : ارور

# روش چاپ  private

print(person._person__height)
# خروجی : 160

# به این روش میگن name mangling

# از این روش هم میشه استفاده کرد

p = person
print(p._person__height)
# خروجی : 160


class person:
    name = "sajjad"
    _age = 15
    __height = 160

    def __show(self):
        print("......")


p = person()

p._person__show()

# خروجی : ......
