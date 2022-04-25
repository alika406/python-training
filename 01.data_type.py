### 資料型態
## python 是動態強型別 
## 動態=> 執行時才能知道變數型別
## 強 => 不同變數不能隱式轉換
## type() => 檢查型別
n1 = 5 # int
n2 = 5.1 # float
# string
s1 = "hello"
s2 = 'hello'
s3 = """hello
world"""
# bool
b = True
l = [3,4,5] # List 有序可變動列表
t = (3,4,5) # Tuple 有序不可變動列表
s = {3,4,5} # Set
d = {"apple":"sweet", "lemon":"sour"} # Dictionary

# 數字運算
c = 5 % 2 # 1 取餘數
c = 3 / 6 # 0.5 小數除法
c = 3 // 6 # 0 整數除法
c = 2 ** 3 # 8 2的三次方

# 字串運算
s = "hello" + "world"
s = "hello" "world"
s = "hello"*3 + "world"
subS = s[1:4] # 取子字串
s[0] = "a" # 與 List 不同，不能這樣替換字串內容，會出現錯誤
print(s.replace(" ", "")) # 替換
"john, jay, jason".split(", ") # ["john", "jay", "jason"]

# bool 判斷
# 優先順序：() > not > and > or
b = True and False
b = True or False
b = not True
b = 1 in [0,1]
b = 1 not in [0, 1]
# 以下為 False
print(1, bool(False))
print(2, bool(0))
print(3, bool(''))
print(4, bool(None))
print(5, bool([]))
print(6, bool({}))

# List 創建
l1 = [3,4,5]
l2 = list("abc") # ["a", "b", "c"] , list(可迭代資料)
l3 = list(range(3)) # [0,1,2] 
l4 = range(3) # [0,1,2] 
l5 = [x*2 for x in range(3)] # [0, 2, 4]
# List 運算
l = [3,4,5] + [6, 7]
subL = l[1:4] # 取子列表 [4,5,6]
l[1:4] = [] # 替換列表元素 [3, 7]
length = len(l) # 列表長度
l = [3,4,5] [6,7] # 與字串不同，不能這樣相加 list，會出現錯誤
# 修改 List element
# 要注意別用 for loop 新增刪除元素, 跟蹤元素會出錯
l1 = [0,1,2]
for item in l1:
    item = 0 # [0,1,2] 不變，修改沒有作用
for i, v in enumerate(l1):
    l1[i] = 0 # [0,0,0] 成功
for i in range(len(l1)):
    l1[i] = 0 # [0,0,0] 成功
# 刪除List element
# 對複製的list刪除比較安全
for item in l1[:]:
    if item == 1:
        l1.remove(item)

# Tuple 運算，不能修改，其他跟list一樣
t = (3,4,5)
t[0] = 5 # 出現錯誤，因為tuple不可變動

# Set 運算
s1 = {3,4,5}
s2 = {4,5,6,7} 
print(3 in s1) # 3 是否在集合中
print(10 not in s1) # 10 是否不再集合中
ss = s1 & s2 # 交集
ss = s1 | s2 # 聯集，但不重複
ss = s1 - s2 # 差集 {3}
ss = s1 ^ s2 # 反交集，取兩結合中不重疊部分 {3,6,7}
# 字串可轉為 Set
s = set("System") # {'S', 's', 't', 'y', 'e', 'm'} 區分大小寫

# 字典運算
dic = {"apple": "蘋果","bug": "蟲蟲"}
print(dic["apple"]) # 取值
print("apple" in dic) # key 是否存在
print("test" not in dic) # key 是否不存在
dic["computer"] = "電腦" # 賦值
del dic["apple"] # 刪除 key
del dic["test"] # 刪除不存在的 key 會出現錯誤
# 可用 List 產生字典
dic = {x: x*2 for x in [3,4,5]}


## 不同型別轉換
typeD = {
    "int": 5,
    "float": 5.1,
    "str1": "010",
    "str2": "010.1",
    "str3": "010A",

}
# 數字轉字串
print(str(typeD["int"])) # "5"
print(str(typeD["float"])) # "5.1"
# 使用 f 格式化將數字轉換為字串
print(f'{typeD["int"]}')
print(f'{typeD["float"]}')

## 數字補0
# zfill 限字串使用
print("10".zfill(5)) # "00010"
# 格式化方式, int float string 皆可使用
print('%05d' % 123) # "00123"
# format
print('{0:05d}'.format(123)) # "00123"

## 數字取小數位
# round 四捨五入
print(round(3.1415, 2)) # 3.14
# 格式化方式
print('%.2f' % 3.1415) # 3.14
# format
print('{:.2f}'.format(3.1415)) #3.14

# 字串轉數字
print(int(typeD["str1"])) # 10
print(int(typeD["str2"])) # error
print(float(typeD["str1"])) # 10.0
print(float(typeD["str2"])) # 10.1
print(float(typeD["str3"])) # error
# 使用列表推導方法將字串轉成數字
A = (('90','88'),('78','56'),('2','4','6'))
B = [list(map(int, x)) for x in A] # [[90, 88], [78, 56], [2, 4, 6]]


# 字串轉任和型別變數
sl = "[1, 2, 3]"
l1 = eval(s1) # 會有安全隱憂，因為eval內可以插入可執行程式片段
import ast
l2 = ast.literal_eval(s1) # 只會轉換合法的python類型，其他會報錯

# 排序
# sorted => 可排序可迭代資料
# list.sort() => 會改變list資料
students = [
    {"john", 10},
    {"jay", 5}
]
d = sorted(students, key = lambda student: student[2], reverse=True)