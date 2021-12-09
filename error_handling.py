# error handling => hata yönetimi
# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)

# except ZeroDivisionError
#     print('y için 0 girilmez')
# except ValueError
#     print('x ve y için sayısal değer girmelisiniz')


# except (ZeroDivisionError,ValueError):
#     print('yanlış bilgi girdiniz')

# except (ZeroDivisionError,ValueError) as e :
#     print('yanlış bilgi girdiniz')
#     print(e)

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except :
#     print('yanlış bilgi girdiniz')
# else:
#     print('herşey yolunda')




while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as ex:
        print('yanlış bilgi girdiniz',ex)   ##### Burası en pratik kullanım eğer hata ayıklanacaksa bu yöntem on numara ...

    else:
        print('herşey yolunda')
        break

    finally:
        print('try except sonlandı')   ### Yanlış da olsa doğru da olsa her türlü bu çalışır.