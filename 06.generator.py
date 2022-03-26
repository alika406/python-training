# 定義生成器函式
def test():
    print("階段一")
    yield 5
    print("階段二")
    yield 10

gen = test() # 會得到一個生成器，此時函數內容還沒執行
print(gen) # <generator object test at 0x000001E2868F9CB0>

# genarator 是一個可疊代物件
# 此時才開始執行函數內容
for d in gen:
    print(d)
# 階段一
# 5
# 階段二
# 10

### 取得大於0的偶數
def genarateEven(maxNumber):
    n = 2
    while n <= maxNumber:
        yield n
        n+=2

gen = genarateEven(20)
for n in gen:
    print(n)