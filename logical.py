x = 12
hak = 0
devam = 'e'

result = 5 < x < 10 

#and

# True, True => True
# True, False => False
result = x>5 and x<10          # True, true => true
result = (hak > 0) and (devam == 'e')

#or

# True, False => True
# True, True => True
# False, False => True
result = (x>0) or  (x%2==0)

# not 

result = not (x>0)


# x, 5-10 arasında olan bir çift sayı mı?

((x>5)or(x<10))and(x%2==0)

print(result)