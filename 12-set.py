#خب بریم سراغ set
#set ها با {} ساخته میشن
a = {"ronaldo" , "messi" , "neymar"}
print(a)
#خروجی : {'messi', 'neymar', 'ronaldo'}
#خروجی set  ها همیشه به هم ریختع اس

k = {"vini" , "halland" , "mbape" , "mbape"}
print(k)
#خروجی : {'mbape', 'halland', 'vini'}
#set کلمات تکراری اضافی رو چاپ  نمیکنه
#ولی به حروف بزرگ و کوچیک حساسه
l = {"daD" , "DAd" , "mom"}
print(l)
#خروجی : {'DAd', 'mom', 'daD'}

#عدد هم میشه نوشت
f = {1 , 2 , 3 , 4 , 5}
print(f)
#خروجی : {1, 2, 3, 4, 5}

m = {1 , 2 , 3}

if 3 in m:
    print('yes')
#خروجی : yes

#خوب ما از  not برای وجود نداشت استفاده میکنیم 

i = {1 , 2 , 3 , 4 , 5}

if 85858 not in i:
    print("no")

    #خروجی : no

#با کلمه کلیدی set میتونم حروف یک متن رو تکه تکه کنیم

h = set("ronaldo")
print(h)
#خروجی: {'r', 'l', 'o', 'n', 'd', 'a'}

