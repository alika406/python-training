### 非同步網頁，內容是透過 ajax 另外request 得到再改變到網頁上
# 還沒找到適合實作的網站所以先照教學打(原本的範例網頁改版了) medium.com抓首頁文章
import urllib.request as req
import json
url = "htpp://medium.com/_/api/graphql"

### 製造 request 物件
# request data (request payload, request body)
# 複雜請求時，client 需要提供 request data 給 server (以下資料室我隨便複製的，僅供參考)
requestData = [{"operationName":"CollectionViewerEdge","variables":{"collectionId":"40187e704f1c"},"query":"query CollectionViewerEdge($collectionId: ID!) {\n  collection(id: $collectionId) {\n    ... on Collection {\n      id\n      viewerEdge {\n        ...Collection_viewerEdge\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment Collection_viewerEdge on CollectionViewerEdge {\n  id\n  canEditOwnPosts\n  canEditPosts\n  isEditor\n  isFollowing\n  isMuting\n  isSubscribedToLetters\n  isSubscribedToMediumNewsletter\n  isSubscribedToEmails\n  isWriter\n  __typename\n}\n"},{"operationName":"CollectionViewerEdge","variables":{"collectionId":"3f6ecf56618"},"query":"query CollectionViewerEdge($collectionId: ID!) {\n  collection(id: $collectionId) {\n    ... on Collection {\n      id\n      viewerEdge {\n        ...Collection_viewerEdge\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment Collection_viewerEdge on CollectionViewerEdge {\n  id\n  canEditOwnPosts\n  canEditPosts\n  isEditor\n  isFollowing\n  isMuting\n  isSubscribedToLetters\n  isSubscribedToMediumNewsletter\n  isSubscribedToEmails\n  isWriter\n  __typename\n}\n"}]
request = req.Request(url, headers={
    "Content-Type": "application/json",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
# request data 需轉成字串且編碼
}, data = json.dumps(requestData).encode("utf-8"))

# 抓資料
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

# 印出標題
data = json.load(data)
items = data["data"]["extenededFeedItems"]
for item in items:
    print(item["post"]["title"])

