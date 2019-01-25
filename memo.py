# python3.6
from slackclient import SlackClient
import requests
import json
from datetime import *
import time

#検索する文字列
#hogeを検索
memo1 ="hoge"

#hogehogeを検索
memo2 ="hogehoge"

#hoge    hogeを検索
memo3 ="hoge    hoge"

#改行してある文章を検索したい場合\nを付けて検索
memo4 ="hoge\nhoge"


url = "https://slack.com/api/channels.history"
token = ""
channel_id = ""

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