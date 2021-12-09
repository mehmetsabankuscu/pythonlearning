list = [1, 2, 3 ]

tuple = (1, 'iki', 3)

# print (type(list))
# print (type(tuple))


# print(list[2])
# print(tuple[2])

# print(len(tuple))
# print(len(list))

list = ['ali', 'veli']
tuple = ('damla', 'ayşe', 'ayşe')
names = ('emel', 'memet', 'said') + tuple

print(names)
list[0] ='ahmet'
#tuple[0] = 'deniz'          #tuple içeriğinde listede yapabildiğimiz gibi değişiklik yapılamaz.

print(tuple.count('ayşe'))
print(tuple.index('ayşe'))     #tuple veriler indexlenebilir

print(list)
print(tuple)
