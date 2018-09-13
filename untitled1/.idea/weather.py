#coding:utf-8
import urllib2  #用来发送网络请求，获取数据
import json     #用来解析获得的数据
from city import city

city_name = raw_input('你想查询哪个城市的天气？\n')
city_code = city.get(city_name)
if city_code:
	try:
		url = 'http://www.weather.com.cn/data/cityinfo/%s.html'%city_code
		content = urllib2.urlopen(url).read()   #h获取内容

		# json.loads() 解码：把Json格式字符串解码转换成Python对象（str->dict）
		# json.dumps()编码：把一个Python对象编码转换成Json字符串

		data = json.loads(content)
		result = data['weatherinfo']
		str_temp = '%s\n%s~%s' % (
			result['weather'],
			result['temp1'],
			result['temp2']
		)
		print str_temp
	except:
		print '查询失败'
else:
	print '没有找到该城市'
'''
url1 =  'http://www.weather.com.cn/data/list3/city.xml?level=1'
content1 = urllib2.urlopen(url1).read()
provinces = content1.split(',')
result = 'city = {\n'
url = 'http://www.weather.com.cn/data/list3/city%s.xml?level=3'
for p in provinces[:3]:
   p_code = p.split('|')[0]
   url2 = url % p_code
   content2 = urllib2.urlopen(url2).read()
   cities = content2.split(',')
   for c in cities[:3]:
	   c_code = c.split('|')[0]
	   url3 = url % c_code
	   content3 = urllib2.urlopen(url3).read()
	   districts = content3.split(',')
	   for d in districts:
		   d_pair = d.split('|')
		   d_code = d_pair[0]
		   name = d_pair[1]
		   url4 = url % d_code
		   content4 = urllib2.urlopen(url4).read()
		   code = content4.split('|')[1]
		   line = "    '%s': '%s',\n" % (name, code)
		   result += line
		   print  name + ':' + code
result += '}'
f = file('city11.py','w')
f.write(result)
f.close()
'''
