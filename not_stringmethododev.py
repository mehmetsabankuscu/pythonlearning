website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1-' Hello World ' karakterinin dizisinin baş ve sondaki boşluk karakterlerini silin.

result=" Hello World u".strip()
result=" Hello World u".lstrip()
result=" Hello World u".rstrip()

result = website.lstrip('/:pth')
# 2- "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakterii silin.

result = "www.sadikturan.com".lstrip('w.').rstrip('.com')
                       # veya
result = "www.sadikturan.com".strip('w..com')

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result = course.lower()
# 4-  'website' içinde kaç tane a karakteri vardır?(count('a'))
result = website.count('a')
result = website.count('www')
result = website.count('www',0,10)


# 5- 'website www ile başlayıp com ile bitiyor mu? )'
result = website.startswith('www')
result = website.endswith('com')
# 6-  'website' içinde '.com' ifadesi var mı ?
result = website.find('.com')
result = website.find('.com',0,15)
result = course.find('Python')
result = course.rfind('Python')

result =website.index('com')
result =website.rindex('com')
# result =website.index('comm') # exception


# 7-  ' course içindeki karakterlerin hepsi alfebetik mi? (isalpha, isdigit)'
result = course.isalpha()
result = 'hello'.isalpha()
result = course.isdigit()
result = '1235'.isdigit()
# 8-  'content' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

result = "content".center(50,"*")
result = "content".ljust(50,'*')
result = "content".rjust(50,"*")

# 9-  course karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result = course.replace(" ", "-")
result = course.replace(" ", "-",5)
result = course.replace(" ", "")
# 10-  "hello world" karakter dizisinin 'World ifadesini 'there' olaraka değiştirin'
result = "hello world".replace("world","there")
# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın.
result = course.split(' ')
result = result[5]





print (result)



