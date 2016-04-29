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
class Option:
	"""docstring for Option"""
	def __init__(self,ratio):
		self.ratio = ratio
		self.price = round(1000/ratio,-1)    #単価が決まる
		# self.unit = unit
		# self.bet = bet
		# self.payout = payout
		# self.profit = profit
	def price(self,ratio):
		price= round(1000/ratio,-1)    #単価が決まる
		return (self.price)
	# def profit(bet,unit):
	# 	payout=unit*1000
	# 	profit=payout-bet
	# 	return profit

	# def unit(bet, price):
	# 	'''ゲーム始めは前回のbetがない
	# 	profitと同じ値にすれば前回利益が0'''
	# 	unit=1
	# 	profit=profit(bet, unit)
	# 	while profit<bet*2:    #利益が前回掛け金掛け金の倍になるまで
	# 		unit+=1
	# 		bet=unit*price
	# 		profit=profit(bet,unit)
	# 	return unit





'''
TEST
'''
x=Option(3)
# x.ratio=3
print(x.ratio,x.price)

# from game2 import *
# ratio=float(soubakan(low=1.01, high=np.inf, mu=1.4, si=0.3, length=1))
# print(ratio)
# price=round(1000/ratio,-1)
# print(price)
# unit=unit(bet=1000, price)
# print(unit)

