# numbers = [1,2,3,4,5]

# for num in numbers:
#     print(num)            ##**listenin herbir elemanını ekrana yazıp num değişkenine atar

# for num in numbers: 
#     print("hello")       ###** listenin elemanı kadar ekrana hello yazdır.
# print(type(num))         
# print (num)


# names = ["çınar", "sadık","sena"]

# for name in names:
#     print(f"may name is {name}")


# name= "Mehmet Şaban"

# for n in name:
#     print(n)


# tuple = (1,2,3,4,5)
# for t in tuple:
#     print(t)

# tuple = [(1,2),(3,4),(5,6)]
# for t in tuple:
#     print(t)


# tuple = [(1,2),(3,4),(5,6)]
# for t,y in tuple:                 ####** t,y tanımalması yaparak liste içeriside hangi indexteki veriyi istiyorsak ona rahat br şekiilde ulaşabiliriz.
#     print(t,y)

# d = {"k1":1, "k2":2, "k3":3}
# for key in d:
#     print(key)                            ####dictionary veri tiplerinde döngüye eğer .item() yazarak döngü yazılmazsa 
                                                #verilerin sadece key kısmına ulaşırız .item() yazdıktansonra iki tarftan hangi veri isteniyorsa ona ulaiabiliriz.

d = {"k1":1, "k2":2, "k3":3}
for key,value in d.items():
    print(value)










