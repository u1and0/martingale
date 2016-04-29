import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
from random import random
def soubakan(low, high, mu, si, length):
	'''正規分布に従う乱数を返す
	low, high: 正規分布の最小値、最大値
	mu, si: 正規分布の中央値、標準偏差
	length: いくつの要素のリストを返すか'''
	x=stats.truncnorm.rvs((low-mu)/si, (high-mu)/si,loc=mu, scale=si,size=length)
	return x



def game(rate):
	'''1-1/rateの確率で勝つゲームに勝ったらTrueを返す'''
	x=bool(random()>=1-1/rate)
	return x




'''TEST2
テストの内容
	何回もゲームして
	勝率を相場観に任せるwinratea=soubakan()
	勝率が自分の相場観にあったものか確かめる
	いつも1.4倍くらい、つまり1/1.4=0.7位に近づくはずだ
'''
# low,high=1.01,np.inf
# mu,si=1.4,0.3
# lll=[]
# trytime=100
# for i in range(trytime):
# 	x=(float(soubakan(low, high, mu, si, 1)))    #倍率
# 	ox=1-1/x    #勝率
# 	y=game(x)    # 勝敗
# 	lll.append(y)
# 	print('baititsu', x, 'winrate',ox,'Did I Win?',y)
# print('How many time did I win', lll.count(True)/trytime)
