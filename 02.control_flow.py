# # if else 判斷式
# x = input("請輸入數字:") # 取得字串型式的使用者輸入
# x = int(X)
# if x > 200:
#     print("大於 200")
# elif x > 100: 
#     print("大於 100, 小於 200")
# else:
#     print("小於 100")

# # while 迴圈
# n = 1
# while n < 5:
#     print("n=", n)
#     n+=1

# # for 迴圈
# for c in "hello":
#     print(c)
# for x in [4, 2, 1]:
#     print(x)
# # 常與 range()搭配使用
# for x in range(3): # 相當於 in [0,1,2]
# for x in range(3, 6): # 相當於 in [3,4,5]

# # break, continue
# n = 0
# sum = 0
# while n < 10:
#     n+=1
#     if sum > 15: 
#         break
#     if n % 2 == 0:
#         continue    
#     sum+=n
# print(sum)

# # 迴圈的 else 可以用在 while 與 for 迴圈
# # 例子: 找整數平方根
# n = input("請輸入數字:")
# n = int(n)
# for i in range(n):
#     if i*i == n:
#         print(i)
#         break # 用 break 中斷迴圈就不會執行 else
# else: # 正常結束迴圈後會執行
#     print("沒有整數平方根")
