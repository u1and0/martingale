'''
##martingale.py 5.0
__UPDATE5.0__
関数の整理  
初期資産10で動くようにした  

標準出力に以下を出力する  
* 100回分のゲーム結果
* 最終資産のリスト(100要素)
* 勝率(ゲーム数=100回平均)


__UPDATE4.1__
関数に分割
# 同じ初期資産を100回計算させて、収益のリストprofitListを得る

__INTRODUCTION__
投資法「マーチンゲール」
1/2の確率で勝負するゲーム(たとえば表裏当てコインゲーム)のシミューレーション

__USAGE__
Just build.

__ACTION__
基本掛け金1
資産から掛け金を引く
買ったら
	掛け金の倍額もらう
	掛け金を基本賭け金に戻す
負けたら
	掛け金は戻らない
	次の掛け金を倍にする
資産がなくなるか、ゲーム回数が*n*回超えたら終了

__PLAN__
初期資産を変えて最も効率の良い「初期資産/掛け金の割合」を見つける
pyplot使って可視化
yield使ったほうがよいんではないかい？

'''
# from scipy import stats
# from scipy import optimize



def game(x):
	'''
	勝ったら掛け金を1に戻す
	負けたら倍額の掛け金を戻す
	'''
	import random
	if random.random()>0.5:
		# print('Win! I got', 2*x, 'and I\'ll bet 1 next time.' )
		return 1
	else:
		# print('Lose! I lost', x, 'and I\'ll bet', 2*x ,'next time.')
		x+=x
		return x




def play(asset):
	'''初期試算を超えるか、ゲーム回数が100超えるまでプレイ
	勝ちゲーム数、継続ゲーム数、勝率(勝ちゲーム数/継続ゲーム数=0.5に近くなるはず)をprint
	戻り値
		asset:最終資産
		win/gnum:勝率
		profitList:収益曲線
		assetList:資産曲線
	最終資産と勝率を返す'''
	gnum,win,bet=0,0,1
	profitList,assetList=[],[]
	defaultAsset=asset
	while asset>bet:
		gnum+=1
		asset-=bet
		'''__ゲーム結果の集計__________________________'''
		result=game(bet)    #結果
		if result==1:    #勝利なら1に戻っているはず
			win+=1
			asset+=2*bet
		bet=result    #次回の掛け金
		'''__資産と収益の記録__________________________'''
		assetList.append(asset)
		profitList.append(result)   #収益曲線
		if gnum>100 : break
	print('Win game:',win)
	print('Game streak:',gnum)
	# print('Win ratio:', win/gnum)
	# print('Profit curve',profitList)
	# plotter(defaultAsset,profitList,assetList)
	return (asset,win/gnum)


# from pandas import *
# def plotter(assetDefault,profitList,assetList):
# 	import matplotlib.pyplot as plt
# 	'''収益曲線(profitList)と資産曲線(assetList)を描画する'''
# 	xaxis=range(len(profitList))
# 	lbl='Default Asset '+str(assetDefault)

# 	plt.plot(xaxis,profitList,'-',label=lbl)

# 	fig, ax1 = plt.subplots()
# 	ax1.plot(xaxis,assetList,'-',label=lbl)
# 	ax2 = ax1.twinx()
# 	ax2.plot(xaxis,profitList,label=lbl)

# 	plt.plot(xaxis,assetList,'-',label=lbl)
# 	ax2 = ax1.twinx()
# 	ax2.plot(xaxis,profitList,label=lbl)


# 	'''__PLOT SETTING__________________________'''
# 	plt.legend(loc='best',fancybox=True,fontsize='small')
# 	plt.xlabel('Game streak')
# 	plt.ylabel('Asset')
# 	plt.grid(True)
# 	plt.show()






# def www(low,high,term):
	# for asset in range(low,high,term):
	# '''初期資産をlow~highまでtermずつ増やしていく'''
	# '''__RESET VALUES__________________________'''
	# '''各値をリセットする'''
	# assetDefault=asset
	# bet,gnum,win=1,0,0
	# gnumList,assetList,profitList=[],[],[]
	# profit_tryList,winrate_tryList=[],[]
	# for i in range(0,100):
	# 	play()
	# # return asset
	# return 



# __MAIN__________________________
'''統計的に見たいから、何度も初期資産から初めて勝率見極める'''
'''__SET DEFAULT ARGUMENTS__________________________'''
defaultAsset=10
# low,high,term=10,110,10
# for defaultAsset in range(low,high,term):
# profit_tryList,winrate_tryList=[],[]
finalAssset,winRate=[],[]


print('__Game start! Your default asset is',defaultAsset,'____________')
for i in range(1,101):    #100回プレイ
	print('\nTake:',i)
	x=play(defaultAsset)
	finalAssset.append(x[0])
	winRate.append(x[1])
import numpy as np
print('Final Asset:', finalAssset, 'Win ratio:', np.mean(winRate))


		# profit_tryList.append(asset-assetDefault)   #最終的な利益をprofit_tryListに追加する
		# winrate_tryList.append(win/gnum)   #勝率をwinrate_tryListに追加する



'''__RESULT__________________________'''
# print('\n____________________________')
# print('Default asset:',assetDefault)
# # print('Game times:', gnum)
# print('Win rate List:', winrate_tryList)
# print('Profit List:', profit_tryList)
# import numpy as np
# winrateAve=np.mean(winrate_tryList)
# profitAve=np.mean(profit_tryList)
# print('Win rate:', winrateAve)
# print('Profit:', profitAve)
# print(gnumList,assetList)





'''
バグ症状
勝率固定
収益の無限増加、または収益の固定
どこかでハンチングが起きている
ループ前に値のリセットをかけるべし
____________________________
Default asset: 10
Win rate List: [0.4, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333]
Profit List: [-5, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Win rate: 0.334
Profit: -0.13

____________________________
Default asset: 20
Win rate List: [0.2857142857142857, 0.504950495049505, 0.5098039215686274, 0.5145631067961165, 0.5096153846153846, 0.5142857142857142, 0.5188679245283019, 0.514018691588785, 0.5092592592592593, 0.5045871559633027, 0.509090909090909, 0.5135135135135135, 0.5178571428571429, 0.5132743362831859, 0.5087719298245614, 0.5043478260869565, 0.5086206896551724, 0.5128205128205128, 0.5084745762711864, 0.5042016806722689, 0.5, 0.5041322314049587, 0.5081967213114754, 0.5040650406504065, 0.5, 0.496, 0.49206349206349204, 0.49606299212598426, 0.4921875, 0.49612403100775193, 0.49230769230769234, 0.48854961832061067, 0.49242424242424243, 0.49624060150375937, 0.4925373134328358, 0.4888888888888889, 0.49264705882352944, 0.49635036496350365, 0.5, 0.5035971223021583, 0.5, 0.49645390070921985, 0.49295774647887325, 0.48951048951048953, 0.4930555555555556, 0.496551724137931, 0.4931506849315068, 0.4897959183673469, 0.4864864864864865, 0.48322147651006714, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48]
Profit List: [-13, 64, 1, 1, -1, 2, 1, -1, -2, -4, 8, 1, 1, -1, -2, -4, 8, 1, -1, -2, -4, 8, 1, -1, -2, -4, -8, 16, -1, 2, -1, -2, 4, 1, -1, -2, 4, 1, 1, 1, -1, -2, -4, -8, 16, 1, -1, -2, -4, -8, -16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Win rate: 0.488401979507
Profit: 0.41

____________________________
Default asset: 30
Win rate List: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Profit List: [-15, -16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Win rate: 0.0
Profit: -0.31

____________________________
Default asset: 40
Win rate List: [0.46534653465346537, 0.47058823529411764, 0.47572815533980584, 0.47115384615384615, 0.4666666666666667, 0.4716981132075472, 0.4672897196261682, 0.4722222222222222, 0.46788990825688076, 0.4636363636363636, 0.4594594594594595, 0.45535714285714285, 0.45132743362831856, 0.45614035087719296, 0.4608695652173913, 0.45689655172413796, 0.46153846153846156, 0.4661016949152542, 0.47058823529411764, 0.4666666666666667, 0.4628099173553719, 0.45901639344262296, 0.45528455284552843, 0.4596774193548387, 0.456, 0.4523809523809524, 0.44881889763779526, 0.4453125, 0.4418604651162791, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846, 0.43846153846153846]
Profit List: [46, 2, 1, -1, -2, 4, -1, 2, -1, -2, -4, -8, -16, 32, 1, -1, 2, 1, 1, -1, -2, -4, -8, 16, -1, -2, -4, -8, -16, -32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Win rate: 0.445090956561
Profit: -0.06

____________________________
Default asset: 50
Win rate List: [0.4444444444444444, 0.42574257425742573, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804, 0.4215686274509804]
Profit List: [-19, 31, -32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Win rate: 0.421839125089
Profit: -0.2

____________________________
Default asset: 60
Win rate List: [0.5247524752475248, 0.5294117647058824, 0.5242718446601942, 0.5288461538461539, 0.5333333333333333, 0.5283018867924528, 0.5233644859813084, 0.5185185185185185, 0.5137614678899083, 0.509090909090909, 0.5135135135135135, 0.5089285714285714, 0.5132743362831859, 0.5087719298245614, 0.5130434782608696, 0.5086206896551724, 0.5042735042735043, 0.5, 0.5042016806722689, 0.5, 0.5041322314049587, 0.5081967213114754, 0.5121951219512195, 0.5161290322580645, 0.512, 0.5158730158730159, 0.5196850393700787, 0.515625, 0.5193798449612403, 0.5230769230769231, 0.5190839694656488, 0.5151515151515151, 0.5112781954887218, 0.5074626865671642, 0.5111111111111111, 0.5147058823529411, 0.5109489051094891, 0.5144927536231884, 0.5107913669064749, 0.5071428571428571, 0.5035460992907801, 0.5, 0.4965034965034965, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556, 0.4930555555555556]
Profit List: [53, 1, -1, 2, 1, -1, -2, -4, -8, -16, 32, -1, 2, -1, 2, -1, -2, -4, 8, -1, 2, 1, 1, 1, -1, 2, 1, -1, 2, 1, -1, -2, -4, -8, 16, 1, -1, 2, -1, -2, -4, -8, -16, -32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Win rate: 0.501809589796
Profit: 0.08

____________________________
Default asset: 70
Win rate List: [0.5643564356435643, 0.5588235294117647, 0.5631067961165048, 0.5673076923076923, 0.5714285714285714, 0.5660377358490566, 0.5700934579439252, 0.5740740740740741, 0.5688073394495413, 0.5636363636363636, 0.5585585585585585, 0.5535714285714286, 0.5486725663716814, 0.543859649122807, 0.5478260869565217, 0.5517241379310345, 0.5470085470085471, 0.5423728813559322, 0.5378151260504201, 0.5333333333333333, 0.5371900826446281, 0.5327868852459017, 0.5365853658536586, 0.5403225806451613, 0.544, 0.5476190476190477, 0.5511811023622047, 0.546875, 0.5503875968992248, 0.5538461538461539, 0.5572519083969466, 0.5606060606060606, 0.556390977443609, 0.5597014925373134, 0.5555555555555556, 0.5588235294117647, 0.5620437956204379, 0.5652173913043478, 0.5683453237410072, 0.5714285714285714, 0.574468085106383, 0.5774647887323944, 0.5804195804195804, 0.5833333333333334, 0.5862068965517241, 0.5821917808219178, 0.5850340136054422, 0.5878378378378378, 0.5906040268456376, 0.5933333333333334, 0.5960264900662252, 0.5921052631578947, 0.5947712418300654, 0.5909090909090909, 0.5870967741935483, 0.5833333333333334, 0.5859872611464968, 0.5822784810126582, 0.5849056603773585, 0.58125, 0.577639751552795, 0.5802469135802469, 0.5766871165644172, 0.573170731707317, 0.5757575757575758, 0.5783132530120482, 0.5808383233532934, 0.5773809523809523, 0.5798816568047337, 0.5764705882352941, 0.5789473684210527, 0.5813953488372093, 0.5838150289017341, 0.5804597701149425, 0.5771428571428572, 0.5795454545454546, 0.576271186440678, 0.5786516853932584, 0.5754189944134078, 0.5777777777777777, 0.574585635359116, 0.5769230769230769, 0.5737704918032787, 0.5760869565217391, 0.572972972972973, 0.5698924731182796, 0.5668449197860963, 0.5638297872340425, 0.5608465608465608, 0.5631578947368421, 0.5654450261780105, 0.5625, 0.5595854922279793, 0.5618556701030928, 0.558974358974359, 0.5612244897959183, 0.5583756345177665, 0.5606060606060606, 0.5628140703517588, 0.565]
Profit List: [57, -1, 2, 1, 1, -1, 2, 1, -1, -2, -4, -8, -16, -32, 64, 1, -1, -2, -4, -8, 16, -1, 2, 1, 1, 1, 1, -1, 2, 1, 1, 1, -1, 2, -1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 2, 1, 1, 1, 1, -1, 2, -1, -2, -4, 8, -1, 2, -1, -2, 4, -1, -2, 4, 1, 1, -1, 2, -1, 2, 1, 1, -1, -2, 4, -1, 2, -1, 2, -1, 2, -1, 2, -1, -2, -4, -8, -16, 32, 1, -1, -2, 4, -1, 2, -1, 2, 1, 1]
Win rate: 0.567892339119
Profit: 1.13

____________________________
Default asset: 80
Win rate List: [0.39285714285714285, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862, 0.3793103448275862]
Profit List: [-52, -64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Win rate: 0.379445812808
Profit: -1.16

____________________________
Default asset: 90
Win rate List: [0.49504950495049505, 0.49019607843137253, 0.4854368932038835, 0.4807692307692308, 0.4857142857142857, 0.49056603773584906, 0.4953271028037383, 0.49074074074074076, 0.48623853211009177, 0.4818181818181818, 0.4774774774774775, 0.4732142857142857, 0.4778761061946903, 0.47368421052631576, 0.4782608695652174, 0.47413793103448276, 0.4700854700854701, 0.4745762711864407, 0.47058823529411764, 0.475, 0.4793388429752066, 0.47540983606557374, 0.4796747967479675, 0.47580645161290325, 0.472, 0.46825396825396826, 0.4645669291338583, 0.4609375, 0.4573643410852713, 0.46153846153846156, 0.46564885496183206, 0.4696969696969697, 0.47368421052631576, 0.47761194029850745, 0.4740740740740741, 0.47794117647058826, 0.48175182481751827, 0.4782608695652174, 0.48201438848920863, 0.4785714285714286, 0.475177304964539, 0.4788732394366197, 0.4755244755244755, 0.4722222222222222, 0.47586206896551725, 0.4726027397260274, 0.46938775510204084, 0.47297297297297297, 0.4697986577181208, 0.47333333333333333, 0.4768211920529801, 0.47368421052631576, 0.47058823529411764, 0.4675324675324675, 0.47096774193548385, 0.46794871794871795, 0.46496815286624205, 0.46835443037974683, 0.4716981132075472, 0.46875, 0.4720496894409938, 0.4691358024691358, 0.4723926380368098, 0.4695121951219512, 0.4666666666666667, 0.463855421686747, 0.46107784431137727, 0.4583333333333333, 0.46153846153846156, 0.4588235294117647, 0.4619883040935672, 0.46511627906976744, 0.4624277456647399, 0.45977011494252873, 0.46285714285714286, 0.4659090909090909, 0.4689265536723164, 0.46629213483146065, 0.46368715083798884, 0.4666666666666667, 0.4696132596685083, 0.4725274725274725, 0.47540983606557374, 0.47282608695652173, 0.4702702702702703, 0.46774193548387094, 0.47058823529411764, 0.46808510638297873, 0.4708994708994709, 0.46842105263157896, 0.46596858638743455, 0.46875, 0.47150259067357514, 0.4742268041237113, 0.47692307692307695, 0.47959183673469385, 0.48223350253807107, 0.4797979797979798, 0.47738693467336685, 0.475]
Profit List: [47, -4, -8, -16, 32, 1, 1, -1, -2, -4, -8, -16, 32, -1, 2, -1, -2, 4, -1, 2, 1, -1, 2, -1, -2, -4, -8, -16, -32, 64, 1, 1, 1, 1, -1, 2, 1, -1, 2, -1, -2, 4, -1, -2, 4, -1, -2, 4, -1, 2, 1, -1, -2, -4, 8, -1, -2, 4, 1, -1, 2, -1, 2, -1, -2, -4, -8, -16, 32, -1, 2, 1, -1, -2, 4, 1, 1, -1, -2, 4, 1, 1, 1, -1, -2, -4, 8, -1, 2, -1, -2, 4, 1, 1, 1, 1, 1, -1, -2, -4]
Win rate: 0.472727631455
Profit: 0.88

____________________________
Default asset: 100
Win rate List: [0.5346534653465347, 0.5392156862745098, 0.5436893203883495, 0.5480769230769231, 0.5428571428571428, 0.5471698113207547, 0.5514018691588785, 0.5555555555555556, 0.5504587155963303, 0.5545454545454546, 0.5495495495495496, 0.5446428571428571, 0.5398230088495575, 0.543859649122807, 0.5478260869565217, 0.5431034482758621, 0.5470085470085471, 0.5508474576271186, 0.5546218487394958, 0.55, 0.5537190082644629, 0.5573770491803278, 0.5609756097560976, 0.5564516129032258, 0.552, 0.5555555555555556, 0.5590551181102362, 0.5625, 0.5658914728682171, 0.5692307692307692, 0.5725190839694656, 0.5681818181818182, 0.5639097744360902, 0.5597014925373134, 0.5555555555555556, 0.5514705882352942, 0.5547445255474452, 0.5507246376811594, 0.5539568345323741, 0.5571428571428572, 0.5602836879432624, 0.5563380281690141, 0.5524475524475524, 0.5555555555555556, 0.5586206896551724, 0.5616438356164384, 0.564625850340136, 0.5675675675675675, 0.5704697986577181, 0.5666666666666667, 0.5695364238410596, 0.5723684210526315, 0.5686274509803921, 0.564935064935065, 0.5612903225806452, 0.5641025641025641, 0.5605095541401274, 0.5632911392405063, 0.5660377358490566, 0.5625, 0.5652173913043478, 0.5617283950617284, 0.5644171779141104, 0.5670731707317073, 0.5696969696969697, 0.5662650602409639, 0.5688622754491018, 0.5714285714285714, 0.5739644970414202, 0.5705882352941176, 0.5672514619883041, 0.563953488372093, 0.5606936416184971, 0.5632183908045977, 0.56, 0.5625, 0.559322033898305, 0.5617977528089888, 0.5586592178770949, 0.5611111111111111, 0.56353591160221, 0.5604395604395604, 0.5573770491803278, 0.5597826086956522, 0.5621621621621622, 0.5645161290322581, 0.5614973262032086, 0.5585106382978723, 0.5555555555555556, 0.5526315789473685, 0.5549738219895288, 0.5520833333333334, 0.5492227979274611, 0.5515463917525774, 0.5538461538461539, 0.5510204081632653, 0.5482233502538071, 0.5505050505050505, 0.5477386934673367, 0.55]
Profit List: [47, 8, 1, 1, -1, 2, 1, 1, -1, 2, -1, -2, -4, 8, 1, -1, 2, 1, 1, -1, 2, 1, 1, -1, -2, 4, 1, 1, 1, 1, 1, -1, -2, -4, -8, -16, 32, -1, 2, 1, 1, -1, -2, 4, 1, 1, 1, 1, 1, -1, 2, 1, -1, -2, -4, 8, -1, 2, 1, -1, 2, -1, 2, 1, 1, -1, 2, 1, 1, -1, -2, -4, -8, 16, -1, 2, -1, 2, -1, 2, 1, -1, -2, 4, 1, 1, -1, -2, -4, -8, 16, -1, -2, 4, 1, -1, -2, 4, -1, 2]
Win rate: 0.557899050344
Profit: 1.1
[Finished in 2.1s]
'''