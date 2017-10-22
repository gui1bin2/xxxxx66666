# -*- coding: utf-8 -*-


import pandas as pd

#导入原始数据
data = pd.read_excel('gui/2860.xlsx')
data = data.iloc[0:500,:]

帝国 = data[['rank','ID','帝国场','帝国MMR']][data.帝国场>0]
松鼠 = data[['rank','ID','松鼠场','松鼠MMR']][data.松鼠场>0]
北方 = data[['rank','ID','北方场','北方MMR']][data.北方场>0]
群岛 = data[['rank','ID','群岛场','群岛MMR']][data.群岛场>0]
怪物 = data[['rank','ID','怪物场','怪物MMR']][data.怪物场>0]

帝国 = data[['rank','ID','帝国场','帝国MMR']][data.帝国场>=20]
松鼠 = data[['rank','ID','松鼠场','松鼠MMR']][data.松鼠场>=20]
北方 = data[['rank','ID','北方场','北方MMR']][data.北方场>=20]
群岛 = data[['rank','ID','群岛场','群岛MMR']][data.群岛场>=20]
怪物 = data[['rank','ID','怪物场','怪物MMR']][data.怪物场>=20]

帝国 = data[['rank','ID','帝国场','帝国MMR']][data.帝国场>=100]
松鼠 = data[['rank','ID','松鼠场','松鼠MMR']][data.松鼠场>=100]
北方 = data[['rank','ID','北方场','北方MMR']][data.北方场>=100]
群岛 = data[['rank','ID','群岛场','群岛MMR']][data.群岛场>=100]
怪物 = data[['rank','ID','怪物场','怪物MMR']][data.怪物场>=100]

帝国 = data[['rank','ID','帝国场','帝国MMR']][data.帝国场>=20]
帝国 = 帝国[帝国.rank>=20]
松鼠 = data[['rank','ID','松鼠场','松鼠MMR']][data.松鼠场>=20]
北方 = data[['rank','ID','北方场','北方MMR']][data.北方场>=20]
群岛 = data[['rank','ID','群岛场','群岛MMR']][data.群岛场>=20]
怪物 = data[['rank','ID','怪物场','怪物MMR']][data.怪物场>=20]


帝国 = data[['rank','ID','帝国场','帝国MMR']][data.帝国MMR>=1300]
松鼠 = data[['rank','ID','松鼠场','松鼠MMR']][data.松鼠MMR>=1300]
北方 = data[['rank','ID','北方场','北方MMR']][data.北方MMR>=1300]
群岛 = data[['rank','ID','群岛场','群岛MMR']][data.群岛MMR>=1300]
怪物 = data[['rank','ID','怪物场','怪物MMR']][data.怪物MMR>=1300]

data1 = data[data.帝国MMR>=1300]
帝国均 = 帝国['帝国MMR'].mean(0)
a = 帝国['帝国场'].mean(0)
松鼠均 = 松鼠['松鼠MMR'].mean(0)
b = 松鼠['松鼠场'].mean(0)
北方均 = 北方['北方MMR'].mean(0)
c = 北方['北方场'].mean(0)
群岛均 = 群岛['群岛MMR'].mean(0)
d = 群岛['群岛场'].mean(0)
怪物均 = 怪物['怪物MMR'].mean(0)
e = 怪物['怪物场'].mean(0)


帝国.columns=['rank','ID','场数','MMR']
松鼠.columns=['rank','ID','场数','MMR']
北方.columns=['rank','ID','场数','MMR']
群岛.columns=['rank','ID','场数','MMR']
怪物.columns=['rank','ID','场数','MMR']
合计 = pd.concat([帝国,松鼠,北方,群岛,怪物])
x = 合计['MMR'].mean(0)

帝国胜率 = (a-(x-帝国均)/8)/(2*a)
松鼠胜率 = (b-(x-松鼠均)/8)/(2*b)
北方胜率 = (c-(x-北方均)/8)/(2*c)
群岛胜率 = (d-(x-群岛均)/8)/(2*d)
怪物胜率 = (e-(x-怪物均)/8)/(2*e)
print ('%.2f%%' %(帝国胜率*100))
print ('%.2f%%' %(松鼠胜率*100))
print ('%.2f%%' %(北方胜率*100))
print ('%.2f%%' %(群岛胜率*100))
print ('%.2f%%' %(怪物胜率*100))

帝国['帝国MMR'].size
松鼠['松鼠MMR'].size
北方['北方MMR'].size
群岛['群岛MMR'].size
怪物['怪物MMR'].size

帝国.sort(columns='帝国MMR',ascending=False)
怪物.sort(columns='怪物MMR',ascending=False)

松鼠 = 松鼠[data.松鼠MMR>=1243]
松鼠 = 松鼠.sort(columns='松鼠MMR',ascending=False)