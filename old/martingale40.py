'''
martingale.py 4.0
<INTRODUCTION>
投資法「マーチンゲール」実践
1/2の確率で勝負するゲーム(たとえば表裏当てコインゲーム)
基本掛け金1
資産から掛け金を引く
買ったら
	掛け金の倍額もらう
	掛け金を基本賭け金に戻す
負けたら
	掛け金は戻らない
	次の掛け金を倍にする
資産がなくなるか、ゲーム回数が100超えたら終了
<USAGE>
Just build.
<UPDATE4.0>
収益をリスト'profitListに格納し'plotする
'''
import numpy as np
# from scipy import stats
# from scipy import optimize
import matplotlib.pyplot as plt
from pandas import *
import random
def game(x):
	if random.random()>0.5:
		# print('Win! I got', 2*x, 'and I\'ll bet 1 next time.' )
		return 1
	else:
		# print('Lose! I lost', x, 'and I\'ll bet', 2*x ,'next time.')
		x+=x
		return x

'''__MAIN__________________________'''
for asset in range(10,100,10):
	'''__RESET VALUES__________________________'''
	assetDefault=asset
	bet,gnum,win=1,0,0
	gnumList,assetList,profitList=[],[],[]
	while asset>bet:
		# print('\n____________________________')

		gnum+=1
		gnumList.append(gnum)
		# print('Game times:',gnum)

		asset-=bet
		# print('Bet:',bet)

		result=game(bet)
		if result==1:
			win+=1
			asset+=2*bet
		bet=result
		assetList.append(asset)
		profitList.append(asset-assetDefault)
		# print('Asset:', asset)
		if gnum>100 : break

	'''__RESULT__________________________'''
	print('\n____________________________')
	print('Default asset:',assetDefault)
	print('Game times:', gnum)
	print('Win rate:', win/gnum)
	print('Profit:', asset-assetDefault)
	# print(gnumList,assetList)

	plt.plot(gnumList,profitList,'-',label=assetDefault)


	# plotplot(gnumList,assetList,'-',label=assetDefault)
	# ax2 = ax1.twinx()
	# ax2.plot(gnumList,profitList,label=assetDefault)

	# fig, ax1 = plt.subplots()
	# ax1.plot(gnumList,assetList,'-',label=assetDefault)
	# ax2 = ax1.twinx()
	# ax2.plot(gnumList,profitList,label=assetDefault)

'''__PLOT SETTING__________________________'''
plt.legend(loc='best',fancybox=True,fontsize='small')
plt.xlabel('Game times')
plt.ylabel('Asset')
plt.grid(True)
plt.show()
