
# try:
#     file = open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya Okuma Hatası")
# finally:
#     print("Dosya Kapandı")
#     file.close


file = open("newfile.txt","r",encoding ="utf-8")

#### for döngüsü

# for i in file:
#     print(i, end="")
# file.close()

#### read() Fonksiyonu
# content1 = file.read()
# print("içerik1")
# print(content1)

# content2 = file.read()
# print("içerik2")
# print(content2)         ####Kursör en sonda kaldığı için texteki veri yeniden oku dersen birşey okumaz.ançak dosya açmayı tekrar yaparsan okur..

# file.close()


#########
# content = file.read(5)
# content = file.read(3)
# content = file.read(60)

# print(content)
# file.close()

#********** readline() fonksiyonu

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline())
# print(file.readline())
# print(file.readline())

# file.close()

#********** readline() fonksiyonu

liste = file.readlines()  # içerik liste haline gelir...

print(liste[0])
print(liste[1])
print(liste[2])



file.close()



