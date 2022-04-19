#Question 8:
import itertools as it

a= [9,8,7,6,5]
l=[]

l = it.accumulate(list(enumerate(a)), lambda x,y: (y[0], (x[1]*(x[0]+1) + y[1])/(y[0]+1)))
print(list(map(lambda x: x[1], l)))
