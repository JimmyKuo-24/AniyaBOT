from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from line_bot import *
from bs4 import BeautifulSoup
import re, requests, twstock, datetime, Msg_Template, mongodb, EXRate

app = Flask(__name__)

def cache_users_stock():
    db = mongodb.constructor_stock()
    nameList = db.list_collection_names()
    users = []
    for i in range(len(nameList)):
        collect = db[nameList[i]]
        cel = list(collect.find({'tag': 'stock'}))
        users.append(cel)
    return users

def oil_price():
    target_url = 'https://gas.goodlife.tw/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.select('#main')[0].text.replace('\n', '').split("(")[0]
    gas_price = soup.select('#gas-price')[0].text.replace('\n\n\n', '').replace(' ', '')
    cpc = soup.select('#cpc')[0].text.replace(' ', '')
    content = '{}\n{}{}'.format(title, gas_price, cpc)
    return content

def push_msg(event, msg):   # 推播訊息 free 200則/月
    try:
        user_id = event.source.user_id
        line_bot_api.push_message(user_id, TextSendMessage(text=msg))
    except:
        room_id = event.source.user_id
        line_bot_api.push_message(room_id, TextSendMessage(text=msg))

def Usage(event):
    guide_msg = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://i.imgur.com/DzvWgBs.jpg",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
            "type": "uri",
            "uri": "https://line.me/"
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "✯ ✯ ✯ 查詢方法 ✯ ✯ ✯",
                "weight": "bold",
                "size": "lg",
                "align": "center"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "請輸入，Aniya可查油價及匯率！",
                        "size": "md",
                        "flex": 5,
                        "align": "center",
                        "weight": "bold"
                    }
                    ]
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "☸ 今日油價➦輸入➦查詢油價",
                        "size": "sm",
                        "flex": 5,
                        "weight": "bold"
                    }
                    ]
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "☸ 今日匯率➦輸入➦查詢匯率",
                        "size": "sm",
                        "flex": 5,
                        "weight": "bold"
                    }
                    ]
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "☸ 匯率兌換➦輸入➦換匯USD/TWD/100",
                        "size": "sm",
                        "flex": 5,
                        "weight": "bold"
                    }
                    ]
                }
                ]
            }
            ]
        },
        "styles": {
            "body": {
            "backgroundColor": "#F8EDED"
            }
        }
    }
    line_bot_api.reply_message(
        event.reply_token,
        FlexSendMessage(alt_text='使用說明', contents=guide_msg)
    )

@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info('Invalid signature. Please check your channel access token/chanel secret.')
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text))
    msg = str(event.message.text).upper().strip()
    profile = line_bot_api.get_profile(event.source.user_id)

    usespeak = str(event.message.text)
    uid = profile.user_id
    user_name = profile.display_name

    #################################### 目錄區 ##########################################

    if event.message.text == '油價查詢':
        content = oil_price()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content)
        )
    if event.message.text == '使用說明':
        Usage(event)
        
    if event.message.text == 'Aniya':
        message = TemplateSendMessage(
        alt_text='目錄 template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/bGyGdb1.jpg',
                        title='股市專區',
                        text='選擇服務',
                        actions=[
                            MessageAction(
                                label='股價查詢',
                                text='股價查詢'
                            ),
                            URIAction(
                                label='財經新聞',
                                uri='https://news.cnyes.com/news/cat/headline'
                            ),
                            URIAction(
                                label='財經M平方',
                                uri='https://www.macromicro.me/'
                            )
                        ]
                    ),
                CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/rwR2yUr.jpg',
                        title='外匯專區',
                        text='選擇服務',
                        actions=[
                            URIAction(
                                label='臺銀匯率',
                                uri='https://rate.bot.com.tw/xrt?Lang=zh-Tw'
                            ),
                            URIAction(
                                label='匯率與指數',
                                uri='https://www.macromicro.me/charts/49426/mei-yuan-tai-bi-hui-lyu-vs-tai-wan-jia-quan-zhi-shu'
                            ),
                            URIAction(
                                label='youtube 小Lin說',
                                uri='https://www.youtube.com/@xiao_lin_shuo'
                            )
                        ]
                    ),
                CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/AxEsJsv.jpg',
                        title='能源專區',
                        text='選擇服務',
                        actions=[
                            MessageAction(
                                label='油價查詢',
                                text='油價查詢',
                            ),
                            URIAction(
                                label='原油基本面指數',
                                uri='https://www.macromicro.me/collections/19/mm-oil-price/182/mm-oil-expectation-index'
                            ),
                            URIAction(
                                label='石油供需平衡及預期',
                                uri='https://www.macromicro.me/collections/19/mm-oil-price/31581/world-petroleum-and-other-liquids-production-consumption'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    if re.match('財經學堂', msg):
        content = Msg_Template.yt_channel()
        line_bot_api.push_message(uid, content)
        return 0

    #################################### 股票區 ##########################################

    if event.message.text == '股價查詢':
        line_bot_api.push_message(uid, TextSendMessage('請輸入股票代號：#xxxx'))

    if re.match('關注[0-9]{4}[<>][0-9]', msg):
        stockNumber = msg[2:6]
        content = mongodb.write_my_stock(uid, user_name, stockNumber, msg[6:7], msg[7:])
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    
    if re.match('股票清單', msg):
        line_bot_api.push_message(uid, TextSendMessage('waiting..., 股票查詢中...'))
        content = mongodb.show_my_stock(user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    
    if re.match('刪除[0-9]{4}', msg):
        content = mongodb.delete_my_stock(user_name, msg[2:])
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    
    if re.match('清空股票', msg):
        content = mongodb.delete_my_allstock(user_name)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0

    if (msg.startswith('#')):
        text = msg[1:]
        content = ''

        stock_rt = twstock.realtime.get(text)
        my_datetime = datetime.datetime.fromtimestamp(stock_rt['timestamp']+8*60*60)
        my_time = my_datetime.strftime('%H:%M:%S')

        content += '%s (%s) %s\n' %(
            stock_rt['info']['name'],
            stock_rt['info']['code'],
            my_time)
        content += '現價: %s / 開盤: %s\n'%(
            stock_rt['realtime']['latest_trade_price'],
            stock_rt['realtime']['open'])
        content += '最高價: %s / 最低價: %s\n' %(
            stock_rt['realtime']['high'],
            stock_rt['realtime']['low'])
        content += '成交量: %s\n' %(stock_rt['realtime']['accumulate_trade_volume'])

        stock = twstock.Stock(text)#twstock.Stock('2330')
        content += '-----\n'
        content += '最近五日價格: \n'
        price5 = stock.price[-5:][::-1]
        date5 = stock.date[-5:][::-1]
        for i in range(len(price5)):
            #content += '[%s] %s\n' %(date5[i].strftime("%Y-%m-%d %H:%M:%S"), price5[i])
            content += '[%s] %s\n' %(date5[i].strftime("%Y-%m-%d"), price5[i])
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content)
        )

    if re.match('關閉提醒', msg):
        import schedule
        schedule.clear()

    if re.match('股價提醒', msg):
        import schedule
        import time
        def look_stock_price(stock, condition, price, userID):
            print(userID)
            url = 'https://tw.stock.yahoo.com/q/q?s=' + stock
            list_req = requests.get(url)
            soup = BeautifulSoup(list_req.content, 'html.parser')
            getstock = soup.find('span', class_='Fz(32px)').string
            content = stock + '當前股價為：' + getstock
            if condition == '<':
                content = '\n篩選條件為：<' + price
                if float(getstock) < float(price):
                    content += '\n符合' + getstock + '<' + price + '的篩選條件'
                    line_bot_api.push_message(userID, TextSendMessage(text=content))
            elif condition == '>':
                content = '\n篩選條件為：>' + price
                if float(getstock) > float(price):
                    content += '\n符合' + getstock + '>' + price + '的篩選條件'
                    line_bot_api.push_message(userID, TextSendMessage(text=content))
            elif condition == '=':
                content = '\n篩選條件為：=' + price
                if float(getstock) > float(price):
                    content += '\n符合' + getstock + '=' + price + '的篩選條件'
                    line_bot_api.push_message(userID, TextSendMessage(text=content))
        
        def job():
            print('HH')
            datalist = cache_users_stock()
            for i in range(len(datalist)):
                for j in range(len(datalist[i])):
                    look_stock_price(datalist[i][j]['favorite_stock'], datalist[i][j]['condition'], datalist[i][j]['price'], datalist[i][j]['userID'])

        schedule.every(10).seconds.do(job).tag('dalily'+uid, 'second')


    #################################### 外匯區 ##########################################

    if re.match('幣別種類', msg):
        message = Msg_Template.show_Button()
        line_bot_api.reply_message(event.reply_token, message)

    if re.match('[A-Z]{3}', msg):
        currency_name = EXRate.getCurrencyName(msg)
        if currency_name == "無可支援的外幣": content = "無可支援的外幣"
        else:
            line_bot_api.push_message(uid, TextSendMessage('waiting..., 匯率查詢中...'))
            content = EXRate.showCurrency(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0

    if re.match('新增外幣[A-Z]{3}', msg):
        currency = msg[4:7]
        currency_name = EXRate.getCurrencyName(currency)
        if currency_name == "無可支援的外幣": content = "無可支援的外幣"
        elif re.match('新增外幣[A-Z]{3}[<>][0-9]', msg):
            content = mongodb.write_my_currency(uid , user_name, currency, msg[7:8], msg[8:])
        else:
            content = mongodb.write_my_currency(uid , user_name, currency, "未設定", "未設定")
        
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0

    if re.match('匯率大小事', msg):
        btn_msg = Msg_Template.stock_reply_rate()
        line_bot_api.push_message(uid, btn_msg)
        return 0
    
    if re.match('換匯[A-Z]{3}/[A-Z]{3}/[0-9]', msg):
        line_bot_api.push_message(uid, TextSendMessage('waiting..., 換匯計算中...'))
        content = EXRate.getExchangeRate(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    
    if re.match('外幣清單', msg):
        line_bot_api.push_message(uid, TextSendMessage('waiting..., 外幣查詢中...'))
        content = mongodb.show_my_currency(uid, user_name)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    
    if re.match('刪除外幣[A-Z]{3}', msg):
        currency = mongodb.delete_my_currency(user_name, msg[4:7])
        line_bot_api.push_message(uid, TextSendMessage(currency))
        return 0
    
    if re.match('清空外幣', msg):
        content = mongodb.delete_my_allcurrency(user_name)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0


@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://i.imgur.com/NakSo51.jpg",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
            "type": "uri",
            "uri": "https://line.me/"
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "歡迎您成為Aniya Millionaire好友！",
                "weight": "bold",
                "size": "md"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Aniya是一個機器人，提供最新的財經資訊",
                        "size": "sm",
                        "flex": 5,
                        "align": "center",
                        "weight": "regular"
                    }
                    ]
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "★★ 這裡有 股票、匯率、油價 資訊",
                        "size": "sm",
                        "flex": 5
                    }
                    ]
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "★★ 直接點選下方【目錄】選單功能",
                        "size": "sm",
                        "flex": 5
                    }
                    ]
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "期待您的光臨 Waku Waku",
                        "size": "sm",
                        "flex": 5,
                        "align": "center"
                    }
                    ]
                }
                ]
            }
            ]
        },
        "styles": {
            "body": {
            "backgroundColor": "#FFEEAD"
            }
        }
    }

    line_bot_api.reply_message(
        event.reply_token,
        FlexSendMessage(alt_text='歡迎訊息', contents=welcome_msg)
    )

@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)


if __name__ == '__main__':
    app.run()


