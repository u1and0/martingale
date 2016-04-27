'''
## martingale2 ver1.0

__UPDATE1.0__
First commit

__USAGE__
Just build

__INTRODUCTION__
--introduction--

__ACTION__

**ゲームのルール**
資産が掛け金を下回るまで繰り返す
	資産から掛け金を引く
	ゲームを行い結果をブール値で返す
	資産について：勝ったら掛け金の2倍を足し、負けたら0を足す(=何もしない)
	掛け金について：勝ったら掛け金を1に戻し、負けたら掛け金を2倍にする
	掛け金の評価：上で出された掛け金と、資金に基づく掛け金の最大値いずれか小さい方
**   ざわざわ･･･倍プッシュだ･･･！**
ゲームの開始に戻る



__PLAN__
None
'''
asset=10
bet=1
i=0
while 1:
	asset-=bet
	import random
	result=random.random()>0.5    #ゲームの結果(bool値)
	asset+=2*bet if result else 0    #勝ったら賞金は掛け金の2倍
	bet*=1/bet if result else 2    #勝ったら掛け金1に戻す。負けたら掛け金2倍
	import maxbet
	bet=min(bet,maxbet.maxbet(asset))    #掛け金は資金に対して最大値が決まっている
	if not bet:print('bet becomes ZERO!!');break    #
	if not asset>bet:print('I have no money!!');break
	i+=1
	print(i,'asset',asset,'bet',bet)
print('End of seqence...')
