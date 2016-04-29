'''
## martingale3 ver1.0

__UPDATE1.0__
First commit

__USAGE__
Just build

__INTRODUCTION__
martingale.pyの改造
ゲームのルールを維持しながら、コードを短くした。
どう条件の繰り返し計算やグラフ作成機能は未実装。

__ACTION__
**ゲームのルール**
資産が掛け金を下回るまで繰り返す
資産から掛け金を引く
ゲームを行い結果をブール値で返す
ゲームの支払額：購入口数×1000=購入口数×単価×勝率で表せる
勝率＝
~~購入口数は資金に依存するunit(asset)~~
	資金いっぱいあるのに購入口数少ないとき==>資金の移動
資産について：勝ったら掛け金の2倍を足し、負けたら0を足す(=何もしない)
掛け金について：勝ったら掛け金を1に戻し、負けたら掛け金を2倍にする**   ざわざわ･･･倍プッシュだ･･･！**
掛け金の評価：上で出された掛け金と、資金に基づく掛け金の最大値いずれか小さい方
終了条件：掛け金最大値評価により掛け金が0、または掛け金を資金上回る
資金の移動：一定の確率で起こる「連続負け」に対する措置として、資金が一定以上溜まったら移動(確率は後で計算する)

__PLAN__

* 購入口数×単価×勝率=購入口数×1000
~~* <負ける=資金が底をつく>見込みのほぼ考えられないだけのasset/bet比を求めること。比率を超えたら万一のための資金の移動~~
~~* n回連続して負ける確率=2**(-n)×100%<<<連続敗率と称する~~
~~	* 連続敗率が十分低いと考えられる0.01%とする~~
勝率:2-random


'''

# def sufficient(bet,rate):
# 	'''
# 	十分低いと考えられる連続して巻ける確率rate%
# 	初期試算を決める
# 	'''
# 	import numpy as np
# 	'''rate=2**(-n)'''
# 	n=-np.log2(rate)
# 	suf=bet*(2**n)
# 	return suf

# print(sufficient(1,0.5))

## __MAIN__________________________
bet, assetDefault, i, profit,assetSafe=1,100,0,0,0
# bet, asset, i, profit=1,10,0,0
asset=assetDefault
while 1:
	asset-=bet
	import random
	import numpy as numpy
	from game2 import *
	ratio=float(soubakan(low=1.01, high=np.inf, mu=1.4, si=0.3, length=1))    #相場観を見て勝ちそうな倍率を人間が決める
	
	unit=1
	bet=unit*price
	payout=unit*1000
	profit=
	result=game(ratio)    #ゲームの結果(bool値)
	asset+=2*bet if result else 0    #勝ったら資金に掛け金の2倍を足す
	bet*=1/bet if result else 2    #勝ったら掛け金1に戻す。負けたら掛け金2倍
	import maxbet
	bet=min(bet,maxbet.maxbet(asset))    #掛け金は資金に対して最大値が決まっている
	if not bet:print('bet becomes ZERO!!');break    #最大掛け金評価により、掛け金0になったら終了
	if not asset>bet:print('I have no money!!');break    #掛け金が資金を上回ったら終了
	profit=asset-assetDefault
	if profit>0:asset-=profit;assetSafe+=profit    #資金が一定以上になったら資金の一部をassetSafeに移動
	i+=1
	print(i,'asset',asset,'bet',bet,'assetSafe',assetSafe)
print('End of sequence...')


