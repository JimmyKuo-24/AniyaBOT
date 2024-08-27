from linebot.models import *

city_list = ["基隆市","台北市","新北市",
             "桃園市","新竹市","新竹縣",
             "苗栗縣","台中市","彰化縣",
             "南投縣","雲林縣","嘉義市",
             "嘉義縣","台南市","高雄市",
             "屏東縣","宜蘭縣","花蓮縣",
             "台東縣","澎湖縣","金門縣",
             "連江縣"]

city_dict = {
    "基隆市": '10017',"台北市": '63',"新北市": '65',
    "桃園市": '68',"新竹市": '10018',"新竹縣": '10004',
    "苗栗縣": '10005',"台中市": '66',"彰化縣": '10007',
    "南投縣": '10008',"雲林縣": '10009',"嘉義市": '10020',
    "嘉義縣": '10010',"台南市": '67',"高雄市": '64',
    "屏東縣": '10013',"宜蘭縣": '10002',"花蓮縣": '10015',
    "台東縣": '10014',"澎湖縣": '10016',"金門縣": '09020',
    "連江縣": '09007',
}

####################縣市選單(即時、預報)####################
# 全台縣市選單(22個)-即時天氣+預報天氣
def select_city(mat):
    if mat=='即時天氣':
        message_1='請問要查詢'
        message_2='的那個地區'
    elif mat=='天氣預報':
        message_1='我要查詢'
        message_2='的預報天氣'
    flex_message = FlexSendMessage(
        alt_text="請選擇想查詢的縣市：",
        contents={
            "type": "bubble",
            "size": "mega",
            "hero": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "全台縣市選單",
                    "color": "#4493A3",
                    "margin": "md",
                    "size": "xl",
                    "weight": "bold",
                    "wrap": True,
                    "adjustMode": "shrink-to-fit",
                    "offsetStart": "25px"
                }
                ],
                "paddingAll": "0px"
            },
            "body": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[0],
                        "text": message_1+city_list[0]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[3],
                        "text": message_1+city_list[3]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[6],
                        "text": message_1+city_list[6]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[9],
                        "text": message_1+city_list[9]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[12],
                        "text": message_1+city_list[12]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[15],
                        "text": message_1+city_list[15]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[18],
                        "text": message_1+city_list[18]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[21],
                        "text": message_1+city_list[21]+message_2
                        }
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "md",
                    "contents": [
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[1],
                        "text": message_1+city_list[1]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[4],
                        "text": message_1+city_list[4]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[7],
                        "text": message_1+city_list[7]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[10],
                        "text": message_1+city_list[10]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[13],
                        "text": message_1+city_list[13]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[16],
                        "text": message_1+city_list[16]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[19],
                        "text": message_1+city_list[19]+message_2
                        }
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "md",
                    "contents": [
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[2],
                        "text": message_1+city_list[2]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[5],
                        "text": message_1+city_list[5]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[8],
                        "text": message_1+city_list[8]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[11],
                        "text": message_1+city_list[11]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[14],
                        "text": message_1+city_list[14]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[17],
                        "text": message_1+city_list[17]+message_2
                        }
                    },
                    {
                        "type": "button",
                        "adjustMode": "shrink-to-fit",
                        "color": "#7EB5A6",
                        "style": "primary",
                        "margin": "sm",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": city_list[20],
                        "text": message_1+city_list[20]+message_2
                        }
                    }
                    ]
                }
                ],
                "paddingAll": "8px"
            }
        }
    )
    return flex_message

#######################最新氣象-圖片轉盤#######################
# 第一層-圖文選單->最新氣象->4格圖片
def img_Carousel():
    flex_message = FlexSendMessage(
        alt_text="請選擇查詢事項：",
        contents={
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://i.imgur.com/RUko8kX.png",
                            "flex": 1,
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://liff.line.me/2006134064-081mZO1b"
                            },
                            "gravity": "center",
                            "aspectMode": "cover",
                            "size": "full"
                        },
                        {
                            "type": "image",
                            "url": "https://i.imgur.com/v3Utnrb.png",
                            "aspectMode": "cover",
                            "gravity": "center",
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://liff.line.me/2006134064-QK1BXK1V"
                            },
                            "size": "full"
                        }
                        ],
                        "paddingAll": "0px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://i.imgur.com/XJoUB8J.png",
                            "aspectMode": "cover",
                            "gravity": "center",
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://liff.line.me/2006134064-QK1BXK1V"
                            },
                            "size": "full"
                        },
                        {
                            "type": "image",
                            "url": "https://i.imgur.com/P1I05xm.png",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "150:150",
                            "gravity": "center",
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://liff.line.me/2006134064-vBqgJRqm"
                            }
                        }
                        ],
                        "flex": 1,
                        "paddingAll": "0px"
                    }
                    ],
                    "paddingAll": "0px"
                }
                ],
                "paddingAll": "0px"
            }
        }
    )
    return flex_message

#######################QuickReply()#######################
# 第二層-quick_reply(即時天氣+預測天氣)

def quick_reply_earth():
    content_twxt = '請選擇您要的資訊：'
    text_message = TextSendMessage(text=content_twxt, 
                                   quick_reply=QuickReply(
                                        items=[
                                            QuickReplyButton(action=URIAction(label='💧💧水庫水情', uri='https://liff.line.me/2006134064-5m4wzp4V')),
                                            QuickReplyButton(action=URIAction(label='🌋🌋地震測報', uri='https://liff.line.me/2006134064-5AXkvjX7')),
                                            QuickReplyButton(action=LocationAction(label='🏠🏠查詢地址'))
                                        ]
                                   ))
    return text_message

# def quick_reply_weather(mat):
#     content_twxt = '請選擇您要查詢的天氣：'
#     text_message = TextSendMessage(text=content_twxt, 
#                                    quick_reply=QuickReply(
#                                         items=[
#                                             QuickReplyButton(action=MessageAction(label='查詢其他天氣', text='其他'+mat)),
#                                             QuickReplyButton(action=LocationAction(label='查詢地址'))
#                                         ]
#                                    ))
#     return text_message
