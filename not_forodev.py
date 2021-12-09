sayılar = [1,3,5,7,9,12,19,21]

# 1- sayılar listesindeki hangi sayılar 3'ün katıdır?

# for a in sayılar:
#     if a%3==0:
#         print (a)

# 2- sayılar listesindeki sayıların toplamı kaçtır?

####*****1.Yöntem*****####
# liste = []
# for a in sayılar:
#     liste.append(a)  
#     toplam = sum(liste)
# print(toplam)
####****2.Yöntem****####
# b = 0
# for a in sayılar:
#     b=b+a 
# print(b)




# 3- sayılar listesindeki tek sayıların karesini alınız.
# list= []
# for a in sayılar:
#     if a%2 == 1:
#         a=a**2
#         list.append(a)
        
# print(list)
#######********2.Yöntem******#######
# b = 0
# for a in sayılar:
#     if a %2 == 1:
#         print(a**2)

sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]

# 4- Şehirlerden hangileri en fazla 5 karakterlidir?
# beskrktr = []
# for a in sehirler:
#     if len(a) <=5:
#         beskrktr.append(a)
# print(beskrktr)

#####******2. Yöntem*******#####
# for a in sehirler:
#     if (len(a)) <=5:
#         print(a)



urunler =[
    {"name":"samsung S6", "price":"3000"},
    {"name":"samsung S7", "price":"4000"},
    {"name":"samsung S8", "price":"5000"},
    {"name":"samsung S9", "price":"6000"},
    {"name":"samsung S10", "price":"7000"},
]


# 5- Ürünlerin fiyatları toplamı nedir ?
# list = []
# for k in urunler:
#     k["price"] = int(k["price"])
#     list.append(k["price"])
#     toplam = sum(list)
# print(toplam)
#####******2. Yöntem*******#####
# b = 0
# for k in urunler:
#     toplam = int(k["price"])
#     b += toplam
# print(b)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

# for k in urunler:
#     k["price"] = int(k["price"])
#     if k["price"] <=5000:
#         print(k["name"],k["price"])














