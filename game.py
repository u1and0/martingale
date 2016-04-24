'''
## game.py ver1.0
__UPDATE1.0__
first commit

__INTRODUCTION__
ジェネレータを使ってゲームの掛け金表した

__USAGE__
just build

__ACTION__
**引数**
bet:掛け金
gametime:ゲーム回数

**戻り値**
profit:掛け金に対する報酬(勝ったらbet,負けたら0)

**ルール**
乱数返して半分の確率で勝敗決める
ジェネレータ式 gameでイールドされたイテレータをprint

__PLAN__
gameの結果を資産(asset)に追加したり差し引いたり
グラフにプロット
'''
asset=300
bet=1
gametime=10000

import random
def game(bet,gametime):
	profit=bet
	for i in range(gametime):
		if random.random()>0.5:
			profit=bet
		else :
			profit+=profit
		yield profit

result=list(game(bet,gametime))
print('Game result\n',result)
print('Win rate is',result.count(1)/gametime,'%')
print('Max drowdown is',max(result))
