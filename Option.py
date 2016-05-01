'''
## Option ver1.0

__UPDATE1.0__
First commit

__USAGE__
?

__INTRODUCTION__
ratioから始まりprofitが決まるまでにClass使えるんじゃないか
まだわからん

__ACTION__
--action--

__PLAN__
None
'''
from game2 import *
class Option:
	"""docstring for Option"""
	def __init__(self):
		self.ratio=float(soubakan(low=1.01, high=np.inf, mu=1.4, si=0.3, length=1))
		self.price = round(1000/self.ratio,-1)    #単価が決まる
		self.unit = 1
		self.bet=self.unit*self.price
		self.last=self.bet
		self.profit = self.unit*(1000-self.price)
		self.asset=1000
		print('--Game Start--')
		print('ratio %f\nprice %d x unit %d=bet %d\npayout %d,profit %d\nasset will %d=>%d' %( self.ratio, self.price,self.unit,self.bet,self.unit*1000,self.profit,self.asset,self.profit+self.asset))
		print('_'*20)


	def __iter__(self):
		self._i=0
		return self

	def __next__(self):
		# while self.profit<self.bet*2:
		self._i+=1
		if self._i == 100:
			raise StopIteration()
		self.ratio=float(soubakan(low=1.01, high=np.inf, mu=1.4, si=0.3, length=1))
		self.price = round(1000/self.ratio,-1)    #単価が決まる
		# self.profit=0
		# self.unit=0
		self.last=self.bet
		print('Before bet asset',self.asset)
		print('bet -',self.last)
		if self.asset<self.bet:
			print('I have no more money!')
			raise StopIteration()
		self.asset-=self.bet
		print('Before game asset',self.asset)
		import random
		if random.random()>=1-1/self.ratio:
			print('Win!+',self.unit*1000)
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
		print('After game asset',self.asset)
		return self

	# def price(self,ratio):
	# 	price= round(1000/ratio,-1)    #単価が決まる
	# 	return (self.price)

'''
TEST
'''
x=Option()
for i in x:
	print('--Next Game--')
	print('ratio %f\nprice %d x unit %d=bet %d\npayout %d,profit %d\nasset will %d=>%d' %( i.ratio, i.price,i.unit,i.bet,i.unit*1000,i.profit,i.asset,i.profit+i.asset))
	print('_'*20)

# j=1
# asset=100000
# while asset>0:
# 	print('ratio%f\nprice%dxunit%d\n=bet%d\nprofit%d' %( x.ratio, x.price,x.unit,x.bet,x.profit))
# 	asset-=x.bet
# 	print('before:',asset)
# 	asset+=x.profit
# 	print('after:',asset)
# 	print('_'*20)
# 	j+=1
# 	if j>100:break



# print(x.rati\o)
# print(x.next())
# for i in x.ratio:
# 	print(i)
# for i in range(10):
# 	y=next(i)
# 	print(y)
# 	j+=1
# 	if j>100:break



# from game2 import *
# ratio=float(soubakan(low=1.01, high=np.inf, mu=1.4, si=0.3, length=1))
# print(ratio)
# price=round(1000/ratio,-1)
# print(price)
# unit=unit(bet=1000, price)
# print(unit)

