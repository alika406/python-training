# 網路連線抓取資料
import urllib.request as request
import json
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    # # 取得html或是該網址提供的資料格式中文
    # # 中文會以奇怪編碼表示，解碼就能正常顯示
    # data=response.read().decode("utf-8") 

    # 轉換json格式(中文自動轉換)
    data = json.load(response)

# 將公司名稱列表存成檔案
clist = data["result"]["results"]
with open("data.txt", mode="w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")


