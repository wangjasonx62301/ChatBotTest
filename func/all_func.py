from func.scraper import News_set
from revChatGPT.revChatGPT import Chatbot

import re

class all_function():
    def __init__(self):
        self.config = {
            "Authorization": "<API-KEY>",
            "session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..JAOY1EqIKojrOe8t.9fTDjx61gG0e2j1rur23-n1Skuxk3gWADJrKGaqMdpNF23o7YjuslZ3_VcIVnHaDgzLxnAqaSGwtgpW3tIeSazpo5c6-KBMFqfhgCK6KWRlbKO5rFZimn2ziHIRpgyek_yNb9xrYdHj_D5urGCTmE8Vvcxx59jlmvjTOmGIEq8XfmYNp2_KTHC5Ui867wfxGk2vL7LBeAI_91Ot0PSKdjqT_x6yzoPtmZSFJc7CmX_YyL4ZkAQ4rcUGsI32eWmPFIj19eQSTPSFxPLWQi9TDNlP-SrYCB7Nomu68JY0C5wswZe-qXFDZeNmcH01I-dvut2-YURLHl36-xnAH2zczT3MnRUTAdPlOuqfxS7wl1xSQvDvJHi4L1eAlfDZ4USjRlIZfnJ9YOfrskDaGSvdK8sHwTcLrii-mc0NWv3DLIcrxX6rN8eav0WvIVHkKydJsjycpGS0_ascQlcsi1IvuEKNoHtqIetnnPBnBM6W-YXkYZQzhax0yYD0fniPXW2vDoxjdyDuIX-H9wKP8Z8rn2aGDEWMY_PpkoXEun3rf9XKB52igXXKTUkLSR_n64sRLqGmO-p5k2nbQkpN4iqaCWyaN_93C3MAOTjHDt1rZWBvHurh4qJ6JGw0FbXyC5GV2UIZPoTFDgJxIoo3LGbTs-z0M0OkVMm3fT08w1SoG9WCpIYf4xbkXSOUOBhDEBDD2QnKqeuRUfUPEz5BRfnb-7YYG4yrwlqORZE6a1NuROF1z-_HOY9D5ADW8pxTEZtwhHveFLeW2SIqYaJ-D9Bvb9U327pjrj3fTZ07jcs2OKgGU9wmI1wpTQp8VsndVfbRiJZ0exYXbd5TvEBC1vR5gi3aibnxC-Qt5Ecpjht_jFDmCVhfvtvkfT0h-3dwDhCfIzjvkVQLso6FjMEAIBPJqQ_T5JcDdq7LAVMDMdV54dXL2eDPMzFgXbLP8idnDEqF37chsxdeqDBQYkcORaomDD6-NAaf_uhApVJtJ2xvqr9zVlimeC9MPAL-MkgXTj6R1HUQzlFZ0y-q2GOk-yzG7GtXZkltLnQxDPRgZ0Qt6YxHgAItwrmrdI3rjOzSH7FJWImrZ9V2sVnhD8ljiDpQhRPc11fnzym9FwAyCHN_Xs-t0kVgEFpyRYb93xdwaf28c1oyqLQGAbvgSLZj9h5Zf87QAmjpD2sF-PiCN6mtDidlezAWcjeXA6e-5b_jgAjxoqXP2jDX1z9OjgbvmYe_DVOESnNLVruZalgg5hBOR76XbYWkJcxfmF0dGmqLvkJICdwU_ustWipIVFOC4RBNiyV1JFyeRELWNra-8xgpKIsq1QpwyR5Qh1nGpBMmVzZMf3COluiMSQyUw6H5f8MW2kgg9eH3rSKJToeo6quKSpj2FaHSyqhPMilzQpGguQFmHYZJF8dg69fTnD8vGggtBDwStabsduGJwlzs-toYu3i1PASf8r1_JBvEXTBF7-vim65duu7VwFWCYpyFLopp3BzYh55XibAGOToTKYE7BZ9VDjcyiGUiRc3BdIW_v3G8dFnh0cNe5wvP695rWWBt-sJ4uS7oxH9sq3Yezx6AE0ZwBwDsZFEu9EOdX5x3GXkGxZGAqOI_4Mit-PwJckSFNqNdAb6OjXnGVoOTZr1LL2Qvu5H3aGhLdRS_sEfTVw5iOWGCeCUjlPaEfFJp03F8sW6qmR2beuFPrwj_O00pdIT5sJKaRRvxAxQhZwgXjWqagi6wVkAxaE1YXimQn1-I4YmwK_Qu3tQ7bbYdbFuK6jyVQxHc7lqb48YF_YlfVduI0DCCljpv8D_c0MtkpR-kuI8Dfl2Q2eK1keo-ZJttQjHIrdM_Tfngc1Zydt1xXP5hA30O4Mmo_KB83c2DEpaJU3Y-Dv7WdsXfuN_XYt_qn01GDt6GxnJd090xnjvnqFzEG_AvulkA0A0jhYX6Gi_LeN9dzasFx5yB9ksXS0arGqRO6Q4xph5kD8L_FEQ_PxCncixf0ySk9JywvZ7CQKuXBdfo_Yzr3QLYPUUsJn08s1s1qt7VJp-GyitZGcJbEedeTNUi4FGBGHa4LBoncxZ1LKNuVdRCOq8HBIT4bWpKlXDC8yDkk2uLUzjmQuaI6zFFtae-N40IrEk46WkuFUNIHodZ72Xpo0cf4kQ_OJm4Ik6purnpNaBs9AAnXTCRVsWceSWxDuIxwvINuyc-ddD7LH2-a0F3_Pyv7HBVIQubrueKCAFaD3eHTumFbwrGnu-AoFYv8arTh3cobkkhooyKJvQ.a82irs0RS7v6hKAQT-yFNA"
        }
        self.BBC_news = News_set()
        self.get_news = False
        self.get_summ = False

    def exe_check(self, text):
        exe_com = text.split()

        if exe_com[0] == '!news':
            # self.get_news = True
            return self.News_scrap(text)

        if exe_com[0] == '!add' and len(exe_com) > 1:
            try:
                index = int(exe_com[1])
                return self.add_news(index)
            except Exception:
                print('Value error')
                return ""

        if exe_com[0] == '!review':
            return self.review_news()
        
        if exe_com[0] == '!del':
            if len(exe_com) == 1: return self.del_news(index=-1)
            return self.del_news(int(exe_com[1]))
        
        return "Unknown Signal"

    def News_scrap(self, text):
        exe_com = text.split()
        if(exe_com[0] == '!news' and len(exe_com) == 2):
            self.get_news = False
            self.get_summ = True
        else:
            self.get_news = True
            self.get_summ = False
        if self.get_news:
            return self.BBC_news.get_BBC_news()
        elif self.get_summ:
            target_index = int(exe_com[1])
            if 0 < target_index < 6:
                return self.BBC_news.Get_summarize(target_index - 1)
            else: return

    def add_news(self, index):
        return self.BBC_news.add_save(index)

    def review_news(self):
        return self.BBC_news.watch_save()

    def del_news(self, index):
        return self.BBC_news.del_save(index)

