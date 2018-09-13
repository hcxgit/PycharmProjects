#coding:utf-8
from random import randint
f = open('game.txt')
name = raw_input('请输入你的名字:')
lines = f.readlines()
f.close()

scores = {}                   #字典记录成绩
for l in lines:
	s = l.split()
	scores[s[0]] = s[1:]      #第一项作为key，剩下的作为value
score = scores.get(name)
if score is None:             #如果没找到，
	score = [0,0,0]           #初始化数据

game_times = int(score[0])   #已玩游戏次数
min_times = int(score[1])    #最快猜到的轮数
total_times = int(score[2])  #总轮数
if game_times > 0:
	avg_times = float(total_times)/game_times     #平均轮数
else:
	avg_times = 0
print '%s,你已经玩了%d次游戏，最少%d轮猜中答案，平均%.2f轮猜中答案'%(name,game_times,min_times,avg_times)

times = 0                    #每轮玩的游戏次数
def isEqual(num1,num2):
	if num1 < num2:
		print 'too small'
		return False

	elif num1 > num2:
		print 'too big'
		return False
	else:
		print '猜对了'
		return True

num = randint(0,10)
bingo = False
print 'who do you think i am'
while bingo == False:
	answer = input()
	bingo = isEqual(answer,num)
	times += 1

if game_times ==0 or times<min_times:     #修改数据
	min_times = times
total_times += times
game_times += 1
   #  更新成绩
scores[name] = [str(game_times),str(min_times),str(total_times)]
result = ''
for n in scores:
	line = n + ' '+' '.join(scores[n])+'\n'
	result += line
f = open('game.txt','w')
f.write(result)
f.close()


