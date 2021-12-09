# Dosya açmak ve oluşturmk için open() fonksiyonu ullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w":(write) yazma modu. Dosyayı konumda oluşturur.
#   **Dosyayı konumda oluşturur.
#   **Dosya içeriğini siler ve yeniden ekleme yapar.
# file = open("newfile.txt","w")
# file = open("C:/Users/MEHMET ŞABAN KUŞÇU/Desktop/newfile.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding='utf-8')
# file.write("mehmetşabankuşçu")
# file.close()


# "a":(append) ekleme. Dosya konumda yoksa oluşturur.

# file = open("newfile.txt","a",encoding='utf-8')
# file.write("mehmetşabankuşçu\n")
# file.close()



# "x":(create) oluşturma. Dosya zaten varsa hata verir.

file = open("newfile2.txt","x",encoding='utf-8')




# "r":(read) okuma. Varsayılan. Dosya konumda yoksa hata verir.