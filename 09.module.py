### 載入內建的 sys 模組
import sys as s # 或是直接 import sys
print(s.platform)
print(s.maxsize)
print(s.path) # 印出模組的搜尋路徑，預設會加入專案資料夾?

### 自定義模組
## 模組檔案 專案資料夾/modules/geometry.py
# 計算兩點距離
def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
# 計算線段斜率
def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

## 在其他檔案載入自定義模組
import sys
sys.path.append("modules") # 調整搜尋模組路徑，手動加入自己新增的模組資料夾相對路徑
import geometry
result=geometry.distance(1,1,5,5)
print(result)
result=geometry.slope(1,2,5,6)
print(result)