from datetime import datetime
from datetime import timedelta


simdi = datetime.now()
simdi = datetime.today()
result = datetime.now().year
# result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second
result = datetime.ctime(simdi)
result = datetime.strftime(simdi,"%Y")
result = datetime.strftime(simdi,"%X")

result = datetime.strftime(simdi,"%d")
result = datetime.strftime(simdi,"%A")
result = datetime.strftime(simdi,"%B")
result = datetime.strftime(simdi,"%Y %B %A")

t = "21 April 2021 hour 10:12:30"
result = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
result = result.hour



birthday = datetime(1983,5,9,12,30,10)
# print(birthday)
result = datetime.timestamp(birthday)# saniye 
result = datetime.fromtimestamp(result) # saniyeden datetime'a
result = datetime.fromtimestamp(0) ### Bilgisayarların milat tarihi "1970-01-01 03:00:00"


result = simdi - birthday # timedelta
# result=result.days
# result = result.seconds
result = result.microseconds

print(simdi)

# result = simdi + timedelta(days=10)
result = simdi + timedelta(days=730, minutes=10)


print(result)








