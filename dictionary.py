# key - value

# 41 => Kocaeli 34 => İstanbul


# sehirler = ['Kocaeli', 'İstanbul']
# plakalar = [41, 34]

# print(plakalar[sehirler.index('İstanbul')])
# print(plakalar[sehirler.index('Kocaeli')])


# print(plakalar['Kocaeli']) => 41
# print(plakalar['İstanbul']) => 34                       
                                                             
# plakalar = { 'Kocaeli' : 41, 'İstanbul' : 34}

# print(plakalar['Kocaeli'])
# print(plakalar['İstanbul'])

# plakalar['Ankara'] = 6                                #####dictionarylere listedeki gibi veriler eklenebilir. tuple da eklenmez
# plakalar['Kocaeli'] = 'new value'

# print (plakalar)

users = {
    'sadikturan':{
        'age': 36,
        'roles':['user'],
        'email': 'sadik@gmail.com',
        'address':'Kocaeli',
        'Phone': '1231321'

    },
    'cinarturan': {
        'age': 36,
        'roles':['admin','user'],
        'email': 'cinar@gmail.com',
        'address':'Kocaeli',
        'Phone': '1231321'
    }
}

# print(users['cinarturan']['age'])

# print(users['cinarturan']['email'])

# print(users['cinarturan']['address'])


print(users['cinarturan']['roles'][0])
