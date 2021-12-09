# 1- Göderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
# def yazdır(kelime,adet):
#     print(kelime*adet)
# yazdır("merhaba\n",10)

# 2- Kendine göderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazın.
# def listeyeCevır(*veri):
#     liste = []
#     for i in veri:
#         liste.append(i)
#     return liste
# result = listeyeCevır(1,2,3,"haelo","meraba")
# print(result)
# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

# def asalbul(x,y):
#     liste = []
#     for sayi in range(sayi1,sayi2+1):
#         if sayi>1:
#             for i in range(2,sayi):
#                 if sayi%i == 0:
#                     break
#             else:
#                 liste.append(sayi)
#     return liste
# sayi1 = int(input("Sayı 1: "))
# sayi2 = int(input("Sayı 2: "))
# result = asalbul(sayi1,sayi2)
# print(result)

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndür.


      
def tamBolenleriBul(x):
    bolenlist =[]
    for i in range(2,sayı):
        if sayı%i==0:
            bolenlist.append(i)
    return bolenlist

    
sayı=int(input("bir sayı gir: "))
result = tamBolenleriBul(sayı)
print










