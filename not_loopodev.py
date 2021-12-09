import random                                                   
                                                        ###NOT###
                                        ### a = round(random.uniform(1,100),2) 
                                        ### uniform belli sayı aralığında sayı üretmek için kullanılır.
                                        ### round virgülden sonra kaç hane olacağını kontrol etmeye yarar.

x = round(random.uniform(1,100))      ### veya random.randit(1,100)

can = int(input("Hak sayısı: "))
haksayısı = can
sayaç = 0

while 0<haksayısı :
    sayaç+=1
    haksayısı-=1
    tahminim = int(input("Bilin bakalım x kaç: "))
    puanım=(100-(100/can)*(sayaç-1))   
    if tahminim == x:
        print(f"puanınız {sayaç}. seferde bildiniz puanınız: {round(puanım)} ")
        break
    elif tahminim < x:
        print("yukarı")        
    else :
        print("aşağı")    
    if haksayısı==0:
        print(f'Hakkınız bitti sayı {x} idi  ')

    



   















