# 1- "bmw, mercedes, opel, mazda" elemanlarına sahip bir liste oluşturun
arabalar = ["bmw", "mercedes", "opel", "mazda"]


# 2- liste kaç elemanlıdır.
result = len(arabalar)

# 3- listenin ilk ve son elemanı nedir?
result = arabalar[0]
result = arabalar[-1]
# 4- mazda değerini toyota ile değiştirin.
arabalar[3] = "toyota"
result = arabalar
# 5- mercedes listenin bir elemanı mıdır?
result = arabalar.index('mercedes')
                #veya
result = 'mercedes' in arabalar
# 6- Listenin -2 indexindeki değer nedir?
result = arabalar[-2]
# 7- listenin ilk üç elemanını alın.
result = arabalar[0:3]
result = arabalar[:3]
result = arabalar[-2:]
# 8- Listenin son iki elemanı yerine "toyota" ve "renault" değerlerini ekleyin.
result = arabalar[-2:] = "toyota", "renault"
result = arabalar
# 9- listenin üzerine "audi" ve "nissan" değerlerini ekleyin.
result = arabalar + ["audi", "nissan"]
# 10- listenin son elemanını sil.

del arabalar[-1]
result = arabalar

# 11- liste elemanlarını tersten yazdır.
arabalar.reverse()
result = arabalar
                    # veya
result = arabalar[::-1]
# 12- aşağıdaki verileri bir liste içinde saklayınız.
    #studentA: Yiğit Bilgi 2010, (70,60,70)
    #studentB: Sena Turan 1999, (80,80,70)
    #studentC: Ahmet Turan 1998, (80,70,90)

studentA = ["Yiğit", "Bilgi", 2010, [70,60,70]]    
studentB = ["Sena", "Turan", 1999, [80,80,70]]
studentC = ["Ahmet", "Turan", 1998, [80,70,90]]

# 13- listenin elemanlarrını ekrana yazdır.
result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentB[0]} {studentA[1]} {2021-studentA[2]} yaşında ve ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"




print(result)






