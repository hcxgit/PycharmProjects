#coding:utf-8
# * * * * * * * * * * * * 点球小游戏* * * * * * * * * * * *
from random import choice
score_you = 0      # 开始你得分0
score_com = 0      # 开始电脑得分0
direction = ['left','center','right']  # 射击方向
for i in range(0,5):
	print '* * * * * * Round%d!* * * * * * * *'%(i+1)
	print '选择一个方向射击：'
	print 'left,center,right'
	you = raw_input()
	print '你踢的方向'+you
	com = choice(direction)
	print '电脑挽救的方向'+ com
	if you !=com:
		print '进球了'
		score_you += 1
	else:
		print '菜鸡，没进去！'
		score_com += 1
	print '分数：'
	print '你：%d     电脑：%d'%(score_you,score_com)
