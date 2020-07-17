import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
headers = ['#features','errorRMSE', 'featurename']
df = pd.read_csv('/home/john/Desktop/TP/tp3-metnum/notebooks/errorRSMLEvsFichurs.csv',names=headers)
print (df)

fig = plt.figure()
fig.suptitle('Variación error logarítmico')
# plt.tight_layout()

x = df['#features']
y = df['errorRMSE']
m = df['featurename']
n =[]
for txt in m:
    n.append("+" + txt)
plt.xlabel('features')
plt.ylabel('error RMSLE')
plt.xticks(x, n,rotation=90)
# plt.tight_layout()

# plot
plt.plot(x, y, '-gD', markevery=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
plt.tight_layout()

# beautify the x-labels
plt.savefig("RMSLE")
plt.show()
