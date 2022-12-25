# News app

一個使用爬蟲和NLP模組構成的機器人，NLP使用Google-pretrained(**Pegasus**)

## Set-up


```bash
pip install uvicorn
pip install ngrok
pip install transformers
```
// only in local
```
uvicorn main:app --reload
ngrok http 8000
```

## FSM

![FSM](https://i.imgur.com/FlWk4Rn.png)

**1. !news x** :  未宣告x會呈列出今日BBC頭條新聞，使用x則會出現該編號新聞的摘要

**2. !add x** :   務必宣告x，加入備忘錄

**3. !del x** :   未宣告x會將備忘錄的新聞全數刪除，使用x則會刪除特定編號的備忘錄

**4. !review** :  顯示當前備忘錄，備忘錄會在00:00重置
