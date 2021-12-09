fruits ={'orange', 'apple', 'banana'}

# print(fruits[0])         ### set verileri indexlenmediği için bu şekilde ekrana yazdırılmaz.

for x in fruits:
    print(x)               #### fruits verilerini x üzeribe yaz demek.


fruits.add('cherry') ### Birden fazla eleman eklemek için burada yapılması gereken add fonksiyonunu bir daha alta yazmak olacak ancak bunun kolayı oalrak update metodunu kullanacağız.

fruits.update(['mango', 'grape'])
fruits.update(['mango', 'grape','apple'])   ### Eğer kümede eleman varsa bir daha yazmaz.

fruits.remove('mango')
fruits.discard('apple')
print(fruits)

fruits.pop()   ### normalde listedeki verilerde son elemanı silmeye yarayan bu fonksiyon kümeler indexlenmediği için sondaki elemanı silmez.Bunun dışında herhangi bir elemanı silmeye yarar.
fruits.clear() ### tüm küme elemanlarını siler
print(fruits)

# myList = [1,2,5,4,4,2,1]
# print(myList)
# print(set(myList))








