import random
r = random.randint(1, 100)

while True:
	x = input('請猜猜看數字是什麼？')
	x= int(x)
	if x == r:
		print('終於猜對了!!')
		break
	elif x > r:
		print('比答案大')
	else:
		print('比答案小')