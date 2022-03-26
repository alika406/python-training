### 觀念
### 模組 => module 是檔案
### 封包 => package 放 module 檔案的資料夾

# -專案檔案配置
#   - 專案資料夾
#     - 主程式.py
#     - geometry # 封包資料夾
#         - __init__.py # 有要這檔案(可以是空的但是要有)才會被認為是封包資料夾
#         - point.py
#         - line.py

## 載入
import geometry.point
result = geometry.point.distance(3,4)
print(result)
import geometry.line as line
result = line.slope(1,1,3,3)
print(result)
