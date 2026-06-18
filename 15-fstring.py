#fstring مبحث جدید در مورده 
#خوب ما نمیتونیم هیچ وقت یه استرینگ رو با اینتییجر جمع کنیم
a = "ali"
b = 12
#print(a + b)
#خروجیش ارور میده

#خب چی کار میکنیم از کلمه کلیدی str استفاده میکنیم
#که میشه دو جا بزاری 
#مثال

e = "sajjad"
r = str(15)
print(e + r)
#خروجی: sajjad15

#روش بعدی

s = "mohamad"
f = 18
print(s + str(f))
#خروجی : mohamad18



#خوب یه روش دیگه بهتر هم داریم به نام  fstring

#روشش

name = "sajad"
age = 15
print('{name} is {age} years old.')
#خروجی : {name} is {age} years old.

#برای اینکه اسم و سن چاپ بشه باید  قبل کوتیشن یه f کوچیک یا بزرگ بزاری

namee = "hosein"
agee = 30
print(f"{namee} is {agee} years old.")
#خروجی : hosein is 30 years old.

#بعدی اینه که متیونی جلوس عدد هم بزاری 

q = "abc"
t = 51
print(f"{q:10} , {t}")
#خروجی : abc        , 51
#خب اینجا چون استرینگم فقط سه حرفه برای تبدیل شدن به 10 تا پایتون از 7 تا خط  فاصله استفاده کرد

