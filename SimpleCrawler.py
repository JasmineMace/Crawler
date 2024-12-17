"""
Simple Web Crawler
"""

import requests
from bs4 import BeautifulSoup
from lxml import etree


search = input("Please enter what you wannan to search for：")

for i in range(1, 102, 10):

    url = f'https://cn.bing.com/search?q={search}&first={i}'
    print(url)

    header = {
        'cookie': 'MUID=22577192BDC56CCC39BA656CBC866D59; _EDGE_V=1; SRCHD=AF=SHORUN; SRCHUID=V=2&GUID=34DEC6FC54464D5FA089347A43C8B8C9&dmnchg=1; MUIDB=22577192BDC56CCC39BA656CBC866D59; MUIDV=NU=1; ANON=A=44AD5FECDBD24FECD066FF18FFFFFFFF; _tarLang=default=zh-Hans; _TTSS_IN=hist=WyJlbiIsImF1dG8tZGV0ZWN0Il0=&isADRU=0; _TTSS_OUT=hist=WyJ6aC1IYW5zIl0=; WLS=C=8a8a97126913d7c8&N=nie; ak_bmsc=1D91C7F0272B324C3A9197882C056D7E~000000000000000000000000000000~YAAQzuNH0nEU5p+TAQAA4TtWtBpEq3s9+VhKw6aa4+PkzA05MBjzazZogkbGJQaD0xHmWSoldBzUx6/Lrr1i0T7m0swXq8z2OLZkweDnleqX8r/H66MgA4Lvl5NFsTtrA9GkwCVvMBoK+UKRXg36/+uvHo23yD3CjGZLWnZBDQWuM/rwxC77ZwdAfdkrEmocNd+cVmNDvyNDwr8EVrA88cePIQnzGnVq8KKbxKi6mo+1jfKli5KsEESfn2KI8HoO128kNRiG+RgiAKssVkW/Ls6OvqemoN5uE+gxGxtpSpxd78+VCRPOQ/JVspnx3PgnAj/EJAJeBZNF/oMEd3tQms/yz7+QmqM8UJIcfNoGR94BYpaPFXyb4LeMWyc3SUyfqy/GmMLGWLk=; _Rwho=u=d&ts=2024-12-11; _EDGE_S=SID=2B1D54B2632B6D7D3F8A41E0623B6C97&mkt=zh-CN&ui=zh-cn; USRLOC=HS=1&ELOC=LAT=30.555086135864258|LON=104.07757568359375|N=%E6%AD%A6%E4%BE%AF%E5%8C%BA%EF%BC%8C%E5%9B%9B%E5%B7%9D%E7%9C%81|ELT=4|&BID=MjQxMjExMTQwOTI2XzBhZGUxMGQ5M2U3YzIxODUzZjI0MWRmODRmMTJhZjVjODgyNzIyOWQ5ZjQ3YTgwNzRhNjgwYTVhNjFiMTdhOGI=; _U=1dMslMK0f9bhoE-3OgiPmdrJFK76XNnWG6RLfm2NwxvjY9863XU4CBYFyMnep1QlKvAZHWLHk9I6oiy8r8QjxLJLoikDO4aqzZ0NL57k0kx9lQ-oBhggG-WMoOddeOxUlkuDALaC5M_vRmHdUL4MErUUUbH-7fzeSbOHxd5Hl1u6FZ-WHVDMDiaH88XDiwGnZ3vCuOmAHIpQnbf-0mjGmLw; SNRHOP=I=&TS=; SRCHUSR=DOB=20240918&T=1733901297000; _C_ETH=1; dsc=order=BingPages; GC=FBmMtPyOfFxfMn6Xr8YXvMhgR0P3mW7mLQZu5-HmXiJTyzYrS2-hAnZBfxtF5m8-WusKh21wqGjyugh1gHTQ8w; _RwBf=r=0&ilt=8&ihpd=0&ispd=8&rc=16833&rb=16833&gb=0&rg=0&pc=16833&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=10&l=2024-12-10T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=-62135539200&rwflt=-62135539200&rwaul2=0&o=0&p=MULTIGENREWARDSCMACQ202205&c=ML2357&t=6546&s=2022-11-20T03:54:33.0704074+00:00&ts=2024-12-11T07:16:38.0442692+00:00&rwred=0&wls=0&wlb=0&wle=0&ccp=2&cpt=0&lka=0&lkt=0&aad=0&TH=&mta=0&e=axmsJn7fdU5lBqyYjuq3hfHxSg_hS6fXcKinq1tr9MToDf2TDzxms_3Oc1MEaldBkdNCyRH2_cvo_DwZbTY8ajRrpG7BvcjOF31EBdPzNhk&A=; _SS=SID=2B1D54B2632B6D7D3F8A41E0623B6C97&PC=NMTS&R=16833&RB=16833&GB=0&RG=0&RP=16833; SRCHHPGUSR=SRCHLANG=zh-Hans&PV=15.0.0&BZA=0&HV=1733901399&DM=0&BRW=NOTP&BRH=T&CW=426&CH=1272&SCW=1084&SCH=3027&DPR=1.0&UTC=480&THEME=0&WEBTHEME=0&EXLTT=31&WTS=63862262810&PRVCW=715&PRVCH=1272&NTWKTYP=4g&AV=14&ADV=14&RB=0&MB=0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',

    }

    # CSS selector
    html =  requests.get(url, headers=header)
    soup = BeautifulSoup(html.text, 'lxml')
    divs = soup.select('div#b_content ol#b_results li.b_algo h2 a')

    for div in divs:
        print('URL:', div['href'])
        print('Title:', div.text)
        print('-' * 10)


    # XPath 
    # soup = etree.HTML(html.text)
    # hrefs = soup.xpath('//div[@id="b_content"]/main/ol/li/h2/a/@href')

    # for href in hrefs:
    #     print('URL:', href)
    #     # print('Title:', div.text)
    #     print('-' * 10)

