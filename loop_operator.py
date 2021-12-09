#####***range***########
# for items in range(50,100,20):
#     print(items)
# print(list(range(10,60,5)))

#####***enumerate***###### ---> *** enumerate() methodu itere edilebilir bir objenin(list, string, tuple vb) itemlarına 
#                               ***  birer index numarası verir.
# index = 0
# mesaj = "hello there"
# for harf in mesaj:
#     print(f"index {index} harf {harf}")
#     index+=1
                            ###Bu işlemi enumerate ile nasıl yaparım

# mesaj = "hello"
# for index , harf in enumerate(mesaj):
#     print(f"index {index} harf {harf}")
#           \     /
#            \   /
#             \ /
#              V  
#        index 0 harf h
#        index 1 harf e
#        index 2 harf l
#        index 3 harf l
#        index 4 harf o

# mesaj = "hello"
# for index  in enumerate(mesaj):
#     print(index)
#    \     /
#     \   /
#      \ /
#       V 
#    (0, 'h')
#    (1, 'e')
#    (2, 'l')
#    (3, 'l')
#    (4, 'o') 

#####***zip***######   ---> İki farklı listeyi tuple olarak birleştirme.

# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']
# list3 = [100,200,300,400,500]
# print(list(zip(list1, list2,list3)))

# for items in zip(list1, list2,list3):
#     print(items)
# for a,b,c in zip(list1, list2,list3):
#     print(a,b)









