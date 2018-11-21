# -*- coding: utf-8 -*-
print("————————我爱鱼C工作室——————————")
temp = input("不妨猜猜小甲鱼心里想的是哪个数字？")
guess = int(temp)
while guess != 8:
	temp = input("猜错了，重新再猜一次吧？")
	guess = int(temp)
	if guess == 8:
		print("挖槽，你是小甲鱼肚子里面的蛔虫吗？")
		print("哼，猜中了也没有奖励。")
	else: 
		if guess > 8:
			print("哥，大了大了。")
		else:
			print("嘿，小了，小了。")
print("游戏结束，不玩啦~~")