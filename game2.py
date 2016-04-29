'''
## game2.py ver1.0

__UPDATE1.0__
First commit

__USAGE__
martingaleのメイン関数から呼び出す
###### 相場観パラメータの設定 
	low,high=1.01,np.inf
	mu,si=1.4,0.3
######  
	x=soubakan(low, high, mu, si,1)
	game_test(float(x))

__INTRODUCTION__
soubakan(相場観):
	自分の取引履歴から算出した、倍率いくらのチケットを買うか、倍率を返す
game:
	ゲームの結果をbool値で返す

__ACTION__

__PLAN__
None
'''
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
from random import random
def soubakan(low, high, mu, si, length=1):
	'''正規分布に従う乱数の入ったリストを返す
	low, high: 正規分布の最小値、最大値
	mu, si: 正規分布の中央値、標準偏差
	length: いくつの要素のリストを返すか'''
	x=stats.truncnorm.rvs((low-mu)/si, (high-mu)/si,loc=mu, scale=si,size=length)
	return x



def game(ratio):
	'''1-1/ratioの確率で勝つゲームに勝ったらTrueを返す'''
	x=bool(random()>=1-1/ratio)
	return x
