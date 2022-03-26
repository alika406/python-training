# 定義
def say(msg):
    print(msg)
    return
# 呼叫
value = say("Hello") # 沒有寫return或是 return 後面沒接值，回傳 None
print(value)

# 參數的預設值   
def power(base, exp=0):
    print(base**exp)
power(3,2)
power(4)

# 參數的名稱對應
def divide(n1, n2):
    print(n1/n2)
divide(2,4)
divide(n2=2,n1=4)

# 無限/不定參數
# 平均數 function
def avg(*ns): # 加上*字號可以傳入不定長度的參數
    sum = 0
    for n in ns: # 傳入的參數為 tuple 型態
        sum+=n
    print(sum/len(ns))
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)
