from game2 import *
class Option:
	'''
	## Option ver1.2

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
	* 安全資産の移動
	* 資産の推移をplot
	* 初期資産を変化させる
	* 最大掛け金評価モジュール maxbet

	'''
	def __init__(self,defaultAsset):
		self.ratio=float(soubakan(low=1.01, high=np.inf, mu=1.4, si=0.3, length=1))
		self.price = round(1000/self.ratio,-1)    #単価が決まる
		self.ticket = 1
		self.bet=self.ticket*self.price
		self.last=self.bet
		self.profit = self.ticket*(1000-self.price)
		self.asset=defaultAsset
		print('--My asset is %d--'% self.asset)
		print('--Game Start--')
		print('ratio %f\nprice %d x ticket %d=bet %d\npayout %d,profit %d\nasset will be %d=>%d' %( self.ratio, self.price,self.ticket,self.bet,self.ticket*1000,self.profit,self.asset,self.profit+self.asset))
		print('_'*20)


	def __iter__(self):
		self._i=0
		return self

	def __next__(self):
		self._i+=1
		if self._i == 100:
			raise StopIteration()
		self.ratio=float(soubakan(low=1.01, high=np.inf, mu=1.4, si=0.3, length=1))
		self.price = round(1000/self.ratio,-1)    #単価が決まる
		self.last=self.bet
		print('Before bet asset: %d'% self.asset)
		print('bet -%d'% self.last)
		if self.asset<self.bet:
			print('--I have no more money!--')
			raise StopIteration()
		self.asset-=self.bet
		print('Before game asset %d'% self.asset)
		import random
		if random.random()>=1-1/self.ratio:
			print('Win!')
			print('asset +%d'% (self.ticket*1000))
			self.asset+=self.ticket*1000
			self.ticket=1
			self.bet=self.ticket*self.price
			self.profit = self.ticket*(1000-self.price)
		else:
			print('Lose!')
			while self.profit<self.last*2:
				self.ticket+=1
				self.bet=self.ticket*self.price
				self.profit = self.ticket*(1000-self.price)
		print('After game asset %d'% self.asset)
		return self


'''
TEST
'''
x=Option(10000)
asset=[]
for i in x:
	print('--%d Game--\nratio %f\nprice %d x ticket %d=bet %d\npayout %d,profit %d\nasset will %d=>%d' %(i._i, i.ratio, i.price,i.ticket,i.bet,i.ticket*1000,i.profit,i.asset,i.profit+i.asset))
	print('_'*20)
	asset.append(i.asset)
print(asset)
