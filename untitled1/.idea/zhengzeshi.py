#import re
import pandas as pd
from numpy import *
import matplotlib.pyplot as plt
ts = pd.Series(random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()
'''text = 'site sea sue sweet see case sse ssee loses'
text2 = '18322597036 23123 423525'
text3 = '(021)88776543 010-55667890 02584453362 0571 66345673 1233435434'
m = re.findall(r"\bs\S*e\b",text)
f = re.findall(r"1\d{10}",text2)
g = re.findall(r"\(?0\d{2,3}[) -]?\d{7,8}",text3)
print m
print f
print g
'''