from base64 import encode
import requests,json,time
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import firebase_admin
with open ("apikey.txt","r") as f:
    apikey_=f.read()
loc_dt = datetime.datetime.today() 
num_=[["宜蘭縣", 3369296],["桃園市", 3369297], ["新竹縣", 3369298], ["苗栗縣", 3369299], ["彰化縣", 3369300], ["南投縣", 3369301], ["雲林縣", 3369302], ["嘉義縣", 3369303], ["屏東縣", 3369304], ["臺東縣", 3369305], ["花蓮縣", 3369306], ["澎湖縣", 3369307], ["基隆市", 312605], ["新竹市", 313567], ["嘉義市", 312591], ["臺北市", 315078], ["高雄市", 313812], ["新北市", 2515397], ["臺中市", 315040], ["臺南市", 314999], ["連江縣", 3369309], ["金門縣", 2332525]]
data_daily=[]
data_hourly=[]
cred = credentials.Certificate('一條龍/weather02.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
#每日
for obj in num_:
    url_daily="http://dataservice.accuweather.com/forecasts/v1/daily/1day/{}?apikey={}&language=zh-tw".format(obj[1],apikey_)
    r_daily=requests.get(url_daily).json()
    doc_ref = db.collection(str(datetime.date.today())).document(obj[0])
    doc_ref.set({"天氣":r_daily})
    
for obj in num_:
    url_hourly="http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{}?apikey={}&language=zh-tw".format(obj[1],apikey_)
    r_houly=requests.get(url_hourly).json()
    doc_ref = db.collection(str(loc_dt.strftime("%Y-%m-%d %H時天氣"))).document(obj[0])
    doc_ref.set({"天氣":r_houly})
