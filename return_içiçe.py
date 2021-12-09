# def usalma (number):

#     def inner(power):
#         return number**power
    
#     return inner
# a=usalma (5)
# b=a(3)
# print(b)

# c=usalma (4)
# d=c(2)
# print(d)


#####*********** örnek

# def yetki_sorgula(page):
#     def inner(role):
#         if role == "admin":
#             return "{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz.".format(role,page)
#     return inner

# # user = yetki_sorgula("heloo")("admin")
# # print(user)
# ######## VEYA **************
# user1 = yetki_sorgula("product edit")
# print(user1("admin"))



def islem(islem_adı):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim
    if islem_adı == "toplama":
        return toplam
    else:
        return carpma


toplama = islem ("toplama")
print(toplama(1,3,5,6,8,7))

###### VEYA
carpma = islem("carpma")(1,5,6,9)
print(carpma)