'''
## game.py ver1.1
__UPDATE1.1__
逐一assetとgameの結果を比較して、assetを超えたらループ終了  

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

def game(bet,gametime):
	'''半分の確率で勝敗決め、報酬(profit)として勝ったら掛け金(bet),負けたら0を返す'''
	profit=bet
	for i in range(gametime):
		import random
		if random.random()>0.5:
			profit=bet
		else :
			profit+=profit
		yield profit

# result=list(game(bet,gametime))
# print('Game result\n',result)
# print('Win rate is',result.count(1)/gametime,'%')
# print('Max drowdown is',max(result))


'''
__MAIN__________________________
逐一assetとgameの結果を比較して、assetを超えたらループ終了
'''
defaultAsset=100
bet=1
breakPlaytime=1000    #連続1000回までプレイ
k=[]
asset=defaultAsset-bet
for profit in game(bet,breakPlaytime):
	asset+=profit
	k.append(profit)
	if profit>asset:
		break
print(k)
