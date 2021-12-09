#####*****     lambda fonksiyonu ve map ve filter methodları     *****#####




# def square(num): return num**2  ## bu şekilde de yazılır sıkıntı olmaz.

# result = square(2)     ### 1 elemanla deneme yapıldı ve fonk çalıştı ancak elimizde bir liste varsa ne yapacaz onu görelim.

numbers = [1,3,5,7,9,4,10]
# result = map(square, numbers) ### Bu şekilde çalıştırırsak bize bu şekilde ->  <map object at 0x00000150E86DDE50> bir adresle geri döner
                            ### bize listedeki her bir elemanın karesi lazım onu da nasıl yapacaz deneyelim.
# result = list(map(square, numbers))   ### [1, 9, 25, 49, 81, 16, 100] bu şekilde sonuç geldi.Bunun için bir öceki result bilgisini listeye çevirdik.
                                       ###   yada bunun yerine şöyle bir yöntem deneyebiliriz.
# for item in map(square, numbers):  ### görüldüğü üzre ya listeyle çevreleyecez ya da for ile her bir değerei enumerate ederk dolaşıp ekrana basacaz.
#     print(item)

#####ismi olmayan fakat bize yukarıdaki gibi çalışacak bir fonksiyn lazımsa onu da lambda expresion ile taımlarız.
###### yani bir sayının kare ya da küpünü almak için tanımlı fonksiyonumu yada başka birşey için
###### tanımlamış olduğum bir fonksiyonla yaptığım bir işi lambda fonksiyonu ile yaparım ve
# ##### square olarak tanımladığımız fonksiyona gerek kalmaz(yukarıdaki fonsiyonu yorum satırına aldım). peki nasıl:

# result = list(map(lambda numara:numara**2, numbers))   ##### işte böyle kolay bir şekilde...yani aslında ben burada squareisimli fonksiyonun yaptığı işi isimsz bir fonksiyon ile yapmış oldum.
######eğer istersem lambda ile tanımladığım işlemi bir isim verip çalıştırabilirim.
# square=lambda numara:numara**2
# result = list(map(square, numbers))

#### bu şekilde isimli bir fonksiyon olarak işlemi yapmış olduk.
# # # # veya listede değilde sadece bir sayı üzerinde işlem yapacaksam şu şekilde yazıp sonuç alabilirim.
# print(square(5))  #### işte bu şekilde
# def çiftmı(x): return x%2==0         ### numberstakilerden çift olanları döndürmesini istedim.
# result=list(map(çiftmı, numbers))    ### ---> [False, False, False, False, False, True, True] diye bir sonuç gelir.
# result=list(filter(çiftmı, numbers))    ### ---> [4, 10] diye sonuç gelir yani sadece true sonuçları bana döndürdü.
### ya da 
# result=list(filter(lambda sayı:sayı%2==0,numbers))     ### ---> [4, 10] yine bu şekilde de aynı sonucu alrız.

### lamda ile yaptığımız işleme bir isim vererek tekrar yapabiliriz daha önceki satırlarda yaptığımız gibi .nasıl mı .....
# kontrolçıftmi = lambda sayı:sayı%2==0
# result=list(filter(kontrolçıftmi,numbers)) ### işte böyle yine aynı sonucu elde ettim.

#### hatta  numberstaki sayıların çift olup olmadığını da kontrol edebilirim 
# kontrolçıftmi = lambda sayı:sayı%2==0
# result=kontrolçıftmi(numbers[3])

print(result)