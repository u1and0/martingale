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
		if asset<1:
			bet=0
		elif 1<=asset<10:
			bet=10
		elif 10<=asset<50:
			bet=25
		elif 50<=asset<100:
			bet=50
		elif 100<=asset<300:
			bet=100
		elif 300<=asset<600:
			bet=300
		else :
			bet=500
	else:# ('l' or 'ladder') == mode:
		if asset<1:
			bet=0
		elif 1<=asset<10:
			bet=10
		elif 10<=asset<50:
			bet=25
		elif 50<=asset<100:
			bet=50
		elif 100<=asset<300:
			bet=100
		elif 300<=asset<600:
			bet=300
		else :
			bet=500
	return bet*0.1    #上の数字は口数。一口1000円単位なので0.1倍




# '''TEST'''
# for i in ['l','r','ladder','range','m','']:
# 	for x in range(-100,700,5):
# 		print(maxbet(x))
# 		# print('mode',i,'\tasset',x,'\tmaxbet',maxbet(x,i))
