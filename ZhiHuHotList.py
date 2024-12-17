"""
    zhihu billboard
"""

import re
import requests


url = "https://www.zhihu.com/billboard"

header = {
    'cookie': 'xsrf=atfC00WJQvsimulpwoMGdDsvJyzqImzI; _zap=80e068e5-219b-4acb-95df-c4d65d8ae270; d_c0=AvARoxDUSxmPTnCUXyF-sNrk_JmGTEIuxbY=|1727365485; __zse_ck=004_ujq6NpYEq7UbX/EnelRBlm2YQLrAwJ/56FviYd6mkv=p/55AjeP0j5OjLdiKYsWvbyaX6z5NGVkuhKdQFQbFX9aT0QYTWqSX0ztwc4/24jfGI2IjJhsCfsQRqUCHZdXO-8RWJuXe760WVVrLEf8h8MbCLmar/tzh4nkM/01MLGDFkS7YpmluwZ4j7FGRrENb13DxjSh29+PytStjdNlbkO1WonOo67BYAmfDbxmWN5zotvjo8yNI5YyhyyCq3UTrPQcgjjLfi8tejJeYk78DDCfORhF4PZA57Roid3YNFIM8=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1733225398,1733306429,1733634104,1733909759; HMACCOUNT=DD981F5BEE743DF5; z_c0=2|1:0|10:1733909758|4:z_c0|80:MS4xMDR3bkRnQUFBQUFtQUFBQVlBSlZUYUxwTTJpR3FXdVBGSEVGZmdyYkdOSzdIQzhHa1oyYjdRPT0=|4792bbb97e8b992d27a9a8fe691324d4c8cc8437eb60ba2554d8d3d837a2d457; SESSIONID=HtLvzlIyO3VFYKqC9h4CTmlzSmpYAwxgV41B60BgzuJ; JOID=WlAQCkN8VImTB50AYnh01k9cYkx2NC3J5H3xRBczZ9LZX9ZxLF0I3fUHkAFvYtX5OIaGwCe30f4isl_KTVZDl5U=; osd=Vl4XBkNwWo6fB5EOZXR02kFbbkx6OirF5HH_Qxsza9zeU9Z9IloE3fkJlw1vbtv-NIaKziC70fIstVPKQVhEm5U=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1733909995; BEC=d6322fc1daba6406210e61eaa4ec5a7a',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

html = requests.get(url, headers=header)


ReIntroduce = re.compile(',"excerptArea":{"text":"(.*?)"},"i', re.I|re.M)
ReURL = re.compile('"link":{"url":"(.*?)"}},"attachedInfo"', re.I|re.M)

Introduce = re.findall(ReIntroduce, html.text)
URL = re.findall(ReURL, html.text)

for i, u in zip(Introduce, URL):
    print("introduce:")
    print(i)
    print("URL:")
    print(u.encode('utf-8').decode('unicode_escape'))
    print('-' * 20)
