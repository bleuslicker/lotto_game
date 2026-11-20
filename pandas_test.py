import pandas as pd
'''
df=pd.read_csv('lotto.csv',encoding='utf-8-sig')
print(df.shape)
print(df.head())


'''

votes=['짜장','짬뽕','짜장','볶음밥']

count={}
for menu in ['짜장','짬뽕','볶음밥']:
    count[menu]=0
for v in votes:
    count[v]+=1

print(count)
print(count['짜장'],sum(count.values()))