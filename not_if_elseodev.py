# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol edininz.
#    Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

# isim = input("İsim giriniz: ")
# yaş = int(input("Yaş bilgisi giriniz: "))
# eğitim = input("Eğitim durumu giriniz: ")

# if yaş >= 18 and (eğitim == "lise" or eğitim == "üniversite" ) :                                ##### İlkini Ben yazdım
#     print(f"{isim} Bey ehliyet alabilir. ")
# elif  yaş >= 18 and (eğitim != "lise" or eğitim != "üniversite" ) :
#     print(f"{isim} Bey eğitim düzeyiniz ehliyet almaya uygun değil. ")
# elif  yaş < 18 and (eğitim == "lise" or eğitim == "üniversite" ) :
#     print(f"{isim} Bey yaşınız ehliyet almaya uygun değil. ")
# else:
#     print(f"{isim} Bey eğitim seviyeniz ve yaşınız bu işi yapmaya uygun değil. ")

# isim = input("İsim giriniz: ")
# yaş = int(input("Yaş bilgisi giriniz: "))
# eğitim = input("Eğitim durumu giriniz: ")
#                                                                                     ####ikinci yapılan videodan

# if yaş >= 18 :
    
#     if (eğitim == "lise" or eğitim == "üniversite" ):
#         print(f"{isim} Bey ehliyet alabilir. ")
#     else:
#         print(f"{isim} Bey eğitim düzeyiniz ehliyet almaya uygun değil. ")
# else:
#     print(f"{isim} Bey yaşınız ehliyet almaya uygun değil. ")


# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre 
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0-24   => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4 
#    85-100 => 5

# ilkyazılı = int(input("1. yazılı notu: "))
# ikinciyazılı = int(input("2. yazılı notu: "))
# sozlunotu =  int(input("Sözlü notu: "))

# ortalama = (ilkyazılı + ikinciyazılı + sozlunotu )/3

# if 0<= ortalama <=24 :                                  #### if 0<=ortalama and ortalama<=24   aynı manaayı ifade etmekte.
#     print(f"Ortalamanız {ortalama} Notunuz: 0 ")
# elif 25<= ortalama <=44 : 
#     print(f"Ortalamanız {ortalama} Notunuz: 1")
# elif 45<= ortalama <=54 : 
#     print(f"Ortalamanız {ortalama} Notunuz: 2")
# elif 55<= ortalama <=69 : 
#     print(f"Ortalamanız {ortalama} Notunuz: 3")
# elif 70<= ortalama <=84 : 
#     print(f"Ortalamanız {ortalama} Notunuz: 4")
# elif 84<= ortalama <=100 :
#     print(f"Ortalamanız {ortalama} Notunuz: 5")
# else:
#     print("Yanlış bilgi girdiniz. ")




# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanı aşağıdaki bilgilere göre hesaplayınız.
#    1. Bakım => 1. yıl
#    2. Bakım => 2. yıl
#    3. Bakım => 3. yıl
#    ** Süre hesabına alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#    ***Datetime modülünü kullanmanız gerekiyor.
#    (şimdi) - (2018/8/1) => gün

# **********datetime açık olamdan*************
# days = int(input("Araç kaç gündür trafikte: "))

# if days <= 365:
#     print("1. Servis Aralığı")
# elif 365 < days <= 365*2:
#     print("2. Servis Aralığı")
# elif 365*2 < days <= 365*3:
#     print("3. Servis Aralığı")
# else:
#     print("Hatalı süre")

#**************************************************AŞAĞIDAKİLER BİRAZ KARIŞIK BİLGİ**************************
import datetime

tarih = (input("Araç hangi tarihte trafiğe çıktı (2019/8/9): "))
tarih = tarih.split('/')
# print(tarih[0])
# print(tarih[1])
# print(tarih[2])

trafigecıkıs = datetime.datetime(int(tarih[0]),int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now()

fark = simdi - trafigecıkıs
days = fark.days


if days <= 365:
    print("1. Servis Aralığı")
elif 365 < days <= 365*2:
    print("2. Servis Aralığı")
elif 365*2 < days <= 365*3:
    print("3. Servis Aralığı")
else:
    print("Hatalı süre")
