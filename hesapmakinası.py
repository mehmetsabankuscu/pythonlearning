giriş = """*********************************
*  (1) topla                               *
*  (2) çıkar                               *
*  (3) çarp                                *
*  (4) böl                                 *        
*  (5) karesini hesapla                    *
*  (6) karekök hesapla                     *
********************************************
"""
print(giriş)
soru = input("Yapmak istediğiniz işlemin numarasını girin: \n")
if soru == "1":
    sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: \n"))
    sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: \n"))
    print(sayı1, "+", sayı2, "=", sayı1 + sayı2)
elif soru == "2":
    sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: \n"))
    sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: \n"))
    print(sayı3, "-", sayı4, "=", sayı3 - sayı4)
elif soru == "3":
    sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: \n"))
    sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: \n"))
    print(sayı5, "x", sayı6, "=", sayı5 * sayı6)
elif soru == "4":
    sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: \n"))
    sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: \n"))
    print(sayı7, "/", sayı8, "=", sayı7 / sayı8)
elif soru == "5":
    sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: \n"))
    print(sayı9, "sayısının karesi =", sayı9 ** 2)
elif soru == "6":
    sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: \n"))
    print(sayı10, "sayısının karekökü = \n",sayı10 ** 0.5)
else :
    print('adam gibi sayı gir')
