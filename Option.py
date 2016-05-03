from game2 import *
class Option:
	'''
	## Option ver1.3

	__UPDATE1.3__
	plot機能
	assetのsafeへの移動
	初期資産の変更

	__UPDATE1.2__
	資産の推移をリストにappend
	printメッセージ修正

	__UPDATE1.1__
	引数に初期資産
	printメッセージ修正

	__UPDATE1.0__
	First commit

	__USAGE__
	初期資産assetを引数に
	結果を標準出力にprint

	__INTRODUCTION__
	プッシュ投資法をオプション取引でシミュレート

	__ACTION__
	init で初期値を決める
	iterはinitの初期値を全てnextに渡す
	nextでループ


	__PLAN__
	何度も試行する

	'''
	def __init__(self,defaultAsset):
		self.ratio=float(soubakan(low=1.01, high=np.inf, mu=1.4, si=0.3, length=1))
		self.price = round(1000/self.ratio,-1)    #単価が決まる
		self.ticket = 1
		self.bet=self.ticket*self.price
		self.last=self.bet
		self.profit = self.ticket*(1000-self.price)
		self.defaultAsset=defaultAsset
		self.asset=defaultAsset
		self.safe=0
		print('--My asset is %d--'% self.asset)
		print('--Game Start--')
		print('ratio %f\nprice %d x ticket %d=bet %d\npayout %d,profit %d\nasset will be %d=>%d' %( self.ratio, self.price,self.ticket,self.bet,self.ticket*1000,self.profit,self.asset,self.profit+self.asset))
		print('_'*20)


	def __iter__(self):
		self._i=0
		return self

	def __next__(self):
		self._i+=1
		self.ratio=float(soubakan(low=1.01, high=np.inf, mu=1.4, si=0.3, length=1))
		self.price = round(1000/self.ratio,-1)    #単価が決まる
		self.last=self.bet
		print('Before bet asset: %d'% self.asset)
		print('bet -%d'% self.last)
		if self.asset<self.bet:
			print('--I have no more money!--')
			raise StopIteration()    #掛け金掛けられなければ終了
		self.asset-=self.bet
		print('Before game asset %d'% self.asset)
		import random
		if random.random()>=1-1/self.ratio:    #ゲームの勝敗を決める
			print('Win!')
			print('asset +%d'% (self.ticket*1000))
			self.asset+=self.ticket*1000
			if self.asset > self.defaultAsset*1.1:
				self.safe+=self.defaultAsset*0.1
				self.asset-=self.defaultAsset*0.1
				print('# Move money +%d, safe money: %d'% (self.defaultAsset, self.safe))
			self.ticket=1
			self.bet=self.ticket*self.price
			self.profit = self.ticket*(1000-self.price)
		else:
			print('Lose!')
			while self.profit<self.last*2:    #次の賭けチケット数計算
				self.ticket+=1
				self.bet=self.ticket*self.price
				self.profit = self.ticket*(1000-self.price)
			import maxbet
			self.ticket=min(maxbet.maxbet(self.asset),self.ticket)    #最大掛け金評価
		print('After game asset %d'% self.asset)
		return self




import matplotlib.pyplot as plt
def plotter(s,l):
	'''収益曲線(profitList)と資産曲線(assetList)を描画する'''
	xaxis=range(len(l))
	lbl='Default Asset '+str(s)
	plt.plot(range(len(l)),l,label=lbl)
	plt.legend(loc='best',fancybox=True,fontsize='small')
	plt.xlabel('Game streak')
	plt.grid(True)





'''
TEST
'''
assetList=[]
profitList=[]
for y in [1000000]:
	x=Option(y)
	for i in x:
		print('--%d Game--\nratio %f\nprice %d x ticket %d=bet %d\npayout %d,profit %d\nasset will %d=>%d' %(i._i, i.ratio, i.price,i.ticket,i.bet,i.ticket*1000,i.profit,i.asset,i.profit+i.asset))
		print('_'*20)
		# assetList.append(i.asset)
		profitList.append(i.asset-y)
	print(profitList)
	plotter(y,profitList)
plt.show()
