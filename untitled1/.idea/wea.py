#coding:utf-8
import urllib2
import json
from city import city

city_name=raw_input('你想查询哪个城市的天气：\n')
city_code=city.get(city_name)

if city_code:
    url=('http://www.weather.com.cn/weather/%s.shtml'%city_code)
    web=urllib2.urlopen(url)
    content=web.read()
    print content