import pandas

df1=pandas.read_csv('n1_trucks.csv')
hourwise=[]
for i in df1['hour'].unique():
    hourwise.append(df1.loc[df1['hour']==i])

y=hourwise[90]['number']
print(y)