from linebot.models import *

def follow_msg():
    flex_message = FlexSendMessage(
            alt_text="歡迎訊息",
            contents={
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
    )
    return flex_message

def realtime_currency_other(currency):
    content = "想知道更多？"
    text_message = TextSendMessage(
                                text = content ,
                               quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="即時匯率", 
                                                    text="匯率查詢"+currency,
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="加入清單", 
                                                    text="新增外幣"+currency,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="趨勢圖", 
                                                    text="CT"+currency,
                                                )
                                       ),
                                ]
                            ))
    return text_message

def show_Button():
    flex_message = FlexSendMessage(
            alt_text="幣別種類",
            contents={
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://i.imgur.com/Fyldio8.jpg",
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
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "澳幣",
                    "text": "AUD"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "加拿大幣",
                    "text": "CAD"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "瑞士法郎",
                    "text": "CHF"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                }
                ],
                "spacing": "sm"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "人民幣",
                    "text": "CNY"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "歐元",
                    "text": "EUR"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "英鎊",
                    "text": "GBP"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                }
                ],
                "spacing": "sm"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "港幣",
                    "text": "HKD"
                    },
                    "color": "#F6FB7A",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "印尼盾",
                    "text": "IDR"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "日元",
                    "text": "JPY"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                }
                ],
                "spacing": "sm"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "韓元",
                    "text": "KRW"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "馬來幣",
                    "text": "MYR"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "紐元",
                    "text": "NZD"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                }
                ],
                "spacing": "sm"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "菲律賓幣",
                    "text": "PHP"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "瑞典克朗",
                    "text": "SEK"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "新加坡幣",
                    "text": "SGD"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                }
                ],
                "spacing": "sm"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "泰銖",
                    "text": "THB"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "美元",
                    "text": "USD"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "越南盾",
                    "text": "VND"
                    },
                    "style": "secondary",
                    "color": "#F6FB7A"
                }
                ],
                "spacing": "sm"
            }
            ],
            "spacing": "sm"
        },
        "styles": {
            "body": {
            "backgroundColor": "#73BBA3"
            }
        }
        }
    )
    return flex_message

# def stock_reply_other():
#     content_text = "分析趨勢"
#     text_message = TextSendMessage(
#         text = content_text ,
#         quick_reply=QuickReply(
#             items=[
#                     QuickReplyButton(
#                             action=MessageAction(
#                                 label="💜股價查詢💜", 
#                                 text="輸入：#股票代號",
#                             )
#                     ),
#                     QuickReplyButton(
#                             action=MessageAction(
#                                 label="💜匯率趨勢💜", 
#                                 text="輸入：CT幣別",
#                             )
#                     ),
#                     QuickReplyButton(
#                             action=MessageAction(
#                                 label="💜股價K線圖💜",  
#                                 text="輸入：@K/2330/2024-08-01",
#                             )
#                     )
#             ]
#         )
#     )
#     return text_message

def stock_reply_rate():
    content_text = "想知道匯率？"
    text_message = TextSendMessage(
        text = content_text ,
        quick_reply=QuickReply(
            items=[
                    QuickReplyButton(
                            action=MessageAction(
                                label="💜💜查詢美元匯率", 
                                text="匯率查詢USD",
                            )
                    ),
                    QuickReplyButton(
                            action=MessageAction(
                                label="💜💜查詢日元匯率", 
                                text="匯率查詢JPY",
                            )
                    ),
                    QuickReplyButton(
                            action=MessageAction(
                                label="💜💜查詢韓元匯率", 
                                text="匯率查詢KRW",
                            )
                    )
            ]
        )
    )
    return text_message

def usage_msg():
    flex_message = FlexSendMessage(
            alt_text="使用說明",
            contents={
        "type": "carousel",
        "contents": [
            {
            "type": "bubble",
            "size": "micro",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/k2FqRn3.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "320:213"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "股票指令",
                    "weight": "bold",
                    "size": "lg",
                    "align": "center"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "股價查詢",
                    "text": "#股票代號 (#2330、#00878)"
                    },
                    "color": "#EECAD5",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "關注股票",
                    "text": "關注XXXX>$$$$ (關注+2330+<=>+1000)"
                    },
                    "color": "#EECAD5",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "股票清單",
                    "text": "股票清單"
                    },
                    "color": "#EECAD5",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "刪除股票",
                    "text": "刪除股票代號 (2330、00878)"
                    },
                    "color": "#EECAD5",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "清空股票",
                    "text": "清空股票"
                    },
                    "color": "#EECAD5",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "股價提醒",
                    "text": "股價提醒"
                    },
                    "color": "#EECAD5",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "關閉提醒",
                    "text": "關閉提醒"
                    },
                    "color": "#EECAD5",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "股票K線圖",
                    "text": "@K/股票代號/年-月-日 (2330、2024-08-01)"
                    },
                    "color": "#EECAD5",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "財經學堂",
                    "text": "財經學堂"
                    },
                    "color": "#EECAD5",
                    "style": "secondary"
                }
                ],
                "spacing": "md",
                "paddingAll": "13px"
            },
            "styles": {
                "body": {
                "backgroundColor": "#F6EACB"
                }
            }
            },
            {
            "type": "bubble",
            "size": "micro",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/LhsGNgU.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "320:213"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "匯率指令",
                    "weight": "bold",
                    "size": "lg",
                    "align": "center"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "幣別代號",
                    "text": "幣別代號"
                    },
                    "color": "#FFDA76",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "匯率查詢",
                    "text": "匯率查詢幣別代號 (匯率查詢+USD)"
                    },
                    "color": "#FFDA76",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "新增外幣",
                    "text": "新增外幣幣別代號 (新增外幣+USD)"
                    },
                    "color": "#FFDA76",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "暢遊美日韓",
                    "text": "暢遊美日韓"
                    },
                    "color": "#FFDA76",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "換匯試算",
                    "text": "換匯幣別(1)/幣別(2)/金額 (TWD/USD/10000)"
                    },
                    "color": "#FFDA76",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "外幣清單",
                    "text": "外幣清單"
                    },
                    "color": "#FFDA76",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "刪除外幣",
                    "text": "刪除外幣幣別 (刪除外幣+USD)"
                    },
                    "color": "#FFDA76",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "清空外幣",
                    "text": "清空外幣"
                    },
                    "color": "#FFDA76",
                    "style": "secondary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "匯率曲線圖",
                    "text": "CT幣別 (CT+USD)"
                    },
                    "color": "#FFDA76",
                    "style": "secondary"
                }
                ],
                "spacing": "md",
                "paddingAll": "13px"
            },
            "styles": {
                "body": {
                "backgroundColor": "#B4D6CD"
                }
            }
            }
        ]
        }
    )
    return flex_message

def yt_channel():
    flex_message = FlexSendMessage(
            alt_text="youtube_channel",
            contents={
        "type": "carousel",
        "contents": [
            {
            "type": "bubble",
            "size": "micro",
            "hero": {
                "type": "image",
                "url": "https://imgur.com/SJPH542.jpg",
                "aspectMode": "fit",
                "aspectRatio": "320:213",
                "size": "full",
                "backgroundColor": "#000000"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "小Lin说",
                    "weight": "bold",
                    "size": "lg",
                    "wrap": True,
                    "align": "center"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "icon",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "text",
                        "text": "乐乐呵呵涨知识",
                        "size": "xs",
                        "color": "#8c8c8c",
                        "margin": "md",
                        "flex": 0,
                        "weight": "bold"
                    }
                    ]
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "uri",
                    "label": "點我觀看",
                    "uri": "https://www.youtube.com/@xiao_lin_shuo/featured"
                    }
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "理財youtuber",
                            "wrap": True,
                            "color": "#8c8c8c",
                            "size": "xxs",
                            "flex": 5
                        }
                        ]
                    }
                    ]
                }
                ],
                "spacing": "sm",
                "paddingAll": "13px"
            }
            },
            {
            "type": "bubble",
            "size": "micro",
            "hero": {
                "type": "image",
                "url": "https://imgur.com/dPW0jcC.jpg",
                "size": "full",
                "aspectMode": "fit",
                "aspectRatio": "320:213",
                "backgroundColor": "#AA0000"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "C&K GO!",
                    "weight": "bold",
                    "size": "lg",
                    "wrap": True,
                    "align": "center"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "icon",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "text",
                        "text": "投資沒有那麼難~",
                        "size": "xs",
                        "color": "#8c8c8c",
                        "margin": "md",
                        "flex": 0,
                        "weight": "bold"
                    }
                    ]
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "uri",
                    "label": "點我觀看",
                    "uri": "https://www.youtube.com/@CKGOChannelShow/featured"
                    }
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "理財youtuber",
                            "wrap": True,
                            "color": "#8c8c8c",
                            "size": "xxs",
                            "flex": 5
                        }
                        ]
                    }
                    ]
                }
                ],
                "spacing": "sm",
                "paddingAll": "13px"
            }
            },
            {
            "type": "bubble",
            "size": "micro",
            "hero": {
                "type": "image",
                "url": "https://imgur.com/zkUZrCj.jpg",
                "size": "full",
                "aspectMode": "fit",
                "aspectRatio": "320:213",
                "backgroundColor": "#444444"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "老貓與指標",
                    "weight": "bold",
                    "size": "lg",
                    "wrap": True,
                    "align": "center"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "icon",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "text",
                        "text": "各種交易指標和策略",
                        "size": "xs",
                        "color": "#8c8c8c",
                        "margin": "md",
                        "flex": 0,
                        "weight": "bold"
                    }
                    ]
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "uri",
                    "label": "點我觀看",
                    "uri": "https://www.youtube.com/@oldgrumpycat/featured"
                    }
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "理財youtuber",
                            "wrap": True,
                            "color": "#8c8c8c",
                            "size": "xxs",
                            "flex": 5
                        }
                        ]
                    }
                    ]
                }
                ],
                "spacing": "sm",
                "paddingAll": "13px"
            }
            }
        ]
        }
    )
    return flex_message

