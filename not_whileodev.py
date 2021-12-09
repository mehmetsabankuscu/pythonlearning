sayilar = [1,3,5,7,9,12,19,21]

# 1- sayilar listesini while ile ekrana yazdırın.
# a = 0
# while a<len(sayilar):
#     print(sayilar[a]) 
#     a+=1

# 2- Başlangıç ve bitiş değerlerinin kullanıcıdan alıp araddaki tüm
#    tek sayıları ekrana yazdırın. 

# baş = int(input("Başlangıç değerini gir: "))
# son = int(input("Bitiş değerini gir: "))

# while baş<son:
#     baş=baş+1
#     if baş%2==1:
#         print(baş)

# 3- 1-100 arasındaki sayıları azalan şeklinde yazdırın.
# a=101
# while 1<a<=101:
#     a-=1
#     print(a)
#####********2.yöntem********########
# i = 100
# while i>0:
#     print(i)
#     i-=1

# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı şekilde yazdırın.
# x = 1
# liste=[]
# while x <= 5:  
#     x += 1
#     sayıgır = int(input("sayı giriniz: "))
#     liste.append(sayıgır)
# liste.sort()
# print(liste)
# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayın. 
# ** ürün sayısını kullanıcıya sorun.
# ** dictionary listesi yapısı (name, price) şeklinde olsun.
# ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
ürünsayısı = int(input("Eklemek isteğin ürün sayısı gir: "))
ürünlistesi = []

while len(ürünlistesi) < ürünsayısı:

    ürünadı = input("Ürünün adını giriniz: ")
    ürünfiyatı = float(input("Ürün fiyatı girin: "))
    dic={
        "name":ürünadı,
        "price":ürünfiyatı,
    }
    ürünlistesi.append(dic)
# print(ürünlistesi)
for urun in ürünlistesi:
    print(f"ürünadı: {urun['name']} ve ürünün fiyatı {urun['price']}")