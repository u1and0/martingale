'''
martingale.py 3.0
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
<UPDATE3.0>
初期資産を10~90まで増やしてみた
'''

import random
def game(x):
	if random.random()>0.5:
		# print('Win! I got', 2*x, 'and I\'ll bet 1 next time.' )
		return 1
	else:
		# print('Lose! I lost', x, 'and I\'ll bet', 2*x ,'next time.')
		x+=x
		return x

for asset in range(10,100,10):
	assetDefault=asset
	bet=1
	gnum=0
	win=0
	while asset>bet:
		# print('\n____________________________')

		gnum+=1
		# print('Game times:',gnum)

		asset-=bet
		# print('Bet:',bet)

		result=game(bet)
		if result==1:
			win+=1
			asset+=2*bet
		bet=result

		# print('Asset:', asset)
		if gnum>100 : break

	print('\n____________________________')
	print('Default asset:',assetDefault)
	print('Game times:', gnum)
	print('Win rate:', win/gnum)
	print('Profit:', asset-assetDefault)
