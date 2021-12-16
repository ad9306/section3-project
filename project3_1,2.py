import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

#서울시 방문팬매업 인허가 정보
#서울 열린 데이터광장에서 데이터를 가져온다. api를 통해여 1회 1000개까지 수집이 가능하므로 10회 진행하여 10000개의 데이터를 수집하고 soup
url1 = 'http://openapi.seoul.go.kr:8088/446f755768666e6638355161734f6d/xml/LOCALDATA_082602/1/1000/'
url2 = 'http://openapi.seoul.go.kr:8088/446f755768666e6638355161734f6d/xml/LOCALDATA_082602/1001/2000/'
url3 = 'http://openapi.seoul.go.kr:8088/446f755768666e6638355161734f6d/xml/LOCALDATA_082602/2001/3000/'
url4 = 'http://openapi.seoul.go.kr:8088/446f755768666e6638355161734f6d/xml/LOCALDATA_082602/3001/4000/'
url5 = 'http://openapi.seoul.go.kr:8088/446f755768666e6638355161734f6d/xml/LOCALDATA_082602/4001/5000/'
url6 = 'http://openapi.seoul.go.kr:8088/446f755768666e6638355161734f6d/xml/LOCALDATA_082602/5001/6000/'
url7 = 'http://openapi.seoul.go.kr:8088/446f755768666e6638355161734f6d/xml/LOCALDATA_082602/6001/7000/'
url8 = 'http://openapi.seoul.go.kr:8088/446f755768666e6638355161734f6d/xml/LOCALDATA_082602/7001/8000/'
url9 = 'http://openapi.seoul.go.kr:8088/446f755768666e6638355161734f6d/xml/LOCALDATA_082602/8001/9000/'
url10 = 'http://openapi.seoul.go.kr:8088/446f755768666e6638355161734f6d/xml/LOCALDATA_082602/9001/10000/'

#getdata url을 받아서 데이터프레임을 만들어 줄 함수 생성
rows = []
def getdata(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    for i in soup.find_all('row'):
        rows.append({"opnsfteamcode":i.opnsfteamcode.string,
        "mgtno":i.mgtno.string,
        "apvpermymd":i.apvpermymd.string,
        "trdstategbn":i.trdstategbn.string,
        "trdstatenm":i.trdstatenm.string,
        "dtlstategbn":i.dtlstategbn.string,
        "dtlstatenm":i.dtlstatenm.string,
        "dcbymd":i.dcbymd.string,
        "clgstdt":i.clgstdt.string,
        "clgenddt":i.clgenddt.string,
        "ropnymd":i.ropnymd.string,
        "sitetel":i.sitetel.string,
        "sitearea":i.sitearea.string,
        "sitepostno":i.sitepostno.string,
        "sitewhladdr":i.sitewhladdr.string,
        "rdnwhladdr":i.rdnwhladdr.string,
        "rdnpostno":i.rdnpostno.string,
        "bplcnm":i.bplcnm.string,
        "lastmodts":i.lastmodts.string,
        "updategbn":i.updategbn.string,
        "updatedt":i.updatedt.string,
        "uptaenm":i.uptaenm.string,
        "x":i.x.string,
        "y":i.y.string,
        "asetscp":i.asetscp.string,
        "bctotam":i.bctotam.string,
        "capt":i.capt.string,
        "silmetnm":i.silmetnm.string})
    colmns = ["opnsfteamcode", "mgtno", "apvpermymd", "trdstategbn", "trdstatenm", "dtlstategbn",
        "dtlstatenm", "dcbymd", "clgstdt", "clgenddt", "ropnymd", "sitetel", "sitearea", "sitepostno", "sitewhladdr",
        "rdnwhladdr", "rdnpostno", "bplcnm", "lastmodts", "updategbn", "updatedt", "uptaenm", "x", "y", "asetscp",
        "bctotam", "capt", "silmetnm"]
    return pd.DataFrame(rows, columns=colmns)

#데이터를 append하여 마지막 df에 모든 데이터를 쌓는다.
df1 = getdata(url1)
df2 = getdata(url2)
df3 = getdata(url3)
df4 = getdata(url4)
df5 = getdata(url5)
df6 = getdata(url6)
df7 = getdata(url7)
df8 = getdata(url8)
df9 = getdata(url9)
df = getdata(url10)

#데이터베이스 연결 파일형 데이터 베이스인 sqlite를 이용한다.
#cursor 후 execute를 통해 넣을 수도 있으나 to_sql을 통해 간편하게 넣어준다.
conn = sqlite3.connect('multilevel.db')
df.to_sql('seoul', conn)