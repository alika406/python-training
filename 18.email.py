# 到google帳戶 -> 安全性 -> App 密碼(如果有開啟兩段式驗證)
import email.message
myEmail = "wentzu.ku.au@gmail.com"
appPWD = "nbokltnnbfclxznp"
msg = email.message.EmailMessage()
msg["From"] = myEmail
msg["To"] = myEmail
msg["Subject"] = "你好"
# 寄送純文字內容
# msg.set_content("測試看看")
# 寄送複雜樣式內容
msg.add_alternative("<h3>優惠券</h3>買五百送一百喔", subtype="html")

## 連線到SMTP Server, 驗證寄件人身分並發送郵件
import smtplib
# 網路搜尋google smtp server 就找的到
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(myEmail, appPWD)
server.send_message(msg)
server.close()