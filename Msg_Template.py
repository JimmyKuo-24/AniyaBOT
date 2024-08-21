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
                                                    text="外幣"+currency,
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
                                                    label="走勢圖", 
                                                    text="CT"+currency,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="新聞", 
                                                    text="N外匯"+currency,
                                                )
                                       )
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

def stock_reply_other():
    content_text = "分析趨勢圖"
    text_message = TextSendMessage(
        text = content_text ,
        quick_reply=QuickReply(
            items=[
                    QuickReplyButton(
                            action=MessageAction(
                                label="💜股價查詢💜", 
                                text="輸入：#xxxx",
                            )
                    ),
                    QuickReplyButton(
                            action=MessageAction(
                                label="💜匯率趨勢💜", 
                                text="輸入：CTUSD",
                            )
                    ),
                    QuickReplyButton(
                            action=MessageAction(
                                label="💜股價K線圖💜",  
                                text="輸入：@K23302024-08-01",
                            )
                    )
            ]
        )
    )
    return text_message

def stock_reply_rate():
    content_text = "想知道匯率？"
    text_message = TextSendMessage(
        text = content_text ,
        quick_reply=QuickReply(
            items=[
                    QuickReplyButton(
                            action=MessageAction(
                                label="💜💜查詢單一幣別匯率", 
                                text="幣別種類",
                            )
                    ),
                    QuickReplyButton(
                            action=MessageAction(
                                label="💜💜查詢幣別匯率", 
                                text="匯率兌換",
                            )
                    ),
                    QuickReplyButton(
                            action=MessageAction(
                                label="💜💜關注的匯率", 
                                text="外幣清單",
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

