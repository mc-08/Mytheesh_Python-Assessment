#Question 2:

def add(n):
    d = {'Square': lambda a : a**2, 
         'Cube': lambda a : a**3, 
         'Squareroot': lambda a : a**(1/2), 
         }
    sum = 0
    for key in d.keys():
        sum += d[key](n)
    return sum

#Get Input From user
x=int(input())
print(add(x))
