### 執行順序: 裝飾器內部程式碼-> 被裝飾器程式碼
### 定義一個裝飾器，計算1+2+...+50總和
def calculate(cb):
    def run():
        n = 0
        for i in range(51):
            n+=i
        cb(n) # 這個cb其實就是被裝飾器showChinese,showEnglish
    return run

# 使用裝飾器
@calculate
def showChinese(n):
    print("總和是", n)

@calculate
def showEnglish(n):
    print("Result is", n)
showChinese()
showEnglish()


### 裝飾器工廠
# 裝飾器工廠的結構其實就是在裝飾器外再包一層function
# 裝飾器工廠跟裝飾器不同之處就是裝飾器工廠可以代入參數

# 計算 1+2+...n
def calculateFactory(n):
    def calculateDeco(cb):
        def run():
            result = 0
            for i in range(n+1):
                result+=i
            cb(result)
        return run
    return calculateDeco

@calculateFactory(10)
def show(n):
    print("結果是", n)

@calculateFactory(10)
def showEng(n):
    print("Result is", n)

show()
showEng()
