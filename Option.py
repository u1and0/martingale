from game2 import *
class Option:
	'''
	## Option ver1.1

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
	None
	'''
	def __init__(self,asset):
		self.ratio=float(soubakan(low=1.01, high=np.inf, mu=1.4, si=0.3, length=1))
		self.price = round(1000/self.ratio,-1)    #単価が決まる
		self.unit = 1
		self.bet=self.unit*self.price
		self.last=self.bet
		self.profit = self.unit*(1000-self.price)
		self.asset=asset
		print('--My asset is %d--'% self.asset)
		print('--Game Start--')
		print('ratio %f\nprice %d x unit %d=bet %d\npayout %d,profit %d\nasset will be %d=>%d' %( self.ratio, self.price,self.unit,self.bet,self.unit*1000,self.profit,self.asset,self.profit+self.asset))
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
		print('Before bet asset',self.asset)
		print('bet -',self.last)
		if self.asset<self.bet:
			print('--I have no more money!--')
			raise StopIteration()
		self.asset-=self.bet
		print('Before game asset %d'% self.asset)
		import random
		if random.random()>=1-1/self.ratio:
			print('Win!')
			print('asset +%d'% (self.unit*1000))
			self.asset+=self.unit*1000
			self.unit=1
			self.bet=self.unit*self.price
			self.profit = self.unit*(1000-self.price)
		else:
			print('Lose!')
			while self.profit<self.last*2:
				self.unit+=1
				self.bet=self.unit*self.price
				self.profit = self.unit*(1000-self.price)
		print('After game asset %d'% self.asset)
		return self

	# def price(self,ratio):
	# 	price= round(1000/ratio,-1)    #単価が決まる
	# 	return (self.price)

'''
TEST
'''
x=Option(10000)
for i in x:
	print('--Next Game--')

	print('ratio %f\nprice %d x unit %d=bet %d\npayout %d,profit %d\nasset will %d=>%d' %( i.ratio, i.price,i.unit,i.bet,i.unit*1000,i.profit,i.asset,i.profit+i.asset))

	print('_'*20)
