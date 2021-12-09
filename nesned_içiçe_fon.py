# def greeting(name):
#     print("hello", name)

# greeting("ali")

# sayHello=greeting

# sayHello("OSman")

# del sayHello

# # sayHello("OSman")
# greeting("emre")

######**************  --------   ****************

### --------encapsulation--------

# def outer(num1):
#     print("outer")
#     def inner_increment(num1):
#         print("inner")
#         return num1 +1
#     num2=inner_increment(num1)
#     print(num1,num2)
# outer(10)
# inner_increment(10)# hata verrir çünkü kapsamı outer olan bir yerde tanımlanmamıştır.


#### -------------------------------------

# def factorial(number):
#     if not isinstance(number, int):
#         raise TypeError("sayı integer olamlı")
#     if not number >=0:
#         raise ValueError("sayı pozitif olmak zorunda")



#     def inner_factorial(number):
#         if number <= 1:
#             return 1
#         else:
#             return number*inner_factorial(number-1)
#     return inner_factorial(number)
# try:
#     print(factorial(5))
# except Exception as ex:
#     print(ex)






