'''
martingale.py ver1.0
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

'''
import random
asset=30
bet=1
gnum=0

# def game(x):
# 	print ('bet:'x)
# 	asset-=bet
# 	gnum+=1
# 	if random.random()>0.5:
# 		print('Win! I got ,'x',and I\'ll bet 1 next' )
# 		# win+=1
# 		asset+=x
# 		x=1
# 	else:
# 		print('Lose! I got ,'x',and I\'ll bet 1 next' )
# 		# lose+=1
# 		x*=2
# 	return x

def game(x):
	x+=x
	return x

while gnum<100:
	gnum+=1
	print(bet)
	bet=game(bet)
	# print('Asset:'asset,'Win rate:',win/gnum)
