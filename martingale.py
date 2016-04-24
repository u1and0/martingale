'''
## martingale.py 5.2

__UPDATE5.2__

* 関数playのbreak条件
	* "100回プレイしたら"==>"資産が初期資産の10倍になったら"に変更
	* 何倍で脱出するのがいいんですかね
	* ある程度溜まったら口座からひきおろしたいから、その条件を次のバージョンに付け加えよう。
* 最終的な資産ではなく、資産がいくら増えたか(減ったか)をリスト内包表記で記述し、プロットする

__UPDATE5.1__
plotできるようにした  
資産曲線と収益曲線を描こうと思ったけど、  
重要なのは最終利益なんで  
最後の結果として、  
1000回プレイした後のそれぞれの最終資産を棒グラフで示した  
初期資産を10回、100回、100回と増やしていくと勝率が50%に近づいて確実に負けないようになるが、  
資産はそれほど増えない  
課題は確実性を見極めること、資産増加率を見極めること  

__UPDATE5.0__
関数の整理  
初期資産10で動くようにした  

標準出力に以下を出力する  
* 100回分のゲーム結果
* 最終資産のリスト(100要素)
* 勝率(ゲーム数=100回平均)


__UPDATE4.1__
関数に分割
同じ初期資産を100回計算させて、収益のリストprofitListを得る

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

* 勝率を50%に十分近づける
* 負け(=初期試算を下回る)を少なくする
* 資産増加率を見極める
* 資産が*n*倍になったらassetから引く
* 引いた数をカウントする
* オプション取引のルールに最大購入金額というものがあるので、それを再現する。つまりbetはある程度の大きさまで行くと増えなくなる。

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
		if 10*defaultAsset<asset : break    #初期資産の10倍になったら終了
	print('Win game:',win)
	print('Game streak:',gnum)
	return (asset,win/gnum)


from pandas import *
import matplotlib.pyplot as plt
# def plotter(assetDefault,profitList,assetList):
# 	'''収益曲線(profitList)と資産曲線(assetList)を描画する'''
# 	xaxis=range(len(profitList))
# 	lbl='Default Asset '+str(assetDefault)

# 	fig, ax1 = plt.subplots()
# 	ax1.plot(xaxis,assetList,'-r',label='Asset')
# 	ax2 = ax1.twinx()
# 	ax2.plot(xaxis,profitList,'-b',label='Profit')

# 	'''__PLOT SETTING__________________________'''
# 	plt.legend(loc='best',fancybox=True,fontsize='small')
# 	plt.xlabel('Game streak')
# 	ax1.set_ylabel('Asset')
# 	ax2.set_ylabel('Profit')
# 	plt.grid(True)
# 	plt.show()


def assetPlotter(assetDefault,assetList,winRateAve):
	'''最終資産(assetList)を棒グラフとして描画する'''
	xaxis=range(len(assetList))
	lbl='Default Asset '+str(assetDefault)+'\nWin rate'+str(winRateAve)
	plt.bar(xaxis,assetList,label=lbl)

	'''__PLOT SETTING__________________________'''
	plt.legend(loc='best',fancybox=True,fontsize='small')
	plt.xlabel('Take')
	plt.ylabel('Asset')
	plt.grid(True)
	plt.show()







'''__MAIN__________________________
統計的に見たいから、何度も初期資産から初めて勝率見極める'''
defaultAsset=10
trial=1000    #何回試行するか(十分多く計算しないと確実性のない計算となる)
# low,high,term=10,110,10
# for defaultAsset in range(low,high,term):
# profit_tryList,winrate_tryList=[],[]
finalAssset,winRate=[],[]


print('__Game start! Your default asset is',defaultAsset,'____________')
for i in range(1,trial+1):
	print('\nTake:',i)
	p=play(defaultAsset)
	finalAssset.append(p[0])
	winRate.append(p[1])
import numpy as np
winRateAve=np.mean(winRate)
print('Final Asset:', finalAssset, 'Win ratio:', winRateAve)
assetPlotter(defaultAsset,[x-defaultAsset for x in finalAssset],winRateAve)

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
