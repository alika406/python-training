# 可疊代資料 Iterable: 可分開、逐一取出內部資料
# 字串、列表、集合、字典

# for 迴圈
# for 變數名稱 in 可疊代資料:
for x in {"a", "test", 8, 10}: # 集合不照順序的
    print(x)
dic = {"a":3, "x":5}
for key in dic:
    print(key)
    print(dic[key])


# 內建函式
# max(可疊代資料)
# sorted(可疊代資料)
result =  max("hello873#@*&HELLO")
print(result) # o
result =  sorted("hello873#@*&HELLO")
print(result) # ['#', '&', '*', '3', '7', '8', '@', 'E', 'H', 'L', 'L', 'O', 'e', 'h', 'l', 'l', 'o'] 

result = max({"x":3,"a":4})
print(result) # x => 以Key判斷
