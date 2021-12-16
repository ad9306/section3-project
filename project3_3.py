import pandas as pd
import sqlite3
import pickle
from sklearn.ensemble import RandomForestClassifier

#1번과 2번을 계속해서 같이 실행 할 수 없으므로 파일을 나눠서 프로젝트를 진행한다.
#2번에서 저장한 db에서 df를 불러온다.
conn = sqlite3.connect('multilevel.db')

#index_col의 경우 기본값이 none으로 자동으로 0부터시작하는 정숫값이 인덱스로 할당된다.
df = pd.read_sql("SELECT*FROM seoul", conn, index_col=None)

#data를 이용하여 다중선형회귀모델을 만든다.
data = df.drop(['opnsfteamcode', 'mgtno', 'apvpermymd', 'trdstategbn', 'trdstatenm', 'dtlstategbn', 'ropnymd', 'dcbymd', 'clgstdt', 'clgenddt', 'sitetel', 'sitearea', 'sitepostno', 'sitewhladdr', 'rdnwhladdr', 'rdnpostno', 'bplcnm', 'lastmodts', 'updategbn', 'updatedt', 'uptaenm', 'x', 'y', 'silmetnm'], axis=1)
data = data.dropna(axis=0)

#data의 값은 다 str로 이를 숫자형으로 변환시켜준다.
data['asetscp']= data['asetscp'].apply(pd.to_numeric)
data['bctotam']= data['bctotam'].apply(pd.to_numeric)
data['capt']= data['capt'].apply(pd.to_numeric)

#split을 통해 데이터를 나눠준다.
from sklearn.model_selection import train_test_split
train_val, test = train_test_split(data, test_size=0.2, random_state=2)
train, val = train_test_split(train_val, test_size=len(test), random_state=2)

target = 'dtlstatenm'

X_train = train.drop(columns=target)
y_train = train[target]
X_val = val.drop(columns=target)
y_val = val[target]
X_test = test.drop(columns=target)
y_test = test[target]

#다중선형회귀모델
model = RandomForestClassifier()
model.fit(X_train, y_train)

#모델 부호화
with open('model.pkl','wb') as pickle_file:
    pickle.dump(model, pickle_file)