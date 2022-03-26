# 開啟模式
# 讀取模式 - r
# 寫入模式 - W
# 讀寫模式 - r+

### 儲存檔案
# 如果檔案不存在會新增，檔案存在寫入會覆蓋
# 基本上不是英文，沒設定encoding 會亂碼
file = open("data.txt", mode="w", encoding="utf-8")
file.write("測試中文\n好棒棒")
file.close()

### 最佳實務，會自動close file
# 寫
with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n3")
# 讀
with open("data.txt", mode="r", encoding="utf-8") as file:
    data=file.read() # 取得整個內容
    for line in file: # 或是可以一行一行讀取
        print(line) 
print(data)

### 讀取json格式
# 有一檔案 config.json
# {
#     "name": "my name",
#     "version": "1.2.3"
# }
import json
# 讀
with open("config.json", mode="r") as file:
    data = json.load(file) # data 是一個字典資料
print(data)
data["name"] ="New name"
# 寫
with open("config.json", mode="w",) as file:
    json.dump(data, file)