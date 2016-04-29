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
	'''
	## soubakan_unitest ver1.0
	
	__UPDATE1.0__
	First commit
	
	__USAGE__
	game_soubakan_integrationtestから呼び出される
	
	__INTRODUCTION__
	soubakanのユニテスト
	
	__ACTION__
	相場観パラメータを設定
	中央値1.4、最低値1.0, 最大値無限大のヒストグラムか描かれるようにsoubakan関数が動いているか
	プロットすることでチェックを行う
	
	__PLAN__
	None
	soubakan()(相場観)のユニテスト
	偏りをもったガウシアン状のヒストグラムがプロットされる
	'''
	low,high=1.01,np.inf
	mu,si=1.4,0.3
	x=soubakan(low, high, mu, si,10000)
	print('minimum ratio',min(x))
	print('maximum ratio',max(x))
	plt.hist(x);plt.show()









def game_test(ratio):
	'''
	## game_test ver1.0
	
	__UPDATE1.0__
	First commit
	
	__USAGE__
	game_unitestとgame_soubakan_integrationtestから呼び出される
	
	__INTRODUCTION__
	game関数の汎用テスト関数
	
	__ACTION__
	trytime=10000回くらい以下の処理を行う
	引数game関数
	>`1<ratio<inf`
	>>いつも2超えるくらいまで
	何回もゲームして
	ゲームに勝った(Trueが返ってきた)率がratioに十分近いかを判断する
	
	__PLAN__
	None
	'''
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
	'''
	## game_unitest ver1.0
	
	__UPDATE1.0__
	First commit
	
	__USAGE__
	game_unitest()のコメントアウトをはずして実行
	
	__INTRODUCTION__
	game()のユニテスト
	
	__ACTION__
	倍率ratioを適当に決める
	汎用テスト関数game_test()を実行する
	
	__PLAN__
	None
	'''
	for ratio in [1+x*0.2 for x in range(20)]:
		game_test(ratio)









def game_soubakan_integrationtest():
	'''
	## game_soubakan_integrationtest ver1.0
	
	__UPDATE1.0__
	First commit
	
	__USAGE__
	game_soubakan_integrationtest()のコメントアウトをはずす
	
	__INTRODUCTION__
	game()とsoubakan()の結合テスト
	
	__ACTION__
	soubakanは中央値1.4の正規分布に従う乱数返してくる
	> ただし1<ratio<inf
	gameはsoubakanから返ってきた勝率に従う確率でTrueを返す
	Trueの返ってくる確率がsoubakanの中央値1.4の逆数に近づくはず

	```run result
	__________ ratio: 1.465780521846425 __________
	Winrate : 0.682230 , Result : 0.678100
	Subtraction 0.00413037835180996
	```

	* ratioは何倍のチケットを買ったのか
	* Winrate:計算式から導かれる勝率(0で絶対勝てない、1で絶対勝てる)
	* Result:関数gameに実際に10000回くらい勝ち負けを判定させ、帰ってきたTrueの回数を試行回数で割り算するとWinrateに近い値が出るはず
	* Subtraction: WinratioとResultの差分
	
	__PLAN__
	None
	'''
	low,high=1.01,np.inf
	mu,si=1.4,0.3
	x=soubakan(low, high, mu, si,1)
	game_test(float(x))



'''__MAIN__________________________'''
# soubakan__unitest()
# game_unitest()
game_soubakan_integrationtest()
