# numbers = []
# for a in range(10):
#     numbers.append(a)
# print(numbers)

# # # # # # Bunu yapmanın daha pratik bir yolu var ######

# numbers = [a for a in  range(10) ]
# print(numbers)


# kare= []
# for x in range(10):
#     kare.append(x**2)
# print(kare)

# kare = [x**2 for x in range(10)]
# print(kare)

# kare = [x*x for x in range(10) if x%3 == 0 ]
# print(kare)

# mystring="hello"
# mylist=[]
# for c in mystring:
#     mylist.append(c)
# print(mylist)

# kelime="Merhaba"
# harfler = [a for a in kelime ]
# print (harfler)

# years = [1983, 1999, 2008, 1956, 1986]
# yaşlar = [2021-yıl for yıl in years]
# print(yaşlar)


# result = [x if x%2 == 0 else "tek" for x in range(1,10)]
# print(result)
# result = []
# for x in range(3):
#     for y in range(3):
#         for z in range(3):
#             result.append((x,y,z)) ### appendde 1 den fazla eleman girince iki parantez gerekiyor
    
# print(result)

###daha pratik bir çözüm
# result =[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
# print(result)