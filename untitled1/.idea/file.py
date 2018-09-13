#coding:utf-8
f = file('aaaaa.txt')#读文件
lines = f.readlines()#按行取数据
print lines
f.close()
results = []
for line in lines:
	print line
	data = line.split()#按空格分开数据
	print data
	sum = 0
	for score in data[1:]:
		sum += int(score)
	result = '%s \t: %d\n' % (data[0],sum)
	print result
	results.append(result)
	print results
output = file('aaaaa.txt','w')
output.writelines(results)
output.close()
