import os
from datetime import datetime

# result = dir(os)
# result = os.name # işletim sistemi adı

##### Dizin Değiştirme ******

# os.chdir("C:\\")             ### dosya konumu oluşturur..
# os.chdir('..')
# os.chdir('..')
##### veya ,tek satırda yapabilriz... 
# os.chdir('../..')

##### Klasör Oluşturma *******

os.mkdir("newdirectory.py")    ### newdirectory isimli dosyayı oluşturur.
# os.makedirs("C:\\newdirectory/yeniklasör/enyeni") #### NOT: ister oluşturmak istediğin dosyaları bu şekilde yaz ister ister os.chdir komutunu çalıştır. Böylelikle dosyayı hangi konumda oluşturmak istiyorsan oluşturmuş olursun.
# os.rename("newdirectory", "yeniklasör")
# os.rmdir("newdirectory") ### var olan dosyayı siler..
# os.removedirs("yeniklasör/yeniklasör/enyeni")

##### Listeleme

# result = os.listdir()
# result = os.listdir("C:\\")

# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)

##### Etkin Dizin Oluşturma *******
# result = os.getcwd() # "modul_os.py" dosya konumunu soyler.

# result = os.stat("modul_datetime.py")
# result = result.st_size/1024
# result= result.st_ctime
# result= datetime.fromtimestamp(result.st_ctime) # Oluşturulma tarihi 
# result= datetime.fromtimestamp(result.st_atime) # Son erişilme tarihi
# result= datetime.fromtimestamp(result.st_mtime) # Değiştirilme tarihi

# os.system("notepad.exe")

###### path

# result = os.path.abspath("asal_sayı.py")
# result = os.path.dirname("C:/Users/MEHMET ŞABAN KUŞÇU/Desktop/python_temelleri/asal_sayı.py")
# result = os.path.dirname(os.path.abspath("asal_sayı.py")) # mantıklı kullanımı bu şekilde
# result = os.path.exists("asal_sayı.py")
# result = os.path.isdir("C:/Users/MEHMET ŞABAN KUŞÇU/Desktop/python_temelleri/asal_sayı.py")
# result = os.path.isfile("C:/Users/MEHMET ŞABAN KUŞÇU/Desktop/python_temelleri/asal_sayı.py")

# result = os.path.join("C:\\","deneme","deneme1")
# result = os.path.split("C:\deneme\deneme1")
# result = os.path.splitext("asal_sayı.py")
# result = result[0]
# result = result[1]
# print(result)





