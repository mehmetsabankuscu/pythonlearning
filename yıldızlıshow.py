
a = 1
satırsayısı=int(input("Satır Sayısı: "))
while a == 1:
    star = -1
    for i in range(satırsayısı):
        star += 2
        yıldız = star*"*"
        göster = yıldız.center(50," ")
        print (göster)
    
    for i in range(satırsayısı):
        star-=2
        yıldız = star*"*"
        göster = yıldız.center(50," ")
        print (göster)








