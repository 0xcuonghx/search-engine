import vnexpress
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')
data = vnexpress.crawler()
data.to_csv('./crawler/data/{}.csv'.format(today), index=False, encoding='utf-8', escapechar='\\')