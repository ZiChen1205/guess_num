import random
print('這是個猜數字的遊戲,請自行定義最大數字和最小數字')
x = input('最大數字:')
y = input('最小數字:')
x = int(x)
y = int(y)
num = random.randint(y, x)
count = 0
while True:
	count += 1
	guess = input('請猜猜看數字是什麼？')
	guess = int(guess)
	if guess == num:
		print('終於猜對了!!')
		print('這是你猜的第',count, '次')
		break
	elif guess > num:
		print('比答案大')
	elif guess < num:
		print('比答案小')
	print('這是你猜的第',count, '次')