names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

### 1-  "Cenk" ismini listenin sonuna ekleyiniz.

# names.append("Cenk")

### 2-  "Sena" değerini listenin başına ekleyin.

# names.insert(0,"Sena")
# names.insert(-1, 'Mehmet')
# names.insert(len(names), 'Mehmet')   # insertle sona eklme mantığı

### 3-  "Deniz" ismini listeden siliniz.

# names.remove('Deniz')
# names.pop()   # Parantez boş kalırsa son indexteki bilgiyi siler.
# names.pop(4)

### 4-  "Deniz isminin indexi nedir"

# index = names.index('Deniz')
# names.pop(index)
# print (index)
### 5-  'Ali' listenin bir elemanı mıdır?

# names ="Ali" in names
            #veya
# names = names.index("Ali")

### 6-    Liste elemanlarıı ters çevirin

# names.reverse()

### 7- Liste elemanlarını alfabetik olarak sıralayın.
 
# names.sort()

### 8-  years listesini rakamsal olarak sıralayınız.

# years.sort()

### 9-   str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.

# str = "Chevrolet, Dacia"
# result = str.split(",")                   #Karakterler bu Şekilde listeye dönüşür.
# print(result)

### 10- years dizisinin en büyük ve en küçük elemanı nedir?

# min = min(years)
# max = max(years)

### 11- years dizisinde kaç tane 1998 değeri vardır?

# years = years.count(1998)

### 12- years dizisinin tüm elemanlarını siliniz

# years.clear()

### 13-  Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayın.

markalar = []
# x = 1
# while x <= 3:  
#     x +=   1
#     markagır = input("Marka giriniz: ")
#     markalar.append(markagır)
for i in range(3):
    markagır = input("Marka giriniz: ")
    markalar.append(markagır)
print(markalar)




