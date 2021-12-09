#bankamatik uygulaması
MehmetHesap = {
    "ad":"mehmet kuscu",
    "hesap no": "32576874",
    "bakıye":3000,
    "ek hesap": 2000
}

SadıkHesap = {
    "ad":"Sadık Turan ",
    "hesap no": "2151684",
    "bakıye":2000,
    "ek hesap": 1000
}

def paraver(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    
    if(hesap['bakıye'] >= miktar):
        hesap['bakıye']-=miktar
        print("Paranızı alabilirsiniz.  ")
    else:
        toplam = hesap["bakıye"]+hesap["ek hesap"]
        if toplam >= miktar:
            ekhesapkullanımı = input("ek hesap kullanılsın mı (E/H)")

            if ekhesapkullanımı=="E":
                ekhesapkullanımı = miktar - hesap["bakıye"]
                hesap["bakıye"]=0
                hesap["ek hesap"]-=ekhesapkullanımı
                print("paranızı alabilirsiniz.  ")
                
            else:
                print(f"{hesap['hesap no']} nolu hesabınızda {hesap['bakıye']} bulunmaktadır. ")

        else :
            print("üzgünüm para yetersiz")


paraver(MehmetHesap, 4000)

