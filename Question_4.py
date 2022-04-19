#Question 4:
ls=['hello','hOw','Dear','ARe','You']
d=[]

for i in range(0,len(ls)):
    s=ls[i]
    if s[1].isupper():
        d.append(s)
print(d)
