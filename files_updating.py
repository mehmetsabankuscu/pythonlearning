# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())


###*************** sayfa sonunda güncelleme********

# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nGüldane")
# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())

###************ sayfa başında güncelleme-*********


# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content="selim katan\n" + content
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())

##********** sayfa ortasında güncelleme*************

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     list = file.readlines()
#     list.insert(1,"hamza\n")
#     file.seek(0)
#     for i in list:
#         file.write(i)

# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())

#########************ vEYA ********

with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"hamza\n")
    file.seek(0)
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())




