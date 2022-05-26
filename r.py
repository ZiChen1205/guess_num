import random
r = random.randint(1, 100)
y = 0
while True:
	y += 1
	x = input('請猜猜看數字是什麼？')
	x= int(x)
	if x == r:
		print('終於猜對了!!')
		print('這是你猜的第',y, '次')
		break
	elif x > r:
		print('比答案大')
	elif x < r:
		print('比答案小')
	print('這是你猜的第',y, '次')