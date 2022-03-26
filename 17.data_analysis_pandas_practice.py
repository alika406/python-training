### 分析 google play store 資料
### 下載網址: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa19mZllicnV2MjNTR0lVNFhIcmRDY2IzTHQyUXxBQ3Jtc0tuQmVDVzRXU2c5T0ZSNnVyVk1XTXJIRHRKdHlkV01odjdJaDhvZVpXcEtiSHIyd0kyV3NaRklabWVCN1JBbWV0bU42UkZvN2M0OS1wbWRWNE0yd0VGYVRGV0FKN1JUMXUtdFIxNGRWUFFJNmhoVExNNA&q=https%3A%2F%2Fcwpeng.github.io%2Flive-records-samples%2Fdata%2Fgoogleplaystore.csv

### 簡單的資料工程步驟
# - 蒐集資料 -> 下載、讀取
# - 清洗資料
# - 分析資料
# - 基於資料的運用

from ctypes import cdll
import pandas as pd
data = pd.read_csv("googleplaystore.csv")
print("資料數量", data.shape)
print("資料欄位", data.columns)
print("平均數", data["Rating"].mean())
print("中位數", data["Rating"].median())

## 清洗資料
# 發現高於5分，不合理
print("取前一百高的應用程式評分平均", data["Rating"].nlargest(100).mean())
# 觀察到有一筆資料高於5分
condition = data["Rating"] > 5
cData = data[condition]
print(cData)
# 清洗掉奇怪資料
condition = data["Rating"] <= 5
data = data[condition]
print("取前一百高的應用程式評分平均", data["Rating"].nlargest(100).mean())
# 將安裝數由字串 500,000+改為數字，順便清洗掉非數字資料列
data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))

## 分析資料: 安裝數量更腫統計數據
print("平均數", data["Installs"].mean())
condition = data["Installs"] > 100000
print("安裝數量大於 10萬有幾個", data[condition].shape[0])

## 資料運用
keyword = input("請輸入關鍵字: ")
# 可設定忽略大小寫
condition = data["App"].str.contains(keyword, case=False)
print("搜尋結果數量", data[condition].shape[0])