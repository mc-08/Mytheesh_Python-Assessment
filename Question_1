#Question 1:
positive=['good','best','awesome','nice']
negative=['worst','awful']
p=[]
n=[]
comments=['He is good boy','Food is worst here','He is an awesome player','She is the best','The pizza tastes awful','These burgers are really nice']

#Segregation
for j in range(0,1):    
    for i in range(0,len(comments)):
        if positive[j] in comments[i] or positive[j+1] in comments[i] or positive[j+2] in comments[i] or positive[j+3] in comments[i]:
            p.append(comments[i])
        elif negative[j] in comments[i] or negative[j+1] in comments[i]:
            n.append(comments[i])
            
#Positive Sentiments-display
print("Positive:\n",p)

#Negative Sentiments-display
print("Negative:\n",n)
