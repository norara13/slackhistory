# python3.6
from slackclient import SlackClient
import requests
import json
from datetime import *
import time

#検索する文字列
memo1 ="＊情報工学科シラバス＊\n<https://syllabus.kosen-k.go.jp/Pages/PublicSubjects?school_id=15&amp;department_id=14&amp;year=2017>\n＊東京高専ホームページリンク＊\n<https://www.tokyo-ct.ac.jp/>\n＊東京高専情報工学科リンク＊\n<http://tokyo-ct.net/hp/index.html>\n＊共通認証ＩＤパスワード変更リンク＊\n<https://kidauthsv.tokyo-ct.ac.jp/iumus/>\n(東京工業高等専門学校LANからのみアクセス可能です) （編集済み）"

memo2 ="*3年情報工学科名簿*\n1    赤間    滉星\n2    五十嵐    克巳\n3    池田    凜音\n4    石田    一翔\n5    石渡    晧基\n6    伊藤    瑠也\n7    井上    流花\n8    岩田    晃広\n9    大越    朱花\n10    大塚    理史\n11    大丸    綾子\n12    小渕    晴紀\n13    久保    夏葵\n14    黒川    潤\n15    小泉    夏椰\n16    小嶋    大地\n17    佐野    友哉\n18    志賀    友哉\n19    下村    直登\n20    鈴木    康平\n21    薄田    怜\n22    多田    桃大\n23    谷崎    栄俊\n24    ﾄﾞｩﾙﾊﾞﾄﾞﾗﾊ    ﾃﾑｰﾚﾝ\n25    豊嶋    大空\n26    中田    裕一朗\n27    長田    勇我\n28    長野    航大\n29    中野    良春\n30    中村    悠哉\n31    畑中    正介\n32    林          辰宜\n33    日高    諒久\n34    福田    美樹\n35    藤澤    俊介\n36    松尾    陸\n37    松村    隼人\n38    三嶋    隆史\n39    村岡    直幸\n40    村山    莉子\n41    山川    祐汰"

memo3 ="＊2J担任 南出先生 連絡先＊\n&gt;研究室:1305室\n&gt;メールアドレス:minamide@tokyo-ct.ac.jp\n&gt;電話:設備調整中\n\n＊2J副担任 鈴木先生 連絡先＊\n&gt;研究室:7302室\n&gt;メールアドレス:suz@tokyo-ct.ac.jp\n&gt;電話:042-668-5170\n\n＊3J担任 船戸先生 連絡先＊\n&gt;研究室:1棟3階\n&gt;メールアドレス:funato@tokyo-ct.ac.jp\n&gt;電話:042-668-5149"

memo4 ="*掃除の班*\n1班：出席番号01~05\n2班：出席番号06~10\n3班：出席番号11~15\n4班：出席番号16~20\n5班：出席番号21~25\n6班：出席番号26~30\n7班：出席番号31~35\n8班：出席番号36~41"


url = "https://slack.com/api/channels.history"
token = "xoxp-132068833441-185388175377-472577771731-7735abf5496e9361f45867f477a3330e"
channel_id = "C497X0Z2P"

sc = SlackClient(token)

def main():
    
    f1 = False
    f2 = False
    f3 = False
    f4 = False
    
    payload = {
        "token": token,
        "channel": channel_id,
        }
    
#指定チャンネル内のメッセージを取得
    response = requests.get(url, params=payload)
    json_data = response.json()
    messages = json_data["messages"]

#チャンネル内のメッセージの検索と表示    
    print("-----------message-----------\n")
    for i in messages:
        print(i["text"]+"\n")
        
        if i["text"] == memo1:
            print("found!!(memo1)\n\n")
            f1 = True
            
        elif i["text"] == memo2:
            print("found!!(memo2)\n\n")
            f2 = True

        elif i["text"] == memo3:
            print("found!!(memo3)\n\n")
            f3 = True
            
        elif i["text"] == memo4:
            print("found!!(memo4)\n\n")
            f4 = True

#発見できないmemoがあったら送信する
    if f1 == False:
        sc.api_call(
            "chat.postMessage",
            channel = channel_id,
            text = memo1
        )
        print("written by memo1")
        print("memo1 =\n" + memo1 + "\n\n")

    if f2 == False:
        sc.api_call(
            "chat.postMessage",
            channel = channel_id,
            text = memo2
        )     
        print("written by memo2")
        print("memo2 =\n" + memo2 + "\n\n")
        
    if f3 == False:
        sc.api_call(
            "chat.postMessage",
            channel = channel_id,
            text = memo3
        )
        print("written by memo3")
        print("memo3 =\n" + memo3 + "\n\n")
            
    if f4 == False:
        sc.api_call(
            "chat.postMessage",
            channel = channel_id,
            text = memo4
        )
        print("written by memo4")
        print("memo4 =\n" + memo4 + "\n\n")
        
if __name__ == '__main__':
    main()