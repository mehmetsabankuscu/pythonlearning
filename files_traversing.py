# file = open("newfile.txt","r",encoding="utf-8")
# content = file.read()
# print(content)
# file.close()

############# VEYA *************
with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read(5)
    print(content)
    file.seek(2)        #### kürsörü istediğin konuma atar.
    print(file.tell())  #### kürsörün konumunu verir.
    content2=file.read()
    print(content2)