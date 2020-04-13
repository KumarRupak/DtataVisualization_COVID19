import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;
Rupak=pd.read_csv("AgeGroupDetails.csv")
plt.plot(Rupak["AgeGroup"],Rupak["TotalCases"],marker="o",color="red",label="Cases")
plt.plot(Rupak["AgeGroup"],Rupak["gender"],marker="o",color="r")
b=plt.bar(Rupak["AgeGroup"],Rupak["TotalCases"],color="mediumspringgreen",label="Male")
plt.bar(Rupak["AgeGroup"],Rupak["gender"],color="deepskyblue",label="Female")
plt.xlabel("Age Groups")
plt.ylabel("No Of Cases")
b[9].set_color("b")
plt.title("COVID19-INDIA Age_Groups")
plt.legend()
plt.show()
