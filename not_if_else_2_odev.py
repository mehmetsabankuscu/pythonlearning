# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# a = float(input("Bir sayı girin: "))
# if a<0:
#     print("Girdiğiniz değer 0'dan küçüktür. ")
# elif 0<= a <=100:
#     print("Girdiğiniz değer 0 ile 100 arasındadır.")
# else:
#     print("Girdiğiniz değer 100'den büyüktür.")


# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
# a = int(input("Bir sayı girin: "))
# if a>0 and a%2==0:
#     print("Girdiğiniz değer pozitif çift sayıdır. ")
# elif a<0 and a%2==0:
#     print("Girdiğiniz değer negatif çift sayıdır. ")
# elif a<0 and a%2 != 0:
#     print("Girdiğiniz değer negatif tek sayıdır. ")
# else:
#     print("Girdiğiniz değer pozitif tek sayıdır")


    ####********aşağıdaki videodan*********###
# a = int(input("Bir sayı girin: "))
# if a>0:
#     if a%2 == 0:
#         print("Girdiğiniz değer pozitif çift sayıdır. ")
#     else :
#          print("Girdiğiniz değer pozitif tek sayıdır")
# else :
#     print("Girdiğiniz değer negatiftir.")


# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 
# email = "kuscumehmetsaban@gmail.com"
# password = "12346"

# mailadres = input("Mail adresi girin: ")
# sifre = input("Şifrenizi girin: ")

# if (email == mailadres):
#     if(password==sifre):
#         print("...Hoşgeldiniz...")
#     else:
#         print("Şifre hatalı. ")
# else:
#     print("Mail adresi hatalı. ")

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırın
# a=int(input("Bir sayı girin: "))
# b=int(input("Bir sayı girin: "))
# c=int(input("Bir sayı girin: "))

# if a<b and a<c:
#     print("a değeri en küçük değerdir. ")
# elif b<a and b<c:
#     print("b değeri en küçük değerdir. ")
# elif c<a and c<b:
#     print("c en küçük değerdir.")



# 5- Kullanıcıdan 2 vize %60 ve final %40 notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

# ılkvize = float(input("1. Vize: "))
# ıkıncıvize = float(input("2. Vize: "))
# fınal = float(input("Final: "))
# ort = ((ılkvize+ıkıncıvize)*0.30+fınal*0.4)

# # a)
# if (ort>=50):
#     if (fınal >= 50):
#         print(f"{ort} ile Dersi geçtin. ")
#     else:
#         print(f"{ort} ile Dersten kaldın. ")
# else:
#     print(f"{ort} ile Dersten kaldın. ")



# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indexlerini hesaplayınız.
#    Formül: (Kilo / Boy Uzunluk Karesi) 
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4     => Zayıf
#    18.5-24.9  => Normal 
#    25.0-29.9  => Fazla Kilolu
#    30.0-34.9  => Obez

Ad = input("Adınızı giriniz: ")
Kilo = float(input("Kilonuzu giriniz: "))
Boy = float(input("Boyunuzu giriniz: "))

form = Kilo/(Boy**2)

if 0<= form <= 18.4:
    print(f"{Ad} kardeşin indexi {form} ve zayıf. ")
elif  18.5<= form and form<= 24.9:
    print(f"{Ad} kardeşin indexi {form} ve normal. ")
elif 25<= form and form<= 29.9:
    print(f"{Ad} kardeşin indexi {form} ve fazla . ")
elif 30<= form and form<= 34.9:
    print(f"{Ad} kardeşin indexi {form} ve obez. ")
else:
    print("ohaaaa")

# result = 0<= form and form<= 18.4
# result2 = 18.5<= form and form<= 24.9
# result3 = 25<= form and form<= 29.9
# result4 = 30<= form and form<= 34.9
# print(f"{Ad} kardeşin indexi {form} bakalım indexi zayıf mı: {result}")
# print(f"{Ad} kardeşin indexi {form} bakalım indexi normal mi: {result2}")
# print(f"{Ad} kardeşin indexi {form} bakalım indexi fazla mı: {result3}")
# print(f"{Ad} kardeşin indexi {form} bakalım indexi obez mi: {result4}")