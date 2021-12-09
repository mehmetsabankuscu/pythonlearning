import re

# result = dir(re)
# re module


str = "Python Kursu: Python Programlama Rehberi | 40 saat"

#####*******   re.findall()
result = re.findall("Python",str)   ### str içerisindeki python yazılarını bul
result = len(result)

#####*******   re.split()
result = re.split(" ", str)
result = re.split("R", str)
 
#####*******   re.sub()
result = re.sub("r","p",str)  ###  str içerisindeki 'r' leri 'p' lerle değiştir.
result = re.sub(" ","-",str)   ### boşluk yerine '-' koy.
result = re.sub("\s","-",str)   ### bir önceki ile aynı şeyi ifade ediyor...

#####*******   re.search()

result = re.search("Python",str)  # ilk Pytgon yazısı hakkında match döndürür ..
# result = result.span()  # kaçıncı indexlerde olduğu
# result = result.start() # kaçıncı indexden başladığı
# result = result.end()   # kaçıncı indexte bittiği
# result = result.group()  # aranan string ifamin kendisini
# result = result.string  # aranan ifadenin bulunduğu string ifadenin tamamını gönderiri.



#####*******  REGULAR EXPRESSİON

"""
[] - Köşeli parantezler arasına ayzılan karakterler aranır.

    [abc] => a      : 1 match
             ac     : 2 match
             Python : No matches

    [a-e]  => [abcde]
    [1-5]  => [12345]
    [0-39] => [01239]

    [^abc] => abc dışındaki karakterler.
    [^0-9] => rakam olmayan karakterler.


"""
result = re.findall("[abc]",str)
result = re.findall("[sat]",str)
result = re.findall("[a-e]",str)
result = re.findall("[a-z]",str)
result = re.findall("[0-5]",str)
result = re.findall("[^abc]",str)
result = re.findall("[^0-9]",str)


"""
. - Herhangi bir tek karakteri belirtir.

    .. =>a      : No match
         ab     : 1 match
         abc    : 1 match
         abcd   : 2 matches

"""
result = re.findall("...",str)
result = re.findall("Py..on",str)


"""
^ -Belirtilen string ^ ifadesinden sonra belirtilen karakterlerle başlıyor mu ?

    ^a => a      : 1 match
          abc    : 1 match
          bac    : No match

"""
result = re.findall("^P",str)

"""
^ -Belirtilen string $ ifadesinden önce belirtilen karakterlerle bitiyor mu ?

    a$ => a         : 1 match
          lamba     : 1 match
          Python    : No match

"""
result = re.findall("t$",str)
result = re.findall("saat$",str)
result = re.findall("saatt$",str)

"""
* - Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.

    ma*n => mn      : 1 match
            man     : 1 match
            maan    : 1 match
            main    : No match (a' nın arakasına n gelmiyor.)
 
"""

result = re.findall("sa*t",str)

"""
+ - Bir karakterin sıfır  ya da daha fazla sayıda olmasını kontrol eder.

    ma+n => mn      : No match
            man     : 1 match
            maan    : 1 match
            main    : No match (a' nın arakasına n gelmiyor.)
 
"""
result = re.findall("sa+t",str)

"""
? - Bir karakterin sıfır  ya da bir kez olmasını kontrol eder.

    ma?n => mn      : No match
            man     : 1 match
            maan    : 1 match
            main    : No match (a' nın arakasına n gelmiyor.)
 
"""
result = re.findall("sa?t",str)


"""
{} - Karakter sayısını kontrol eder.

    al{2}   => a karakterinin arkasına 'l' karakteri 2 kez takrarlamalı.
    al{2,3} => a karakterinin arkasına 'l' karakteri en az 2 en fazla 3 kez tekrarlanmalı.
    [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.

"""
result = re.findall("a{2}", str)
result = re.findall("[0-9]{2}", str)


"""
 | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.

    a|b => a ya da b

        cde     =>   No match
        ade     =>   1 match
        acdbea  =>   3 match


"""

"""
() - Gruplama yapmak için kullanılır.

    (a|b|c)xz => a,b,c karaketrlerinin arkasına xz gelmelidir.

"""

"""
\ - Özel karakterleri aramamızı sağlar.

    \$ => $ karakterinin arkasına a karakterini arar.yani
          $ regular exp. engine tarafından yorumlanmaz.

    \A - Belirtilen akrakter string'in başında mı? 
         \Athe => the string'in başında mı?

    \Z - Belirtilen karakter string'in sonunda mı?
         the\Z => the stringin sonunda mı?

result = re.findall("\APython",str)
result = re.findall("saat\Z",str)


    \b - Belirtilen karekter kelimenin başında ya da sonunda mı?
         \bthe => the kelimenin başında mı?
         the\b => the kelimenin sonunda mı?
        
    \B - Belirtilen karekter kelimenin başında ya da sonunda değil mı?
         \Bthe => the kelimenin başında değil mı?
         the\B => the kelimenin sonunda değil mı?
    
    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
        \d => 12abc34
    
    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
        \D => 1ab44_50
    
    \s - Boşluk karakterlerini arar.
    \S - Boşluk karakterleri dışındakiler.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi



"""




print (result)