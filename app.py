from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from line_bot import *
from bs4 import BeautifulSoup
import datetime, EXRate, re, requests, schedule, time, twstock, mongodb, mplfinance as mpf, Msg_Template, pyimgur, yfinance as yf
from openai import OpenAI

app = Flask(__name__)
IMGUR_CLIENT_ID = '377a9d38e49c276'

# push_message free 200則/月

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

@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = Msg_Template.follow_msg()
    line_bot_api.reply_message(event.reply_token, welcome_msg)

@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)

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

def plot_stock_k_chart(IMGUR_CLIENT_ID, stock='0050', date_from='2021-01-01'):
    stock = str(stock) + '.TW'
    try:
        print(f'正在獲取股票數據: {stock}')
        df = yf.download(stock, start=date_from)

        if df is None or df.empty:
            print(f'股票數據: {stock} 無法取得')
            return None

        print(f'正在繪製股票K線圖: {stock}')
        mpf.plot(df, type='candle', mav=(5, 20), volume=True, ylabel=stock.upper() + 'Price', savefig=f'{stock}.png')

        PATH = f'{stock}.png'
        im = pyimgur.Imgur(IMGUR_CLIENT_ID)
        uploaded_image = im.upload_image(PATH, title=f'{stock} K-Chart')
        print(f'已上傳圖片: {uploaded_image.link}')
        return uploaded_image.link
    except Exception as e:
        print(f'錯誤: {e}')
        return None

def push_msg(event, msg):
    try:
        user_id = event.source.user_id
        line_bot_api.push_message(user_id, TextSendMessage(text=msg))
    except:
        room_id = event.source.user_id
        line_bot_api.push_message(room_id, TextSendMessage(text=msg))

def Usage(event):
    guide_msg = Msg_Template.usage_msg()
    line_bot_api.reply_message(event.reply_token, guide_msg)

    
def volume0000():
    rs0 = requests.session()
    res = rs0.get('https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?response=html')
    res.encoding = 'utf8'
    soup = BeautifulSoup(res.text, 'html.parser')
    date = soup.find_all('th')[0].text[:11].replace('\n','')
    volume_0000 = round(int(soup.find_all('td')[-18].text.replace(',',''))/10**8)
    
    return date, volume_0000

def II3():   # institutional investors 三大法人
    rs1 = requests.session()
    res = rs1.get('https://www.twse.com.tw/rwd/zh/fund/BFI82U?response=html')
    res.encoding = 'utf8'
    soup = BeautifulSoup(res.text, 'html.parser')
    
    foreign_investors = round(int(soup.find_all('td')[15].text.replace(',',''))/10**8)
    investment_trust = round(int(soup.find_all('td')[11].text.replace(',',''))/10**8)
    dealer = int(soup.find_all('td')[3].text.replace(',',''))/10**8
    dealer_hedge = int(soup.find_all('td')[7].text.replace(',',''))/10**8
    DEALER = round(dealer + dealer_hedge)

    return foreign_investors, investment_trust, DEALER

def FI_futures():
    rs2 = requests.session()
    res = rs2.get('https://www.taifex.com.tw/cht/3/futContractsDate')
    res.encoding = 'utf8'
    soup = BeautifulSoup(res.text, 'html.parser')
    big = soup.find_all('td')[39].text.replace(',','')
    small = soup.find_all('td')[162].text.replace(',','')
    micro = soup.find_all('td')[203].text.replace(',','')
    LOTS = round(int(big) + int(small)/4 + int(micro)/20)
    
    return LOTS

def futures_large():
    rs3 = requests.session()
    res = rs3.get('https://www.taifex.com.tw/cht/3/largeTraderFutQry')
    res.encoding = 'utf8'
    soup = BeautifulSoup(res.text, 'html.parser')
    B5 = soup.find_all('td')[22].text.replace(',','').split()
    S5 = soup.find_all('td')[26].text.replace(',','').split()
    large5 = int(B5[0]) - int(S5[0])
    B10 = soup.find_all('td')[24].text.replace(',','').split()
    S10 = soup.find_all('td')[28].text.replace(',','').split()
    large10 = int(B10[0]) - int(S10[0])

    return large5, large10

def PCR():
    rs4 = requests.session()
    res = rs4.get('https://www.taifex.com.tw/cht/3/pcRatio')
    res.encoding = 'utf8'
    soup = BeautifulSoup(res.text, 'html.parser')
    pcr = eval(soup.find_all('td')[6].text)
    
    return pcr

def putcall():
    rs5 = requests.session()
    res = rs5.get('https://www.taifex.com.tw/cht/3/callsAndPutsDate')
    res.encoding = 'utf8'
    soup = BeautifulSoup(res.text, 'html.parser')
    fcall = soup.find_all('td')[41].text.replace(',','').split()
    fput = soup.find_all('td')[81].text.replace(',','').split()
    FPC = (int(fcall[0]) - int(fput[0]))/10**5

    return FPC


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
    msg = str(event.message.text).upper().strip()
    profile = line_bot_api.get_profile(event.source.user_id)

    usespeak = str(event.message.text)
    uid = profile.user_id
    user_name = profile.display_name

    # if re.match('hi ai:', event.message.text):
    #     client = OpenAI(api_key = 'YOUR_API_KEY')
    #     response = client.chat.completions.create(
    #         model="gpt-3.5-turbo-instruct",
    #         max_tokens=256,
    #         temperature=0.7,
    #         messages=[
    #             {"role": "system", "content": "You are a helpful assistant."},
    #             {"role": "user", "content": "Hello!"}
    #         ],
    #     )
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=response.choices[0].text.replace('\n', '')))

    #################################### 目錄區 ##########################################
    
    if msg == '使用說明':
        Usage(event)
        
    if msg == 'Aniya':
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
                        title='匯率專區',
                        text='選擇服務',
                        actions=[
                            URIAction(
                                label='臺銀匯率',
                                uri='https://liff.line.me/2006134064-X1yPGZyA'
                            ),
                            URIAction(
                                label='匯率與指數',
                                uri='https://www.macromicro.me/charts/49426/mei-yuan-tai-bi-hui-lyu-vs-tai-wan-jia-quan-zhi-shu'
                            ),
                            URIAction(
                                label='youtube 小翠時政財經',
                                uri='https://www.youtube.com/channel/UCOhck8oLoIwSJzmwYMXsSnQ'
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

    if msg == '油價查詢':
        content = oil_price()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
    
    if msg == '財經學堂':
        content = Msg_Template.yt_channel()
        line_bot_api.reply_message(event.reply_token, content)

    #################################### 股票區 ##########################################

    # if msg == '分析趨勢':
    #     message = Msg_Template.stock_reply_other()
    #     line_bot_api.reply_message(event.reply_token, message)

    if msg == '股價查詢':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入：#股票代號'))

    if msg.startswith('#'):
        if msg[1:6].isdigit():
            text=msg[1:6]
        else:
            text=msg[1:5]
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
            # content += '[%s] %s\n' %(date5[i].strftime("%Y-%m-%d %H:%M:%S"), price5[i])
            content += '[%s] %s\n' %(date5[i].strftime("%Y-%m-%d"), price5[i])

        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))

    if re.match('關注[0-9]{4}[<=>][0-9]', msg):
        stockNumber = msg[2:6]
        content = mongodb.write_my_stock(uid, user_name, stockNumber, msg[6:7], msg[7:])
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))
    elif re.match('關注[0-9]{5}[<=>][0-9]', msg):
        stockNumber = msg[2:7]
        content = mongodb.write_my_stock(uid, user_name, stockNumber, msg[7:8], msg[8:])
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))

    # if re.match('關注[0-9]{4}[<>][0-9]', msg):
    #     stockNumber = msg[2:6]
    #     content = mongodb.write_my_stock(uid, user_name, stockNumber, msg[6:7], msg[7:])
    #     line_bot_api.push_message(uid, TextSendMessage(content))
    #     return 0
    
    if re.match('股票清單', msg):
        content = mongodb.show_my_stock(user_name, uid)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))

    # if re.match('股票清單', msg):
    #     line_bot_api.push_message(uid, TextSendMessage('waiting..., 股票查詢中...'))
    #     content = mongodb.show_my_stock(user_name, uid)
    #     line_bot_api.push_message(uid, TextSendMessage(content))
    #     return 0
    
    if re.match('刪除[0-9]{4}', msg):
        content = mongodb.delete_my_stock(user_name, msg[2:])
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))
    elif re.match('刪除[0-9]{5}', msg):
        content = mongodb.delete_my_stock(user_name, msg[2:])
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))

    # if re.match('刪除[0-9]{4}', msg):
    #     content = mongodb.delete_my_stock(user_name, msg[2:])
    #     line_bot_api.push_message(uid, TextSendMessage(content))
    #     return 0
    
    if re.match('清空股票', msg):
        content = mongodb.delete_my_allstock(user_name)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))

    # if re.match('清空股票', msg):
    #     content = mongodb.delete_my_allstock(user_name)
    #     line_bot_api.push_message(uid, TextSendMessage(content))
    #     return 0

    if re.match('關閉提醒', msg):
        schedule.clear()

    if re.match('股價提醒', msg):
        def look_stock_price(stock, condition, price, userID):
            print(userID)
            url = 'https://tw.stock.yahoo.com/q/q?s=' + stock
            list_req = requests.get(url)
            soup = BeautifulSoup(list_req.content, 'html.parser')
            getstock = soup.find('span', class_='Fz(32px)').string
            content = stock + '當前股價為：' + getstock
            if condition == '<':
                content += '\n篩選條件為：<' + price
                if float(getstock) < float(price):
                    content += '\n符合' + getstock + '<' + price + '的篩選條件'
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
            elif condition == '>':
                content += '\n篩選條件為：>' + price
                if float(getstock) > float(price):
                    content += '\n符合' + getstock + '>' + price + '的篩選條件'
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
            elif condition == '=':
                content += '\n篩選條件為：=' + price
                if float(getstock) == float(price):
                    content += '\n符合' + getstock + '=' + price + '的篩選條件'
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
    
    # if re.match('股價提醒', msg):
    #     import schedule
    #     import time
    #     def look_stock_price(stock, condition, price, userID):
    #         print(userID)
    #         url = 'https://tw.stock.yahoo.com/q/q?s=' + stock
    #         list_req = requests.get(url)
    #         soup = BeautifulSoup(list_req.content, 'html.parser')
    #         getstock = soup.find('span', class_='Fz(32px)').string
    #         content = stock + '當前股價為：' + getstock
    #         if condition == '<':
    #             content += '\n篩選條件為：<' + price
    #             if float(getstock) < float(price):
    #                 content += '\n符合' + getstock + '<' + price + '的篩選條件'
    #                 line_bot_api.push_message(userID, TextSendMessage(text=content))
    #         elif condition == '>':
    #             content += '\n篩選條件為：>' + price
    #             if float(getstock) > float(price):
    #                 content += '\n符合' + getstock + '>' + price + '的篩選條件'
    #                 line_bot_api.push_message(userID, TextSendMessage(text=content))
    #         elif condition == '=':
    #             content += '\n篩選條件為：=' + price
    #             if float(getstock) == float(price):
    #                 content += '\n符合' + getstock + '=' + price + '的篩選條件'
    #                 line_bot_api.push_message(userID, TextSendMessage(text=content))
        
        def job():
            print('HH')
            datalist = cache_users_stock()
            for i in range(len(datalist)):
                for j in range(len(datalist[i])):
                    look_stock_price(datalist[i][j]['favorite_stock'], datalist[i][j]['condition'], datalist[i][j]['price'], datalist[i][j]['userID'])

        schedule.every(15).seconds.do(job).tag('dalily-task-stock'+uid, 'second')
        while True: 
            schedule.run_pending()
            time.sleep(1)

    if msg[:3] == '@K/':   # @K/2330/2024-08-01
        if msg[3:7].replace(' ', '').isdigit():
            input_word = msg
            stock_name = input_word[3:7]
            start_date = input_word[8:]
        elif msg[3:8].replace(' ', '').isdigit():
            input_word = msg
            stock_name = input_word[3:8]
            start_date = input_word[9:]
        content = plot_stock_k_chart(IMGUR_CLIENT_ID, stock_name, start_date)
        message = ImageSendMessage(original_content_url=content, preview_image_url=content)

        line_bot_api.reply_message(event.reply_token, message)

    if re.match('先行指標', msg):
        date, volume_0000 = volume0000()
        foreign_investors, investment_trust, DEALER = II3()
        LOTS = FI_futures()
        large5, large10 = futures_large()
        pcr = PCR()
        FPC = putcall()

        content = f'日期：{date}\n'
        content += f'成交量(億元)：{volume_0000}\n外資(億元)：{foreign_investors}\n投信(億元)：{investment_trust}\n自營(億元)：{DEALER}\n'
        content += f'外資期貨留倉(口)：{LOTS}\n前五大留倉(口)：{large5}\n前十大留倉(口)：{large10}\n'
        content += f'PCR：{pcr}\n外資選擇權留倉(億元)：{FPC}'

        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))

    #################################### 匯率區 ##########################################

    if re.match('幣別代號', msg):
        message = Msg_Template.show_Button()
        line_bot_api.reply_message(event.reply_token, message)

    if re.match('匯率查詢[A-Z]{3}', msg):
        currency = msg[4:7]
        currency_name = EXRate.getCurrencyName(msg)
        if currency_name == "無可支援的外幣":
            content = "無可支援的外幣"
            line_bot_api.reply_message(event.reply_token, TextSendMessage(content))
        else:
            content = EXRate.showCurrency(currency)
            line_bot_api.reply_message(event.reply_token, TextSendMessage(content))

    # if re.match('外幣[A-Z]{3}', msg):
    #     currency = msg[2:6]
    #     currency_name = EXRate.getCurrencyName(msg)
    #     if currency_name == "無可支援的外幣":
    #         content = "無可支援的外幣"
    #         line_bot_api.push_message(uid, TextSendMessage(content))
    #     else:
    #         line_bot_api.push_message(uid, TextSendMessage('waiting..., 匯率查詢中...'))
    #         content = EXRate.showCurrency(currency)
    #     line_bot_api.push_message(uid, TextSendMessage(content))
    #     return 0

    if re.match('新增外幣[A-Z]{3}', msg):
        currency = msg[4:7]
        currency_name = EXRate.getCurrencyName(currency)
        if currency_name == "無可支援的外幣": content = "無可支援的外幣"
        elif re.match('新增外幣[A-Z]{3}[<>][0-9]', msg):
            content = mongodb.write_my_currency(uid , user_name, currency, msg[7:8], msg[8:])
        else:
            content = mongodb.write_my_currency(uid , user_name, currency, "未設定", "未設定")
        
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))

    # if re.match('新增外幣[A-Z]{3}', msg):
    #     currency = msg[4:7]
    #     currency_name = EXRate.getCurrencyName(currency)
    #     if currency_name == "無可支援的外幣": content = "無可支援的外幣"
    #     elif re.match('新增外幣[A-Z]{3}[<>][0-9]', msg):
    #         content = mongodb.write_my_currency(uid , user_name, currency, msg[7:8], msg[8:])
    #     else:
    #         content = mongodb.write_my_currency(uid , user_name, currency, "未設定", "未設定")
        
    #     line_bot_api.push_message(uid, TextSendMessage(content))
    #     return 0

    if re.match('暢遊美日韓', msg):
        btn_msg = Msg_Template.stock_reply_rate()
        line_bot_api.reply_message(event.reply_token, btn_msg)

    # if re.match('匯率大小事', msg):
    #     btn_msg = Msg_Template.stock_reply_rate()
    #     line_bot_api.push_message(uid, btn_msg)
    #     return 0
    
    if re.match('換匯[A-Z]{3}/[A-Z]{3}/[0-9]', msg):
        content = EXRate.getExchangeRate(msg)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))

    # if re.match('換匯[A-Z]{3}/[A-Z]{3}/[0-9]', msg):
    #     line_bot_api.push_message(uid, TextSendMessage('waiting..., 換匯計算中...'))
    #     content = EXRate.getExchangeRate(msg)
    #     line_bot_api.push_message(uid, TextSendMessage(content))
    #     return 0
    
    if re.match('外幣清單', msg):
        content = mongodb.show_my_currency(uid, user_name)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))

    # if re.match('外幣清單', msg):
    #     line_bot_api.push_message(uid, TextSendMessage('waiting..., 外幣查詢中...'))
    #     content = mongodb.show_my_currency(uid, user_name)
    #     line_bot_api.push_message(uid, TextSendMessage(content))
    #     return 0
    
    if re.match('刪除外幣[A-Z]{3}', msg):
        currency = mongodb.delete_my_currency(user_name, msg[4:7])
        line_bot_api.reply_message(event.reply_token, TextSendMessage(currency))

    # if re.match('刪除外幣[A-Z]{3}', msg):
    #     currency = mongodb.delete_my_currency(user_name, msg[4:7])
    #     line_bot_api.push_message(uid, TextSendMessage(currency))
    #     return 0
    
    if re.match('清空外幣', msg):
        content = mongodb.delete_my_allcurrency(user_name)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))

    # if re.match('清空外幣', msg):
    #     content = mongodb.delete_my_allcurrency(user_name)
    #     line_bot_api.push_message(uid, TextSendMessage(content))
    #     return 0

    if re.match("CT[A-Z]{3}", msg):
        currency = msg[2:5] # 外幣代號
        if EXRate.getCurrencyName(currency) == "無可支援的外幣":
            line_bot_api.push_message(uid, TextSendMessage('無可支援的外幣'))
            return 0
        line_bot_api.push_message(uid, TextSendMessage('稍等一下, 將會給您匯率走勢圖'))
        cash_imgurl = EXRate.cash_exrate_sixMonth(currency)            
        if cash_imgurl == "現金匯率無資料可分析":
            line_bot_api.push_message(uid, TextSendMessage('現金匯率無資料可分析'))
        else:
            line_bot_api.push_message(uid, ImageSendMessage(original_content_url=cash_imgurl, preview_image_url=cash_imgurl))
        
        spot_imgurl = EXRate.spot_exrate_sixMonth(currency)
        if spot_imgurl == "即期匯率無資料可分析":
            line_bot_api.push_message(uid, TextSendMessage('即期匯率無資料可分析'))
        else:
            line_bot_api.push_message(uid, ImageSendMessage(original_content_url=spot_imgurl, preview_image_url=spot_imgurl))
        btn_msg = Msg_Template.realtime_currency_other(currency)
        line_bot_api.push_message(uid, btn_msg)
        return 0


if __name__ == '__main__':
    app.run()

