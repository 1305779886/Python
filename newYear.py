import requests
import pandas as pd
from urllib.parse import quote

def get_content(year):
    keywords = quote('年中国中央电视台春节联欢晚会')
    url = 'https://zh.wikipedia.org/wiki/{}{}'.format(year,keywords)
    # 1 节目单； 0 节目信息
    if year != 2014:
        response = pd.read_html(url)[1]
    else:
        response = pd.read_html(url)[3]
    response['year'] = year
    response.drop([0],inplace=True) #删除首行
    response.to_csv('chinese_newyear.csv',mode='a',encoding='utf_8_sig',index=0,header=0)

if __name__ == '__main__':
   for year in range(1983,2018):
       get_content(year)