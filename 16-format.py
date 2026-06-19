#مبحث امروز در مورده format هستش

#کار فورمت اینع که چند تا متغییر توی یه استرینگ قرار میده

#برای اینکه این کارو بکنی باید توی استرینگت یه {} بزاری

name = "sajjad "
age = 15

print("{}is {} years old.".format(name , age))
#خروجی : sajjad is 15 years old.

#حتما باید اسم متغییر ها رو درست بدی چون منطق نوشتن رو خربا میکنه 
#مثلا
print("{}is {} years old.".format(age , name ))
#  15is sajjad  years old.
#این جمله اصلا معنی نمیده پس باید اسم متغییر ها رو به ترتیب درست بنویسی


#از این روش هم میشه استفاده کرد


print("{} {}".format("hello", "world"))
#خروجی : hello world


#خوب ما میتونیم اکولاد ها رو هم شماره گزاری بکنیم (شماره گزاری از 0 شروع میشه)

print("{0} {1} ".format("hello" , "sajjad"))
#خروجی : hello sajjad
#اینجا hello میشه شماره 0 و sajjad میشه شماره 1
#اگه جا به جا عدد گذاری کنیم کدمون به هم میخوره


print("{1} {0} ".format("hello" , "sajjad"))
#خروجی : sajjad hello


#مال علاوه بر اینکه میتونیم عدد بنویسیم اسم هم میتونیم بنویسیم
# مثال


namee = "ronaldo"
agee = 41
print("{a} {b}".format(a = namee , b = agee))
#خروجی : ronaldo 41

#مثل بالا اگه جاهارو جابه جا بنویسی جمله به هم میخوره

print("{b} {a}".format(a = namee , b = agee))
#خروجی : 
#41 ronaldo


#ما میتونیم از همین متود فورمت برای دیکشنری هم استفاده کنیم

info = {"namme" : "sajjad " , "agge" :  15 }

print("{0[namme]}is{0[agge]}years old".format(info))
#خروجی : sajjad is15years old



#ما میتونیم چن تا دیکشنری هم بنویسیم

infoo = {"nname" : " messi " , "aage" : 38}
infoo1 = {"nnaame" : "cristiano " , "aagge" : 41}
print("{0[nnaame]} is {0[aagge]}years old and{1[nname]} is {1[aage]}years old.".format(infoo1 , infoo))
#خروجی : cristiano  is 41years old and messi  is 38years old.


