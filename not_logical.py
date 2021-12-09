# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# a = float(input("Bir sayı giriniz: "))
# result = a>0 and a<100

# print(f"Girdiğiniz {a} değeri 0 ile 100 arasında bir değer midir: {result} ")

# 2- Girilen bir sayının pozitif çift sayı olup olamdığını kontrol ediniz.
# a = int(input("Bir sayı giriniz: "))
# result = (a%2 == 0) and (a>0)
# print(f"{a} değeri pozitif çift sayı mıdır : {result}")

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 
# email = "kuscumehmetsaban@gmail.com"
# sıfre  = "ksc123"

# mail = input("Bir mail adresi girin: ")
# password = input("Bir şifre girin: ")

# result = (mail == email) and ( password == sıfre)
# print (f"Girdiğiniz mail ve şifre doğru mu: {result}")

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırın
# a = int(input("a değerini giriniz: "))
# b = int(input("b değerini giriniz: "))
# c = int(input("c değerini giriniz: "))

# result = a>b and c>a
# print(f"a en büyük müdür : {result}")
# result = b>a and b>c
# print(f"b en büyük müdür : {result}")
# result = c>b and c>a
# print(f"c en büyük müdür : {result}")

# 5- Kullanıcıdan 2 vize %60 ve final %40 notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

# ılkvize = int(input("1. Vize: "))
# ıkıncıvize = int(input("2. Vize: "))
# fınal = int(input("Final: "))


# ort = ((ılkvize+ıkıncıvize)*0.30+fınal*0.4)
# result= ort >= 50
# print(f"{ort} notu ile geçtim mi : {result}")
    # a-)
# result = ort>=50 and fınal>=50
# print(f"ortalama {ort} ve final notu{fınal} ile geçer miyim: {result} ")

    # b-)
# result = fınal>=70 or ort>=50
# print(f"fınalden {fınal} ile geçer miyim: {result}")



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
result = 0<= form and form<= 18.4
result2 = 18.5<= form and form<= 24.9
result3 = 25<= form and form<= 29.9
result4 = 30<= form and form<= 34.9
print(f"{Ad} kardeşin indexi {form} bakalım indexi zayıf mı: {result}")
print(f"{Ad} kardeşin indexi {form} bakalım indexi normal mi: {result2}")
print(f"{Ad} kardeşin indexi {form} bakalım indexi fazla mı: {result3}")
print(f"{Ad} kardeşin indexi {form} bakalım indexi obez mi: {result4}")











