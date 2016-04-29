'''
## game2test ver1.0

__UPDATE1.0__
First commit

__USAGE__
テストしたいコードのテスト関数を適宜コメントアウトしてから実行

__INTRODUCTION__
モジュールgame2のテストコード

__ACTION__
game2をインポートして
テスト関数を実行していく

__PLAN__
None
'''
from game2 import *
def soubakan_unitest():
	'''soubakan()(相場観)のユニテスト
	偏りをもったガウシアン状のヒストグラムがプロットされる'''
	low,high=1.01,np.inf
	mu,si=1.4,0.3
	x=soubakan(low, high, mu, si,10000)
	print('minimum ratio',min(x))
	print('maximum ratio',max(x))
	plt.hist(x);plt.show()

def game_test(ratio):
	trytime=10000
	lll=[]
	for i in range(trytime):
		y=game(ratio)
		lll.append(y)
	print('_'*10,'ratio:',ratio,'_'*10)
	w=1/ratio
	result=lll.count(True)/trytime    #Trueの数を数える: すなわち何回勝ったか
	print('Winrate : %f , Result : %f'% (w,result))    #何回もトライして勝つ確率がbairitsuに近づけばいい
	print('Subtraction' , abs(w-result))


def game_unitest():
	'''game()のユニテスト
	倍率ratioを適当に決める
	>`1<ratio<inf`
	>>いつも2超えるくらいまで
	何回もゲームして
	ゲームに勝った(Trueが返ってきた)率がratioに十分近いかを判断する
	'''
	for ratio in [1+x*0.2 for x in range(20)]:
		game_test(ratio)


def game_soubakan_integrationtest():
	'''game()とsoubakan()の結合テスト
	soubakanは中央値1.4の正規分布に従う乱数返してくる
	> ただし1<ratio<inf
	gameはsoubakanから返ってきた勝率に従う確率でTrueを返す
	Trueの返ってくる確率がsoubakanの中央値1.4の逆数に近づくはず
	'''
	low,high=1.01,np.inf
	mu,si=1.4,0.3
	x=soubakan(low, high, mu, si,1)
	# for i in range(10):
	game_test(float(x))



'''__TEST__________________________'''
# soubakan__unitest()
# game_unitest()
game_soubakan_integrationtest()