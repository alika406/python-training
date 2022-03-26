### 直接使用 class
# 定定義 class
class IO:
    suportedSrcs=["console", "file"]
    def read(src):
        if src not in IO.suportedSrcs:
            print("Not supported")
        else:
            print("Read from", src)

# 使用 class
print (IO.suportedSrcs)
IO.read("file")
IO.read("internet")


### 建立物件
class Point:
    # 初始化
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def distance(self, targetX, targetY):
        return ((self.x-targetX)**2 + (self.y-targetY)**2)**0.5

p = Point(3,4)
p.show()
result = p.distance(0,0)
print(result)