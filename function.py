# def sayHello(x = "user"):
#     print("Hello " + x)

# sayHello("Mehmet")
# sayHello("Şaban")
# sayHello()

# #####*************************************************####

def sayHello(x = "user"):
    return "Hello " + x
     
msg = sayHello("Mehmet")
msg = sayHello("Şaban")

print(msg)
# #####*************************************************####
# def total(num1, num2):
#     return num1+num2
# result = total(10,20)
# result = total(15,20)

# print(result)
# #####*************************************************####
def yasHesapla(Dogumyılı):
    return 2020-Dogumyılı
ali = yasHesapla(2000)
veli = yasHesapla(2010)

print (ali,veli)
#####*************************************************####
def EmekliligeKacYilKaldi(Dogumyılı, isim):
    ''' 
    DOCSTRING: Dogum yılınıza göre emekliliğinize kaç yıl kaldı.
    INPUT: dogum yılı
    outuput: hesaplanan yıl bilgisi
    '''
    yas = yasHesapla(Dogumyılı)
    emeklilik = 65- yas

    if emeklilik>0:
        print(f"emekliliğinize {emeklilik} yıl kaldı. ")
    else:
        print("zaten emeklisiniz. ")
   
EmekliligeKacYilKaldi(1983,"ali")

# print(help(EmekliligeKacYilKaldi))

# list = [1,2,3,4]
# print(help(list.append))#### help methodu fonksiyonla veya methodla alakalı karşı tarfa  bilgi verir.








