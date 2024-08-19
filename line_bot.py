from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (CarouselColumn, CarouselTemplate, ImageSendMessage, MessageAction, MessageEvent, TemplateSendMessage, TextMessage,
                            TextSendMessage, StickerSendMessage, URIAction)

line_bot_api = LineBotApi('fBBQE7ZnUiwPfQ4TxnXeD8AcpfSMtcckArANHkxxZoGij3Ofp2tqQSZi0+zgeOHaxax3Zjd0zKtRoU9dp+5MhU5h/okOMpsMylgJoStsrhLEOHqhAw2lLID+KRHGg2mQFiYngozPa2NGQj5BG3qWawdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e5ea8d5cc5973437b28421a9f63aede4')