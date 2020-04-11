import matplotlib.pyplot as plt;
import pandas as pd
import numpy as np;
df=pd.read_csv('covd19_india.csv')
df=df[df.Date=='02/04/20']
df=df.sort_values(by=["Confirmed",'Deaths','Cured'],ascending=True)
confirm=df["Confirmed"]
death=df['Deaths']
cured=df['Cured']
states=df["State/UnionTerritory"]
plt.barh(states,confirm,label="Confirmed["+str(df["Confirmed"].sum())+"]")
plt.barh(states,cured,label="Cured["+str(df["Cured"].sum())+"]",color="y")
plt.barh(states,death,label="Death["+str(df["Deaths"].sum())+"]",color="r")
plt.legend()
plt.title("COVID-19  INDIA (BY RUPAK KUMAR PATRO)")
plt.xlabel("Cases")
plt.ylabel("States")
plt.show()
