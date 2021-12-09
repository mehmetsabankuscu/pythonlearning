ogrenciler = {}
for i in range(3):                                                #for kullanarak da yapılabilir yani döngüyü üç kere yazmaya gerk yok.
    number = input('Öğrenci Numarası: ')
    name = input('Öğrencinin Adı: ')
    surname = input('Öğrencinin Soyadı: ')
    phone = input('Öğrenci Telefon Numarası: ')

# ogrenciler[number] = {
# 'adı':name,                              # ......... veya update methodu ile de kullanılabilir....
# 'soyadı':surname,
# 'telefon':phone
# }
    ogrenciler.update({
        number: {
            'adı' : name,
            'soyadı': surname,
            'telefon': phone,

        }

    })

# number = input('Öğrenci Numarası: ')
# name = input('Öğrencinin Adı: ')
# surname = input('Öğrencinin Soyadı: ')
# phone = input('Öğrenci Telefon Numarası: ')

# ogrenciler.update({
#     number: {
#         'adı' : name,
#         'soyadı': surname,
#         'telefon': phone,
        
#     }

# })

# number = input('Öğrenci Numarası: ')
# name = input('Öğrencinin Adı: ')
# surname = input('Öğrencinin Soyadı: ')
# phone = input('Öğrenci Telefon Numarası: ')


# ogrenciler.update({
#     number: {
#         'adı' : name,
#         'soyadı': surname,
#         'telefon': phone,
        
#     }

# })



print('*'*50)

arananogrenci = input('öğrenci no: ')
ogrenci = ogrenciler[arananogrenci]


print(f"Aramış olduğunuz {ogrNo} nolu öğrencinin adı: {ogrenci['adı']} soyadı: {ogrenci['soyadı']} ve telefonu da: {ogrenci['telefon']}")


