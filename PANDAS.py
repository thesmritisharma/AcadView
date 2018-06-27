'''
#QUESTION 1
import pandas as pd
data = {'Name':['Tom'],'Age':[28], 'Mail ID':['smriti7545@gmail.com'],'Phone':[9996308548]}
df = pd.DataFrame(data)
df.loc[4]=['Lala', 24, 'lala@gmail.com', 9876545678]
print(df)
'''

#QUESTION 2
import pandas as pd
df=pd.read_csv(r'C:\Users\smrit\Downloads\weather.csv', header = None)
print(df.head(6))

print(df.head(11))

print(df.tail(5))


print(df.values)