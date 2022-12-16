import os
import re
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from fastapi.params import Header
from starlette.requests import Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from func.all_func import all_function
from func.Preprocessing_eng_custom import Custom_preprocessing
from func.Txt_summarize_helper import Summarize
from func.scraper import News_set
# from func import *
# from func.summarize import Summarize
import json
import nest_asyncio
from revChatGPT.revChatGPT import Chatbot

app = FastAPI()

load_dotenv()

config = {
    "Authorization": "<API-KEY>",
    "session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..JAOY1EqIKojrOe8t.9fTDjx61gG0e2j1rur23-n1Skuxk3gWADJrKGaqMdpNF23o7YjuslZ3_VcIVnHaDgzLxnAqaSGwtgpW3tIeSazpo5c6-KBMFqfhgCK6KWRlbKO5rFZimn2ziHIRpgyek_yNb9xrYdHj_D5urGCTmE8Vvcxx59jlmvjTOmGIEq8XfmYNp2_KTHC5Ui867wfxGk2vL7LBeAI_91Ot0PSKdjqT_x6yzoPtmZSFJc7CmX_YyL4ZkAQ4rcUGsI32eWmPFIj19eQSTPSFxPLWQi9TDNlP-SrYCB7Nomu68JY0C5wswZe-qXFDZeNmcH01I-dvut2-YURLHl36-xnAH2zczT3MnRUTAdPlOuqfxS7wl1xSQvDvJHi4L1eAlfDZ4USjRlIZfnJ9YOfrskDaGSvdK8sHwTcLrii-mc0NWv3DLIcrxX6rN8eav0WvIVHkKydJsjycpGS0_ascQlcsi1IvuEKNoHtqIetnnPBnBM6W-YXkYZQzhax0yYD0fniPXW2vDoxjdyDuIX-H9wKP8Z8rn2aGDEWMY_PpkoXEun3rf9XKB52igXXKTUkLSR_n64sRLqGmO-p5k2nbQkpN4iqaCWyaN_93C3MAOTjHDt1rZWBvHurh4qJ6JGw0FbXyC5GV2UIZPoTFDgJxIoo3LGbTs-z0M0OkVMm3fT08w1SoG9WCpIYf4xbkXSOUOBhDEBDD2QnKqeuRUfUPEz5BRfnb-7YYG4yrwlqORZE6a1NuROF1z-_HOY9D5ADW8pxTEZtwhHveFLeW2SIqYaJ-D9Bvb9U327pjrj3fTZ07jcs2OKgGU9wmI1wpTQp8VsndVfbRiJZ0exYXbd5TvEBC1vR5gi3aibnxC-Qt5Ecpjht_jFDmCVhfvtvkfT0h-3dwDhCfIzjvkVQLso6FjMEAIBPJqQ_T5JcDdq7LAVMDMdV54dXL2eDPMzFgXbLP8idnDEqF37chsxdeqDBQYkcORaomDD6-NAaf_uhApVJtJ2xvqr9zVlimeC9MPAL-MkgXTj6R1HUQzlFZ0y-q2GOk-yzG7GtXZkltLnQxDPRgZ0Qt6YxHgAItwrmrdI3rjOzSH7FJWImrZ9V2sVnhD8ljiDpQhRPc11fnzym9FwAyCHN_Xs-t0kVgEFpyRYb93xdwaf28c1oyqLQGAbvgSLZj9h5Zf87QAmjpD2sF-PiCN6mtDidlezAWcjeXA6e-5b_jgAjxoqXP2jDX1z9OjgbvmYe_DVOESnNLVruZalgg5hBOR76XbYWkJcxfmF0dGmqLvkJICdwU_ustWipIVFOC4RBNiyV1JFyeRELWNra-8xgpKIsq1QpwyR5Qh1nGpBMmVzZMf3COluiMSQyUw6H5f8MW2kgg9eH3rSKJToeo6quKSpj2FaHSyqhPMilzQpGguQFmHYZJF8dg69fTnD8vGggtBDwStabsduGJwlzs-toYu3i1PASf8r1_JBvEXTBF7-vim65duu7VwFWCYpyFLopp3BzYh55XibAGOToTKYE7BZ9VDjcyiGUiRc3BdIW_v3G8dFnh0cNe5wvP695rWWBt-sJ4uS7oxH9sq3Yezx6AE0ZwBwDsZFEu9EOdX5x3GXkGxZGAqOI_4Mit-PwJckSFNqNdAb6OjXnGVoOTZr1LL2Qvu5H3aGhLdRS_sEfTVw5iOWGCeCUjlPaEfFJp03F8sW6qmR2beuFPrwj_O00pdIT5sJKaRRvxAxQhZwgXjWqagi6wVkAxaE1YXimQn1-I4YmwK_Qu3tQ7bbYdbFuK6jyVQxHc7lqb48YF_YlfVduI0DCCljpv8D_c0MtkpR-kuI8Dfl2Q2eK1keo-ZJttQjHIrdM_Tfngc1Zydt1xXP5hA30O4Mmo_KB83c2DEpaJU3Y-Dv7WdsXfuN_XYt_qn01GDt6GxnJd090xnjvnqFzEG_AvulkA0A0jhYX6Gi_LeN9dzasFx5yB9ksXS0arGqRO6Q4xph5kD8L_FEQ_PxCncixf0ySk9JywvZ7CQKuXBdfo_Yzr3QLYPUUsJn08s1s1qt7VJp-GyitZGcJbEedeTNUi4FGBGHa4LBoncxZ1LKNuVdRCOq8HBIT4bWpKlXDC8yDkk2uLUzjmQuaI6zFFtae-N40IrEk46WkuFUNIHodZ72Xpo0cf4kQ_OJm4Ik6purnpNaBs9AAnXTCRVsWceSWxDuIxwvINuyc-ddD7LH2-a0F3_Pyv7HBVIQubrueKCAFaD3eHTumFbwrGnu-AoFYv8arTh3cobkkhooyKJvQ.a82irs0RS7v6hKAQT-yFNA" 
}

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

Scraper = News_set()
All_check = all_function()




@app.post("/api/line")
async def callback(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(
            status_code=400, detail="Invalid signature. Please check your channel access token/channel secret.")
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    print("Handle: reply_token: " + event.reply_token + ", message: " + event.message.text)
    content = "{}".format(event.message.text)
    c = All_check.exe_check(content)
    # chatbot = Chatbot(config = config, conversation_id=None)
    # chatbot.reset_chat()
    # chatbot.refresh_session()
    # resp = chatbot.get_chat_response(content)
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=c))
    # else:
    #     line_bot_api.reply_message(event.reply_token,TextSendMessage(text=resp['message']))
