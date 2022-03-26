# # 資料型態
# n1 = 5
# n2 = 5.1
# s1 = "hello"
# s2 = 'hello'
# s3 = """hello
# world"""
# b = True
# l = [3,4,5] # List 有序可變動列表
# t = (3,4,5) # Tuple 有序不可變動列表
# s = {3,4,5} # Set
# d = {"apple":"sweet", "lemon":"sour"} # Dictionary

# # 數字運算
# c = 5%2 # 1 取餘數
# c = 3/6 # 0.5 小數除法
# c = 3//6 # 0 整數除法
# c = 2**3 # 8 2的三次方

# # 字串運算
# s = "hello" + "world"
# s = "hello" "world"
# s = "hello"*3 + "world"
# subS = s[1:4] # 取子字串
# s[0] = "a" # 與 List 不同，不能這樣替換字串內容，會出現錯誤

# # List 運算
# l = [3,4,5] + [6, 7]
# subL = l[1:4] # 取子列表 [4,5,6]
# l[1:4] = [] # 替換列表元素 [3, 7]
# length = len(l) # 列表長度
# l = [3,4,5] [6,7] # 與字串不同，不能這樣相加 list，會出現錯誤

# # Tuple 運算，不能修改，其他跟list一樣
# t = (3,4,5)
# t[0] = 5 # 出現錯誤，因為tuple不可變動

# # Set 運算
# s1 = {3,4,5}
# s2 = {4,5,6,7} 
# print(3 in s1) # 3 是否在集合中
# print(10 not in s1) # 10 是否不再集合中
# ss = s1&s2 # 交集
# ss = s1|s2 # 聯集，但不重複
# ss = s1-s2 # 差集 {3}
# ss = s1^s2 # 反交集，取兩結合中不重疊部分 {3,6,7}
# # 字串可轉為 Set
# s = set("System") # {'S', 's', 't', 'y', 'e', 'm'} 區分大小寫

# # 字典運算
# dic = {"apple":"蘋果","bug": "蟲蟲"}
# print(dic["apple"]) # 取值
# print("apple" in dic) # key 是否存在
# print("test" not in dic) # key 是否不存在
# dic["computer"] = "電腦" # 賦值
# del dic["apple"] # 刪除 key
# del dic["test"] # 刪除不存在的 key 會出現錯誤
# # 可用 List 產生字典
# dic = {x:x*2 for x in [3,4,5]}