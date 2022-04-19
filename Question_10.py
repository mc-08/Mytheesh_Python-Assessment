#Question 10:
import datetime

d=['17-12-1997','22-04-2011','01-05-1993','19-06-2020']
l=[]

for i in d:
    date = datetime.datetime.strptime(i, "%d-%m-%Y")
    l.append(str(date.year))
print(l)
