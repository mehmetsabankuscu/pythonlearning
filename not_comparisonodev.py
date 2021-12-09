


# 1- Girilen 2 sayıdan hangisi büyüktür ?
# a = int(input('1.Sayı: '))
# b = int(input('2.Sayı: '))

# result = a>b
# print(f'a: {a} b: {b} den büyüktür. {result}')

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

# a = int(input('1.Vize: '))
# b = int(input('2.Vize: '))
# c = int(input('Final: '))

# result = (((a+b)*0.3)+c*0.4)

# d = result >= 50 

# print(f"Öğrencinin 1.vize notu {a} 2.vize notu {b} final notu {c} olup ortalamısı da {result} olup dersi geçmiştir: {d}")

# 3- Girilen bir sayının tek mi çift mi olduğunu yazırın.
# x = int(input('Bir sayı girin: '))
# result = x%2 
# d = (result == 1)
# print(f"Girmiş olduğunuz {x} değeri tektir: {d} ")

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
# x = int(input('Bir sayı girin: '))
# result = (x > 0)
# print(f"Girmiş olduğunu {x} değeri pozitiftir: {result}")
# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@sadikturan.com parola:abc123)

doğrumail='email@sadikturan.com'
doğruşifre='abc123'

mail= input("Email Adresinizi Giriniz: ")
password = (input("Şifrenizi Giriniz: "))

a = (mail.lower().strip() == doğrumail )
b = (password.lower() == doğruşifre.lower())

print(f"Girmiş olduğunuz mail doğrudur:{a} ve şifre doğrudur: {b}")
