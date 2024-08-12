from linebot.models import *

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

def yt_channel():
    flex_message = FlexSendMessage(
            alt_text="youtube_channel",
            contents=
            {
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
                                "url": "https://www.youtube.com/@xiao_lin_shuo/featured"
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
