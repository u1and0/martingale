'''
## ticket ver1.0

__UPDATE1.0__
First commit

__USAGE__
martingaleのメイン関数から呼び出す

__INTRODUCTION__
負けた際に次回購入するチケット購入数を計算する

__ACTION__
引数:前回ゲームの掛け金
戻り値:チケットの購入数

1. 勝ちそうなところの[倍率]を相場観で決める
	2. [単価]が決まる
3. [購入口数]を決める(最初は1)
	4. [購入額]が決まる
	5. [利益]が決まる
4. [資産]から[購入価格]が引かれる
6. ゲームの結果で[資産]が増える
7. 1に戻る

__PLAN__
None
'''

def profit(bet,unit):
	payout=unit*1000
	profit=payout-bet
	return profit

def unit(bet, price):
	'''ゲーム始めは前回のbetがない
	profitと同じ値にすれば前回利益が0'''
	unit=1
	profit=profit(bet, unit)
	while profit<bet*2:    #利益が前回掛け金掛け金の倍になるまで
		unit+=1
		bet=unit*price
		profit=profit(bet,unit)
	return unit


def yyy(unit, price):
	profit=unit*(1000-price)
	return profit

def xxx(ratio,lastbet=2000):
	price=round(1000/ratio,-1)
	unit=1
	profit=0
	while profit<lastbet*2:
		unit+=1
		profit=unit*(1000-price)
	return unit


'''
TEST
'''
from game2 import *
ratio=float(soubakan(low=1.01, high=np.inf, mu=1.4, si=0.3, length=1))
print(list(xxx(ratio)))


