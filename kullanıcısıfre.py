yazı = """
            *********
        Uygulamaya Hoşgeldiniz

Lütfen Kullanıcı Adınızı ve Parolanızı
        Doğru Şekilde Giriniz.
            *********
"""

print(yazı)

kullanıcıAdı = "kuscumehmetsaban"
Sıfre = "15046049"

user = input("Kullanıcı Adını Giriniz: \n")

password = input("Şifreyi Gİriniz: \n")


if (kullanıcıAdı == user and Sıfre == password) : 
    print("...Sisteme Hoşgeldiniz...")
elif (kullanıcıAdı != user and Sıfre == password) :
    print("...Kullanıcı Adını Yanlış Girdiniz...\nLütfen Tekrar Deneyin...")
elif (kullanıcıAdı == user and Sıfre != password) :
    print("...Şifreyi Yanlış Girdiniz...\nLütfen Tekrar Deneyin...")
else :
    print("...Kullanıcı Adını ve Şifreyi Yanlış Girdiniz...\nLütfen Tekrar Deneyin...")