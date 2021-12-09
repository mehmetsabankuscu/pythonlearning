def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')

    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3)/3

    if ortalama>=90:
        harf ="AA"
    elif ortalama>=80:
        harf ="BA"
    elif ortalama>=70:
        harf ="BB"
    elif ortalama>=60:
        harf ="CB"
    elif ortalama>=50:
        harf ="CC"
    elif ortalama>=40:
        harf ="DC"
    elif ortalama>=30:
        harf ="DD"
    elif ortalama>=20:
        harf ="FD"
    else: 
        harf ="FF"
    
    return ogrenciAdi + ":" + harf + "\n"

def ortalama_oku():
    with open("sınav_notları.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))
def not_gir():
    ad = input("Öğrenci Adı: ")
    soyad = input("Öğrenci Soyadı: ")
    not1 = input("1. Vize: ")
    not2 = input("2. Vize: ")
    not3 = input("3. Vize: ")


    with open("sınav_notları.txt","a",encoding="utf-8") as file:
        file.write(ad+' '+soyad+ ':'+not1+','+not2+','+not3+'\n')


def not_kaydet():
    with open("sınav_notları.txt","r",encoding="utf-8") as file:
        liste = []
        
        for i in file:
            liste.append(not_hesapla(i))
    
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)



while True:
    islem = input("1- Notları Oku\n2- Notları Gir\n3- Notları Kaydet\n4- Çıkış\n")

    if islem=="1":
        ortalama_oku()
    elif islem=="2":
        not_gir()
    elif islem == "3":
        not_kaydet()
    else:
        break