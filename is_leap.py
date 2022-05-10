#function 定義
def is_leap(x):
	if x % 4 > 0 : # X不能被4整除
		return False   #回傳False
	elif x % 4 == 0 and x % 100 > 0:    # X能被4整除X不能被100整除
		return True    #回傳True
	elif x % 100 == 0 and x % 400 > 0:  # X能被100整除X不能被400整除
		return False   #回傳False
	elif x % 400 == 0 and x % 3200 > 0: # X能被400整除X不能被3200整除
		return True    #回傳True

#TypeError: not all arguments converted during string formatting
#中間出現這個錯誤是因為沒有將input之變數字串轉換成數字

while True:
	a = input('請輸入西元年，來判斷是否為閏年或按Q退出: ')  #  用戶輸入
	if a == 'q':
		break
	elif a == 'Q':
		break
	a = int(a)  #將字串轉成數字
	year = is_leap(x=a)  #將回傳值存入
	if year == True:
		print('你輸入的西元年', a, '年為閏年')
	else:
		print('你輸入的西元年', a, '年為平年')