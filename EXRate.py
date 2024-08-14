import imgur, json, twder, matplotlib, requests, ssl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.font_manager import FontProperties
chinese_font = matplotlib.font_manager.FontProperties(fname='msjh.ttf')

ssl._create_default_https_context = ssl._create_unverified_context

def getCurrencyName(currency):
    currency_list = {
        'AUD': '澳幣',  
        'CAD': '加拿大幣',
        'CHF': '瑞士法郎',
        'CNY': '人民幣',
        'EUR': '歐元',
        'GBP': '英鎊',
        'HKD': '港幣',
        'IDR': '印尼盾',
        'JPY': '日元',
        'KRW': '韓元',
        'MYR': '馬來幣',
        'NZD': '紐元',
        'PHP': '菲律賓幣',
        'SEK': '瑞典克朗',
        'SGD': '新加坡幣',
        'THB': '泰銖',
        'USD': '美元',
        'VND': '越南盾',
    }
    try:
        currency_name = currency_list[currency]
    except:
        return "Not Found"
    return currency_name

def getExchangeRate(msg):
    """
    sample
    code = '換匯 USD/TWD/100'
    code = '換匯 USD/JPY/100'
    """
    currency_list = msg[2:].split('/')
    currency = currency_list[0]
    currency1 = currency_list[1]
    money_value = currency_list[2]
    url_coinbase = 'https://api.coinbase.com/v2/exchange-rates?currency=' + currency
    res = requests.get(url_coinbase)
    jData = res.json()
    pd_currency = jData['data']['rates']
    content = f"目前兌換匯率：{pd_currency[currency1]} {currency1} \n查詢金額為："
    amount = float(pd_currency[currency1])
    content += str('%.2f'%(amount*float(money_value))) + " " + currency1
    return content

def showCurrency(code):
    content = ""
    currency_name = getCurrencyName(code)
    if currency_name == "無可支援的外幣": return "無可支援的外幣"
    # 資料格式 {貨幣代碼: (時間, 現金買入, 現金賣出, 即期買入, 即期賣出), ...}
    currency = twder.now(code) 
    # 當下時間
    now_time = str(currency[0])
    # 銀行現金買入價格
    buying_cash = "無資料" if currency[1] == '-' else str(float(currency[1])) 
    # 銀行現金賣出價格
    sold_cash = "無資料" if currency[2] == '-' else str(float(currency[2])) 
    # 銀行即期買入價格
    buying_spot = "無資料" if currency[3] == '-' else str(float(currency[3])) 
    # 銀行即期賣出價格
    sold_spot = "無資料" if currency[4] == '-' else str(float(currency[4])) 
    content +=  f"{currency_name} 最新掛牌時間為: {now_time}\n ---------- \n 現金買入價格: {buying_cash}\n 現金賣出價格: {sold_cash}\n 即期買入價格: {buying_spot}\n 即期賣出價格: {sold_spot}\n \n"
    return content

def cash_exrate_sixMonth(code1):
    currency_name = getCurrencyName(code1)
    if currency_name == "無可支援的外幣": return "無可支援的外幣"
    dfs = pd.read_html(f'https://rate.bot.com.tw/xrt/quote/l6m/{code1}')
    currency = dfs[0].iloc[:, 0:6]
    currency.columns = [u'Date', u'Currency', u'現金買入', u'現金賣出', u'即期買入', u'即期賣出']
    currency[u'Currency'] = currency[u'Currency'].str.extract('\((\w+)\)')
    currency = currency.iloc[::-1]   # 倒序排列
    if currency['現金買入'][0] == '-' or currency['現金買入'][0] == 0.0:
        return "現金匯率無資料可分析"
    currency.plot(kind='line', x='Date', y=[u'現金買入', u'現金賣出'], figsize=(12, 6))
    plt.legend(prop=chinese_font)
    plt.title(f"{currency_name} 6 個月現金匯率趨勢圖", fontsize=20, fontproperties=chinese_font)
    plt.savefig(f'{code1}_cash_exrate_sixMonth.png')
    plt.show()
    plt.close()
    return imgur.showImgur(code1)

def spot_exrate_sixMonth(code2):
    currency_name = getCurrencyName(code2)
    if currency_name == "無可支援的外幣": return "無可支援的外幣"
    dfs = pd.read_html(f'https://rate.bot.com.tw/xrt/quote/l6m/{code2}')
    currency = dfs[0].iloc[:, 0:6]
    currency.columns = [u'Date', u'Currency', u'現金買入', u'現金賣出', u'即期買入', u'即期賣出']
    currency[u'Currency'] = currency[u'Currency'].str.extract('\((\w+)\)')
    currency = currency.iloc[::-1]   # 倒序排列
    if currency['即期買入'][0] == '-' or currency['即期買入'][0] == 0.0:
        return "即期匯率無資料可分析"
    currency.plot(kind='line', x='Date', y=[u'即期買入', u'即期賣出'], figsize=(12, 6))
    plt.legend(prop=chinese_font)
    plt.title(f"{currency_name} 6 個月即期匯率趨勢圖", fontsize=20, fontproperties=chinese_font)
    plt.savefig(f'{code2}_spot_exrate_sixMonth.png')
    plt.show()
    plt.close()
    return imgur.showImgur(code2)