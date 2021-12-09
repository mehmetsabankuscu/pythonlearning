import math
import time

def zaman_hesapla(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon " + str(finish-start)+ "saniye sürdü.")
    return wrapper
@zaman_hesapla
def usalma(a,b):
    
    print(math.pow(a,b))

@zaman_hesapla
def factorial(num):
    
    print(math.factorial(num))

@zaman_hesapla
def toplam(a,b):
    print(a+b)

usalma(2,3)
factorial(80)
toplam(6,8)
