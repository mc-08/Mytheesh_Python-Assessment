#Question 6:
nameList=['santa Maria','Hello World','Marry christmas','tHank You']
n1=[]
out=[]

for i in nameList:
  n1.append(i.split(' ')[0])
  n1.append(i.split(' ')[1])
    
for i in n1:
    if i[0].isupper():
      out.append(i)
    
print(out)
