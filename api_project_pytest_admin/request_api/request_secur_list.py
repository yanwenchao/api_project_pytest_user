"""
==================
Author: 严文超
2020/12/16 15:38
==================
"""
import requests
# 第一步：准备请求参数
# url
url = "https://crm.o2moment.com/api/batch/queryClue"
# 请求参数
params = {
    "createType": 1,
    "batchId": "BT0",
    "projectId":"",
    "batchName":"",
    "timeLimit":"",
    "bonusDays":"",
    "batchStatus": 7,
    "createTime":"",
    "filterFactors": {"createTimeType":0,"addressType":0,"status1":100,"status2":0,"distrEnterpriseId":12,"createTimeRange":"2020-12-01 00:00:00,2020-12-31 23:59:59","relativeTimeRange":"","offsetStart":"","offsetEnd":"","channel":"","landProduct":"","level":"","sex":"","startAge":"","endAge":"","ageRange":"","notInEnterpriseIds":"","inGradeForecast":"","customRecallLabel":"","answerLabel":"","customCanRecallLabel":"","transferTimeRange":"","transferlevel":"","productText":"","secondLevelText":"","ipProvinceAcode":"","ipCityAcode":"","idcardProvinceAcode":"","idcardCityAcode":"","phoneProvinceAcode":"","phoneCityAcode":"","clueStatus":"0-1.00,6-0.00","aiGroup":0,"ai":0,"clueNums":100},
    "clueStatus": "0-1.00,6-0.00",
    "clueCreateTimeRange":"",
    "channel":"",
    "landProduct":"",
    "level":"",
    "orderStatus":"",
    "limit": 10,
    "page": 1,
    "clueNums": 100,
    "startAge":"",
    "endAge":"",
    "signStatus":"",
    "sex":"",
    "crmPaymentNum":"",
    "productId":"",
    "ipProvinceAcode":"",
    "ipCityAcode":"",
    "idcardProvinceAcode":"",
    "idcardCityAcode":"",
    "phoneProvinceAcode":"",
    "phoneCityAcode":"",
    "file":"",
    "createTimeType": 0,
    "addressType": 0,
    "status1": 100,
    "status2": 0,
    "distrEnterpriseId": 12,
    "createTimeRange": "2020-12-01 00:00:00,2020-12-31 23:59:59",
    "relativeTimeRange":"",
    "offsetStart":"",
    "offsetEnd":"",
    "ageRange":"",
    "notInEnterpriseIds":"",
    "inGradeForecast":"",
    "customRecallLabel":"",
    "answerLabel":"",
    "customCanRecallLabel":"",
    "transferTimeRange":"",
    "transferlevel":"",
    "productText":"",
    "secondLevelText":"",
    "aiGroup": 0,
    "ai": 0}
# 请求头
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "authorization": "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI0MDg1Iiwic3ViIjoieWFud2VuY2hhbyIsImlhdCI6MTYwODIzMzU3MCwiZXhwIjoxNjA4MzA3MTk5fQ.Hmtt6PZaHr4wBUc7pSva27ujruOOo4JQnd4zL2CM3ZHz_IYKeAT8zfaJBpITGnyABpwPzIU4mErE16AtzGw71A"
}
# 第二步：发起请求，
response = requests.request(url=url,method="POST",data=params,headers=headers)
res = response.json()
print(res)