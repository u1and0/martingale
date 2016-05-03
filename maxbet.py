'''
## maxbet ver1.0

__UPDATE1.0__
first commit

__INTRODUCTION__
最大購入可能金額(Max Bet)を調べるpy

__USAGE__

* 引数
	* asset:資産
	* mode:デフォルトはラダー取引。レンジにするには第2引数に'r'か'range'と入れる。省略するとラダー、'r'か'range'の文字以外でもラダー
* 戻り値
	* 最大購入可能掛け金(単位:万円)

importして使用
または
TESTのコメントアウトはずしてbuild

__ACTION__
ラダー(ladder)とレンジ(range)の2種類の取引方法
口座口数0~600以上でif文分岐
数字は[YJFX!のバイナリオプトレのページ](http://www.yjfx.jp/opt/information/outline/)のを拾ってきた。

__PLAN__
none
'''

def maxbet(asset,mode='l'):
	'''単位:[万円]'''
	if mode in ['range' ,'r']:
		if asset<10000:
			ticket=0
		elif 10000<=asset<100000:
			ticket=10
		elif 100000<=asset<500000:
			ticket=25
		elif 500000<=asset<1000000:
			ticket=50
		elif 1000000<=asset<3000000:
			ticket=100
		elif 3000000<=asset<6000000:
			ticket=300
		else :
			ticket=500
	else:# ('l' or 'ladder') == mode:
		if asset<10000:
			ticket=0
		elif 10000<=asset<100000:
			ticket=10
		elif 100000<=asset<500000:
			ticket=25
		elif 500000<=asset<1000000:
			ticket=50
		elif 1000000<=asset<3000000:
			ticket=100
		elif 3000000<=asset<6000000:
			ticket=300
		else :
			ticket=500
	return ticket




# '''TEST'''
# for i in ['l','r','ladder','range','m','']:
# 	for x in range(-100000,7000000,50000):
# 		print('mode: %s, asset:%d, max ticket: %d'% (i,x,maxbet(x)))
# 		# print('mode',i,'\tasset',x,'\tmaxbet',maxbet(x,i))
