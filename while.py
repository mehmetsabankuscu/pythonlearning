# 1- 50 e kadar


# x=1
# while x <= 50 : 
#     print(x)
#     x += 1
#     # buraya print koyarsam 51 sayısıda ekrana gelir. ama yukarıda öyle bir durum olmaz.
# print("bitti")


# x=1
# while x <= 50 :
#     if x%2==0:
#         print(f"{x} sayısı çifttir.")
#     else:
#         print(f"{x} sayısı tektir.")
#     x += 1
#     # buraya print koyarsam 51 sayısıda ekrana gelir. ama yukarıda öyle bir durum olmaz.
# print("bitti....")


name = '' #false
while not name.strip() :
    name = input("isminizi giriniz: ")
print(f"Merhaba {name}")

