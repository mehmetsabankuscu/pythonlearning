liste = ["1","2","5a","10b","abc","10","50"]

#1: liste elemanları içindeki sayısal değerleri bulunuz.
# sayı=[]
# for x in liste:
#     try:
#         result = int(x)
#         print (result)
#         sayı.append(x)
#     except Exception as ex:
#         print('yanlış bilgi girdiniz',ex)
# print (sayı)
# # # # # # # # # # # # # # # ***********************************************
# for x in liste:
#     try:
#         result = int(x)
#         print (result)
#     except ValueError:
#         continue

# 2: kullanıcı 'q' değerini girmedikçe aldığınız her inputun
# sayı olduğundan emin olunuz aksi halde hata mesajı yazın.

# while True:
#     sayı = input("Sayı giriniz:  ")
#     if sayı == "q":
#         break
#     try:
#         result = float(sayı)
#         print("girdiğiniz değer ", result)
#         break
#     except ValueError:
#         print("girdiğiniz değer hatalı ")



# 3: Girilen parola içinde türkçe karakter hatası veriniz.
# def checkPassword(password):
#     tr_karakter= "şçüğöıi"

#     for i in password:
#         if i in tr_karakter:
#             raise Exception("parola türkçe karakter içeremez")
#         else:
#            pass
#     print("sıkıntı yok")
    
# password = input("Şifreyi Giriniz: ")     
# try:
#     checkPassword(password)
# except Exception as e:
#     print(e)




# 4: Faktöriyel fonksiyyonu oluşturacaz fonsiyona gelen değer için
# hata mesajları verecez.


def faktoriyel(x):
    x = int(x)

    if x<0:
        raise Exception("negatif değer")
    result = 1

    for i in range(1,x+1):
        result*=i
    return result 

for x in [5,10,20,-3,'10a']:
    try:
        y = faktoriyel(x)
    except Exception as e:
        print(e)
        continue
    print(y)





