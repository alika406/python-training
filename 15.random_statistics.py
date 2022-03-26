### 隨機模組
import random
# 隨機取一
data = random.choice([5,3,7,3])
# 隨機取多
data = random.sample([5,3,7,3], 3)
# 洗牌，直接改變變數資料
data = [5,3,7,3]
random.shuffle(data)
print(data)
# 隨機取得亂數
data = random.random() # 0 ~ 1 隨機亂數
data = random.uniform(60, 100) # 隨機亂數(可指定區間，有福點數)
data = random.normalvariate(100, 10) # 常態分配亂數，設定平均數100標準差10，得到的亂數多數在90~110之間


### 統計婆組
import statistics as stat
data = stat.mean([6,30,38,70,3,4,200]) # 平均數
data = stat.median([6,30,38,70,3,4,200]) # 中位數
data = stat.stdev([6,30,38,70,3,4,200]) # 標準差(資料散布情況)
