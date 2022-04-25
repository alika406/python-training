try:
    print("Hello")
    # print(x)
    # 自己丟出錯誤
    raise Exception("Sorry, no numbers below zero")
except NameError: # 抓取特定錯誤
    print("Variable x is not defined")
except: # 抓取所有沒有歸類的錯誤
    print("Something went wrong")
else: # 執行完 try 沒有錯誤才會執行
    print("Nothing went wrong")
finally: # 不管有沒有錯誤，最後執行，比else晚執行
  print("The 'try except' is finished")