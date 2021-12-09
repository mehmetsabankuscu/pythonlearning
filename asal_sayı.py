#### Soru girilen bir sayının asal olup olmadığını bulun.

# sayı = int(input("Bir sayı girin: "))
# asalmı=True
# if sayı == 1:
#     asalmı = False
# for i in range(2,sayı):
#     if (sayı%i==0):
#         print("Sayı asal değil")
#         asalmı=False
#         break
# if asalmı:
#     print("Sayı asaldır. ")
# else:
#     ("Sayı asal değil. ")


########veya##############

sayı=int(input("Sayı giriniz: "))
if(sayı==2):
    sonuç="sayı asal"
liste=list(range(2,sayı))
for i in liste:
    if(sayı%i==0):
        sonuç="asal sayı değil. "
        break
    else:
        sonuç="asal sayı ."
        

print(sonuç)










