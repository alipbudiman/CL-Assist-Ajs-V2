[![Version 1.0.0](https://i.ibb.co/6vJvwyf/5.png "Version 1.0.0")](https://github.com/alipbudiman/CL-Assist-Ajs-V2/blob/main/README.md#cl-assist-ajs-v2)
[![LICENSE](https://i.ibb.co/5nR4p7x/6.png "LICENSE")](https://github.com/alipbudiman/CL-Assist-Ajs-V2/blob/main/LICENSE)
[![Supported python versions: 3.x](https://i.ibb.co/L1k6BC2/7.png "supported python versions: 3.x")](https://www.python.org/downloads/)
[![Contact Author](https://i.ibb.co/xCDRtJs/8.png "contact author")](https://fxgdev.site/alifbudiman.html)


# ![logo](https://i.ibb.co/zJvVhJ3/Untitled-design-88.png)


# CL-Assist-Ajs-V2
## Version 1.3.0

**Unoffcial LINE bot**. Using LINE private API for automate some task in LINE chat.

**Please Note**, this is using Unoffcial library, wich is **ILLEGAL**. so use wisely

This script under [**MIT LICENSE**](https://github.com/alipbudiman/CL-Assist-Ajs-V2/blob/main/LICENSE).

**NOT FOR SALE!!**


# Features
- Banning
  - Auto Purge Blacklist
  - Add Blacklist
  - Auot Blacklist
  - Delete And Add Blacklist
  - View Blacklist
  - Other

- Backup
  - Add Whitelist (Add Bot)
  - Delete Whitelist
  - Backup Whitelist
  - View Whitelist
  - Backup Owner & Creator

- Kick
  - Kick (Python kick)
  - Kill (Js kick)
  - Kickall
  - Join & Kickall
 
- Protect
  - Protect Kick
  - Protect Cancel
  - Protect Invite
  - Protect Join
  - Protect QR Group
  - View List Protect

- Profile
  - Update Pict
  - Update Cover
  - Update Name
  - Update Bio
  - Add Key
  - Remove Key
  - View Group List

- Ajs
  - Run Ajs from Assist
  - Ajs Stay / Denay
  - Ajs In
  - Ajs Backup

- Basic
  - Debug Speed
  - Restart Bot
  - Out / Out All from Group

- Login
  - Random Header

And Others (WIP).

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

Owner will get more access than Creator(**TBA*)

** NEED API FOR CONVERT PRIMARY TOKEN TO SECONDARY **

https://github.com/alipbudiman/CL-Assist-Ajs-V2/blob/1f387092248e29d137c35bfae8e5f9921a0b47fe/main.py#L23-L25

for converting token, you need put your api-key.

You can get api key from https://api.chstore.me

FREE 200 api-request for new user


## 3. Run your script
This script running using python3
```SH
python3 main.py
```
Note: Kill, Nuke, Nuke Join fiture using JS-Node. So you need install JS-node to.


# Casing

You can contact me if have a question or want to help this repo :)

You can visit my website to, [www.fxgdev.site](https://fxgdev.site/)

Please don't sell this script and APPRECIATE me


# Credit

## Special Thanks:
Basic library from: [herywinarto/SIMPLE-PROTECTV2](https://github.com/herywinarto/SIMPLE-PROTECTV2)

Convert Primary token from: [hert0t/API-DOC](https://github.com/hert0t/API-DOC)

Super Split Logic from: [ii64/Archimed](https://github.com/ii64/Archimed)

Testing & Help by: [Whynotfarell](https://github.com/Whynotfarell)

## Author:
[Alip/Alif Budiman](https://fxgdev.site/alifbudiman.html)

# Donation:
https://saweria.co/alipbudiman
