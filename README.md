# CL-Assist-V2

**Unoffcial LINE bot**. Using LINE private API for automate some task in LINE chat.

**Please Note**, this is using Unoffcial library, wich is **ILLEGAL**. so use use wisely


# How to run bot?

## 1. Add Primary Token into JSON
First input your token into file > statusalip.json
```JSON
{
  "assistToken":"*Your Token"
}
```
**Your Token is your LINE Primary token, you can get it from Sniffing your LINE account or generate from your Auth Key*

You can get Primary token form Sniffing or generate it by using Authkey or Generete token Bot.
If you want run AJS (Anti-js) or Pending bots for backup your Assist. You need to input Other token (Diffrent Another Token) into Value of key "ajsToken"
```JSON
{
  "ajsToken":"*Your Other Token"
}
```
**Your Other Token is your LINE Primary token and Diffrent Token from LINE Primary token input into assistToken (Diffrent Account)*

Please note, **you must input Token into value of assistToken** for run this bot. but you are **free to input Token into value of ajsToken**.

if You if you don't put the token in the value of ajsToken, then your bot will run as Single Assist.

## 2. Add Mid Token into JSON

For reconize operatior of this bot, you need input mid into file > statusalip.json

mid same as id, but for server. You can get your mid with Sniffing, Using other bot or if you need help you can contact me on [LINE](https://line.me/ti/p/~alip_budiman)

You can find Owner and Creator empty list in file > statusalip.json

You can imput your mid and other mid into list
```JSON
{
  "Owner":[
    "*Your mid",
    "*Other mid"
  ],
  "Creator":[
    "*Other mid"
  ]
}
```
**the maximum number of mids entered is not limited*

Bot will not be able to run if you leave Creator and Owner empty.

Owner will get more access than Creator* (**TBA*)

## 3. Run your script
This script running using python3
```SH
python3 main.py
```
