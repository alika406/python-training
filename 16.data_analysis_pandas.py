# 要安裝 pandas
# pip install pandas
import pandas as pd

### 單維度資料 series
# 0    20
# 1    10
# 2    15
# dtype: int64
# 要帶入 list 資料
sData = pd.Series([20,10,15])
print(sData.max()) # 最大值
print(sData.median()) # 中位數
sData2 = sData * 2 # 每個資料乘以2{也可以做其他運算)
print(sData==20) # 檢查每列資料是不是等於20


### 雙維度資料 DataFrame
#    name  salary
# a   Amy   30000
# b  John  500000
# c   Bob  400000
# 要帶入字典資料
dData = pd.DataFrame({
    "name": ["Amy", "John", "Bob"],
    "salary": [30000, 50000, 40000]
# 索引可以不帶，預設是 0,1,2...
}, index=["a", "b", "c"])

print(dData.size) # 欄 * 列
print(dData.shape) # (列, 欄) (3,2)
print(dData.index) # Index(['a', 'b', 'c'], dtype='object')
print(dData.iloc[1]) # 取得第二列
print(dData.loc["c"]) # 按照index取得特定列
print(dData["name"]) # 取得特定欄位
# 取出的特定欄或列就是Series，可以做特定操作
print(dData["name"].str.upper())
print(dData["salary"].mean())
# 建立新欄位
dData["revenue"] =[500000, 400000, 300000] # 創造的營收，簡單的寫法
dData["rank"] = pd.Series([3,6,1], index=["a","b","c"]) # 正式的寫法
dData["cp"] = dData["revenue"]/dData["salary"] # 利用其他欄位計算
print(dData)



### 資料篩選
## Series
data = pd.Series([30,15,20])
condition = [True,False,True] # 指定篩選
condition = data > 18 # 條件篩選
filterData = data[condition]
print(filterData)
## DataFrame
data = pd.DataFrame({
    "name": ["Amy","Bob","Charles"],
    "salary": [30000, 50000, 40000]
})
condition = [False, True,True] # 指定篩選
condition = data["salary"] > 40000 # 條件篩選
condition = data["name"] == "Amy" # 條件篩選
filterdData = [condition]
print(filterData)