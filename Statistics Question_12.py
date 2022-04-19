#Question 12:
import pandas as pd
import numpy as np

City = ["New York", "New Jersey", "Michigan", "California", "Florida", "Massachusetts", "Texas"]
No_of_deaths_in_last_month = [3406, 1469, 662, 583, 582, 526, 461]
No_of_deaths_in_current_month = [4398, 1846, 1288, 382, 879, 430, 321]
df = pd.DataFrame({"City": City, "No_of_deaths_in_last_month":No_of_deaths_in_last_month, "No_of_deaths_in_current_month": No_of_deaths_in_current_month})
print(df)

pred=[]
signi=[]

for i in No_of_deaths_in_last_month:
    pred.append((0.30*i)+i)
    signi.append(0.1*i)
print("Predicted_scientist",pred)
print("Actual death value ",No_of_deaths_in_current_month)


#difference between Actual and predicted

n_pred=np.array(pred)
n_No_of_deaths_in_current_month=np.array(No_of_deaths_in_current_month)

diff=np.absolute(n_No_of_deaths_in_current_month-n_pred)

print("Difference b/w Predicted and Current",diff)
print("Signicance as 0.1",signi)
