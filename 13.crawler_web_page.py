### 傳統網頁，內容由server render

# 抓取 ptt 八卦版文章標題
def printTitles(url):
    ### 用網路連線抓取網頁
    import urllib.request as req
    # 原本是 403 Forbidden
    # 為了模擬使用者發出的request，需要複製使用者真實開啟網頁時附帶的header資訊
    # 並且創造一個Request物件，改用Request 物件帶入發出請求
    request = req.Request(url,headers= {
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")


    ### 解析網頁資料
    # 安裝 beautifulsoup4
    # pip install beautifulsoup4
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    # 在html中，我們想要的標題結構長這樣:
    # <div class="title">
    #     <a href="/bbs/movie/M.1647628562.A.A75.html">[問片] 求西洋恐怖片名 投幣 籤詩 小丑 追殺</a>
    # </div>
    # 用選擇棄篩選標題
    titles = root.find_all("div", class_="title")
    for title in titles:
        # 已刪除的文章不取
        if title.a != None:
            print(title.a.string)

    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]

url="https://www.ptt.cc/bbs/Gossiping/index.html"

n = 0
while n < 3:
    url = "https://www.ptt.cc/" + printTitles(url)
    print(url)
    n+=1

