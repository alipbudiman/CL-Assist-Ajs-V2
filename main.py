"""

CL PYTHON V2 /+ AJS

# LINE bot Library from https://github.com/herywinarto/SIMPLE-PROTECTV2
# Create by Alip Budiman
# Copyright 2021 by www.fxgdev.site
# find me on
    -> Instagram: alifbudimanwahabbi
    -> LineID: alip_budiman
    -> github: https://github.com/alipbudiman

Visit our website:
    -> www.fxgdev.com

"""


from function import *

statusalip = livejson.File("statusalip.json", True, True, 4)

hostt = "https://api.coursehero.store"
VersionBot = "1.0.0"

if statusalip["assistToken"] == "":
    sys.exit(
        "Token Assist tidak boleh kosong!! silahkan masukan di dalam database 'statusalip.json'"
    )


def ConvPrim(token, header):
    params = {"appname": header, "authtoken": token}
    resp = requests.get(hostt + "/lineprimary2secondary", params=params).json()
    if resp["status"] != 200:
        raise Exception(resp["reason"])
    return resp["result"]["token"]


header = statusalip["headers"]
if statusalip["assistSecondary"] == "":
    token1 = ConvPrim(statusalip["assistToken"], header)
    statusalip["assistSecondary"] = token1

alip = LINEBOT(myToken=str(statusalip["assistSecondary"]), myApp=header)

alipMID = alip.profile.mid
if alipMID:
    print("Success login Assist")

time.sleep(2)

ajsMID = None
ajs = alip

if statusalip["ajsToken"] != "":
    if statusalip["ajsSecondary"] == "":
        token2 = ConvPrim(statusalip["ajsToken"], header)
        statusalip["ajsSecondary"] = token2
    ajs = LINEBOT(myToken=str(statusalip["ajsSecondary"]), myApp=header, isAjs=True)
    ajsMID = ajs.profile.mid
    if ajsMID:
        print("Success login AJS")


def AlipKedua():
    print("Auto add Syncro")
    ts = random.uniform(10, 20)
    ts2 = random.uniform(10, 20)
    if ajsMID not in alip.getAllContactIds():
        print("find and add ajs contact, wait 10 second")
        time.sleep(ts)
        alip.findAndAddContactsByMid(ajsMID)
        if ajsMID in alip.getAllContactIds():
            print("Success add ajs contact")
        else:
            print("Failed add ajs contact")
    else:
        print("Ajs Alredy in Assist friend list")

    if alipMID not in ajs.getAllContactIds():
        print("find and add assist contact, wait 10 second")
        time.sleep(ts2)
        ajs.findAndAddContactsByMid(alipMID)
        if alipMID in ajs.getAllContactIds():
            print("Success add assist contact")
        else:
            print("Failed add assist contact")
    else:
        print("Assist Alredy in Ajs friend list")


def SyncAllFriends():
    print("Syncronize All Friends")
    SyncFriends = alip.FindDuplicatedAndRemove(creator, owner, Bots)
    for x in SyncFriends:
        if x not in alip.getAllContactIds():
            alip.findAndAddContactsByMid(x)
            print("add friends --> " + alip.getContact(x).displayName)
            time.sleep(random.uniform(1, 2))
    print("Success Syncronize All Friends")


# main
creator = statusalip["Creator"]  # <<< masukan mid kamu di statusalip.json
owner = statusalip["Owner"]  # <<< masukan mid kamu di statusalip.json
Bots = statusalip["Bots"]
Blacklist = statusalip["Blacklist"]


wait = {
    "keyCmd": "x",
    "dBlacklist": False,
    "NukeJoin": False,
    "silent": False,
    "warmode": False,
    "updatepict": False,
    "updatecover": False,
    "ajs": {"forceAjs": True, "updatepict": False, "updatecover": False},
    "realtedWithAdmin": {},
}


def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def command(text, msg_from):
    pesan = text.lower()
    if msg_from in alip.FindDuplicatedAndRemove(creator, owner):
        if pesan.startswith(wait["keyCmd"]):
            cmd = pesan.replace(wait["keyCmd"], "")
        else:
            cmd = ""
        return cmd
    else:
        cmd = pesan.replace(pesan, "")
        return pesan


def sendMentionv2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {"S": str(slen), "E": str(elen - 4), "M": mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {"S": str(slen), "E": str(elen - 4), "M": mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    alip.sendMessage(
        to, textx, {"MENTION": str('{"MENTIONEES":' + json.dumps(arr) + "}")}, 0
    )


def super_mention(to, status, text, dataMid=[], pl="", ps="", pg="", pt=[]):
    arr = []
    list_text = ps
    i = 0
    no = pl
    if pg == "DeleteBlacklist":
        for l in dataMid:
            try:
                Blacklist.remove(l)
            except:
                continue
            no += 1
            if no == len(pt):
                list_text += "\n" + str(no) + ". @[wew-" + str(i) + "] "
            else:
                list_text += "\n" + str(no) + ". @[wew-" + str(i) + "] "
            i = i + 1
        text = list_text
    if pg == "DeleteWhitelist":
        for l in dataMid:
            try:
                Bots.remove(l)
            except:
                continue
            no += 1
            if no == len(pt):
                list_text += "\n" + str(no) + ". @[wew-" + str(i) + "] "
            else:
                list_text += "\n" + str(no) + ". @[wew-" + str(i) + "] "
            i = i + 1
        text = list_text
    i = 0
    for l in dataMid:
        if l not in alipMID:
            mid = l
            name = "@[alp-" + str(i) + "]"
            ln_text = text.replace("\n", " ")
            if ln_text.find(name):
                line_s = int(ln_text.index(name))
                line_e = int(line_s) + int(len(name))
            arrData = {"S": str(line_s), "E": str(line_e), "M": mid}
            arr.append(arrData)
            i = i + 1
    alip.sendMessage(
        to, text, {"MENTION": str('{"MENTIONEES":' + json.dumps(arr) + "}")}, 0
    )


def AddBlacklist(target):
    if target not in Blacklist:
        if target not in alip.FindDuplicatedAndRemove(creator, owner, Bots):
            Blacklist.append(target)


def lockqr(group):
    group = alip.getChats([group]).chats[0]
    G = group.extra.groupExtra.preventedJoinByTicket = False
    alip.updateChat(group, G)


def purge(group):
    try:
        wait["dblacklist"] = True
        threads = []
        alip.inviteIntoChat(group, [Bots])
        for a in Blacklist:
            t = threading.Thread(target=alip.deleteOtherFromChat(group, [a]))
            threads.append(t)
        for t in threads:
            t.start()
    except:
        wait["dblacklist"] = False


def NOTIFIED_KICKOUT_FROM_GROUP(op):
    group = op.param1
    executor = op.param2
    target = op.param3
    if executor in Blacklist:
        try:
            purge(group)
        except Exception as e:
            print(e)
    if executor not in alip.FindDuplicatedAndRemove(creator, owner, Bots):
        if target in alip.FindDuplicatedAndRemove(creator, owner, Bots):
            if group in statusalip["protect"]["kick"]:
                try:
                    AddBlacklist(executor)
                    alip.deleteOtherFromChat(group, [executor])
                    alip.findAndAddContactsByMid(target)
                    alip.inviteIntoChat(group, [target])
                except Exception as e:
                    print(e)
            else:
                try:
                    AddBlacklist(executor)
                    alip.deleteOtherFromChat(group, [executor])
                    alip.inviteIntoChat(group, [target])
                except Exception as e:
                    print(e)
    if ajsMID != None:
        if target in ajsMID:
            try:
                AddBlacklist(executor)
                alip.deleteOtherFromChat(group, [executor])
                alip.inviteIntoChat(group, [ajsMID])
            except:
                pass
        if target in alipMID:
            G = ajs.getChats([group]).chats[0]
            pends = list(G.extra.groupExtra.inviteeMids)
            if ajsMID in pends:
                AddBlacklist(executor)
                ajs.acceptChatInvitation(group)
                time.sleep(0.8)
                ajs.deleteOtherFromChat(group, [executor])
                ajs.inviteIntoChat(group, [alipMID])
                time.sleep(1.8)
                alip.acceptChatInvitation(group)
                ajs.deleteSelfFromChat(group)
                if wait["ajs"]["forceAjs"] == True:
                    time.sleep(0.8)
                    alip.inviteIntoChat(group, [ajsMID])


def NOTIFIED_CANCEL_INVITATION_GROUP(op):
    group = op.param1
    executor = op.param2
    target = op.param3
    print("cancel", group, executor, target)
    if executor in Blacklist:
        try:
            purge(group)
        except Exception as e:
            print(e)
    if executor not in alip.FindDuplicatedAndRemove(creator, owner, Bots):
        if target in alip.FindDuplicatedAndRemove(creator, owner, Bots):
            try:
                AddBlacklist(executor)
                alip.deleteOtherFromChat(group, [executor])
                alip.inviteIntoChat(group, [target])
            except Exception as e:
                print(e)
        if group in statusalip["protect"]["cancel"]:
            try:
                AddBlacklist(executor)
                alip.deleteOtherFromChat(group, [executor])
                alip.findAndAddContactsByMid(target)
                alip.inviteIntoChat(group, [target])
            except Exception as e:
                print(e)
    if ajsMID != None:
        if target == ajsMID:
            try:
                AddBlacklist(executor)
                alip.deleteOtherFromChat(group, [target])
                alip.inviteIntoChat(group, [ajsMID])
            except:
                pass
        if target == alipMID:
            G = ajs.getChats([group]).chats[0]
            pends = list(G.extra.groupExtra.inviteeMids)
            if ajsMID in pends:
                ajs.acceptChatInvitation(group)
                time.sleep(0.8)
                AddBlacklist(executor)
                ajs.deleteOtherFromChat(group, [executor])
                ajs.inviteIntoChat(group, [alipMID])
                time.sleep(1.8)
                alip.acceptChatInvitation(group)
                ajs.deleteSelfFromChat(group)
                if wait["ajs"]["forceAjs"] == True:
                    time.sleep(0.8)
                    alip.inviteIntoChat(group, [ajsMID])


def NOTIFIED_INVITE_INTO_GROUP(op):
    group = op.param1
    executor = op.param2
    target = op.param3
    if alipMID in target:
        if executor in alip.FindDuplicatedAndRemove(creator, owner, Bots):
            alip.acceptChatInvitation(group)
        elif ajsMID != None:
            if executor == ajsMID:
                alip.acceptChatInvitation(group)
    if executor in Blacklist:
        lipacans = target.split("\x1e")
        alip.deleteOtherFromChat(group, [executor])
        for x in lipacans:
            try:
                AddBlacklist(x)
                alip.cancelChatInvitation(group, [x])
            except Exception as e:
                print(e)
    if wait["warmode"] == True:
        if target not in alip.FindDuplicatedAndRemove(creator, owner, Bots):
            AddBlacklist(executor)
    if wait["NukeJoin"] == True:
        try:
            G = alip.getChats([group]).chats[0]
            mems = list(G.extra.groupExtra.memberMids)
            targk = []
            for x in mems[0:150]:
                if x not in alip.FindDuplicatedAndRemove(creator, owner, Bots):
                    targk.append(x)
            nazwa = "kickall.js gid={} token={}".format(
                group, str(statusalip["assistToken"])
            )
            for x in targk:
                nazwa += " uik={}".format(x)
            execute_js(nazwa)
            time.sleep(0.8)
        except Exception as e:
            print(e)
    if group in statusalip["protect"]["invite"]:
        if executor not in alip.FindDuplicatedAndRemove(creator, owner, Bots):
            if executor in Blacklist:
                AddBlacklist(executor)
                lipacans = target.split("\x1e")
                alip.deleteOtherFromChat(group, [executor])
                for x in lipacans:
                    try:
                        AddBlacklist(x)
                        alip.cancelChatInvitation(group, [x])
                    except Exception as e:
                        print(e)
            if group in statusalip["protect"]["join"]:
                if executor in alip.FindDuplicatedAndRemove(creator, owner, Bots):
                    lipacans = target.split("\x1e")
                    for x in lipacans:
                        try:
                            if group not in wait["realtedWithAdmin"]:
                                wait["realtedWithAdmin"][group] = [x]
                            else:
                                wait["realtedWithAdmin"][group].append(x)
                        except Exception as e:
                            print(e)


def NOTIFIED_ACCEPT_GROUP_INVITATION(op):
    group = op.param1
    executor = op.param2
    if executor in Blacklist:
        try:
            alip.deleteOtherFromChat(group, [executor])
            lockqr(group)
        except:
            if ajsMID != None:
                G = ajs.getChats([group]).chats[0]
                pends = list(G.extra.groupExtra.inviteeMids)
                if ajsMID in pends:
                    ajs.acceptChatInvitation(group)
                    try:
                        lockqr(group)
                        ajs.deleteOtherFromChat(group, [executor])
                        ajs.inviteIntoChat(group, [alipMID])
                        time.sleep(1.8)
                        alip.acceptChatInvitation(group)
                        ajs.deleteSelfFromChat(group)
                        if wait["ajs"]["forceAjs"] == True:
                            time.sleep(0.8)
                            alip.inviteIntoChat(group, [ajsMID])
                    except Exception as e:
                        print(e)
    if wait["warmode"] == True:
        if executor not in alip.FindDuplicatedAndRemove(creator, owner, Bots):
            AddBlacklist(executor)
    if group in statusalip["protect"]["join"]:
        if executor not in alip.FindDuplicatedAndRemove(creator, owner, Bots):
            if executor not in wait["realtedWithAdmin"][group]:
                AddBlacklist(executor)
                try:
                    alip.deleteOtherFromChat(group, [executor])
                    lockqr(group)
                except:
                    if ajsMID != None:
                        G = ajs.getChats([group]).chats[0]
                        pends = list(G.extra.groupExtra.inviteeMids)
                        if ajsMID in pends:
                            ajs.acceptChatInvitation(group)
                            try:
                                lockqr(group)
                                ajs.deleteOtherFromChat(group, [executor])
                                ajs.inviteIntoChat(group, [alipMID])
                                time.sleep(1.8)
                                alip.acceptChatInvitation(group)
                                ajs.deleteSelfFromChat(group)
                                if wait["ajs"]["forceAjs"] == True:
                                    time.sleep(0.8)
                                    alip.inviteIntoChat(group, [ajsMID])
                            except Exception as e:
                                print(e)


def NOTIFIED_UPDATE_GROUP(op):
    group = op.param1
    executor = op.param2
    if executor in Blacklist:
        try:
            alip.deleteOtherFromChat(group, [executor])
            lockqr(group)
        except Exception as e:
            print(e)
    if wait["warmode"] == True:
        if executor not in alip.FindDuplicatedAndRemove(creator, owner, Bots):
            AddBlacklist(executor)
    if statusalip["protect"]["qr"]:
        if executor not in alip.FindDuplicatedAndRemove(creator, owner, Bots):
            try:
                AddBlacklist(executor)
                alip.deleteOtherFromChat(group, [executor])
                lockqr(group)
            except Exception as e:
                print(e)


def NOTIFIED_READ_MESSAGE(op):
    group = op.param1
    executor = op.param2
    if executor in Blacklist:
        alip.deleteOtherFromChat(group, [executor])


def RECEIVE_MESSAGE(op):
    global time
    global ast
    global Blacklist
    global Bots
    if wait["silent"] == False:
        msg = op.message
        text = msg.text
        msg_id = msg.id
        receiver = msg.to
        sender = msg._from
        if msg.toType == 0 or msg.toType == 2:
            if msg.toType == 0:
                to = receiver
            elif msg.toType == 2:
                to = receiver
            if msg.contentType == 1:
                if wait["updatepict"] == True:
                    alip.updatePictAssist(header, statusalip["assistSecondary"], msg_id)
                    alip.sendMessage(to, "Success change Assist pict")
                    wait["updatepict"] = False
                if wait["updatecover"] == True:
                    alip.updatePictCover(header, statusalip["assistSecondary"], msg_id)
                    alip.sendMessage(to, "Success change Assist cover")
                    wait["updatecover"] = False
                if wait["ajs"]["updatepict"] == True:
                    alip.updatePictAssist(header, statusalip["ajsSecondary"], msg_id)
                    alip.sendMessage(to, "Success change Ajs pict")
                    wait["ajs"]["updatepict"] = False
                if wait["ajs"]["updatecover"] == True:
                    alip.updatePictCover(header, statusalip["ajsSecondary"], msg_id)
                    alip.sendMessage(to, "Success change Ajs cover")
                    wait["ajs"]["updatecover"] = False
            if msg.contentType == 0:
                if text is None:
                    return
                else:
                    cmd = command(text, sender)
                    cooms = str(wait["keyCmd"])
                    if cmd == "help":
                        txt = "</> Status :"
                        if ajsMID != None:
                            txt += "\n<> Ajs mode : ON"
                        else:
                            txt += "\n<> Ajs mode : OFF"
                        if wait["warmode"] == True:
                            txt += "\nWar mode: ON"
                        else:
                            txt += "\nWar mode: OFF"
                        if wait["NukeJoin"] == True:
                            txt += "\nNuke Join: ON"
                        else:
                            txt += "\nNuke Join: OFF"
                        txt += "\n\n</> Commands Bots :"
                        txt += "\n⌖ " + cooms + "about"
                        txt += "\n⌖ " + cooms + "addbot <tag>"
                        txt += "\n⌖ " + cooms + "banlist"
                        txt += "\n⌖ " + cooms + "botlist"
                        txt += "\n⌖ " + cooms + "clearbot"
                        txt += "\n⌖ " + cooms + "clearban"
                        txt += "\n⌖ " + cooms + "delban <num> or/w <-/,>"
                        txt += "\n⌖ " + cooms + "delbot <num> or/w <-/,>"
                        txt += "\n⌖ " + cooms + "nukejoin  <on/off>"
                        txt += "\n⌖ " + cooms + "silent <on/off>"
                        txt += "\n⌖ " + cooms + "nuke"
                        txt += "\n⌖ " + cooms + "kick  <tag>"
                        txt += "\n⌖ " + cooms + "speed"
                        txt += "\n⌖ " + cooms + "out / out all"
                        txt += "\n⌖ " + cooms + "restart"
                        txt += "\n⌖ " + cooms + "profile"
                        txt += "\n⌖ " + cooms + "protect"
                        txt += "\n⌖ " + cooms + "glist"
                        if ajsMID != None:
                            txt += "\n⌖ " + cooms + "ajs <stay/denay/in>"
                        else:
                            txt += "\n⌖ " + cooms + "runajs <primary token>"
                        txt += "\n\n</> Keys Settings"
                        txt += "\n⌖ Keys:  " + cooms
                        txt += "\n⌖ Resetkey"
                        txt += "\n⌖ Mykey"
                        txt += "\n⌖ " + cooms + "addkey  <text>"
                        alip.sendMessage(to, str(txt))

                    elif cmd.startswith("runajs "):
                        xae1 = cmd.split(" ")[0]
                        xae2 = cmd.replace(xae1 + " ", "")
                        xtok = ConvPrim(xae2, header)
                        test = LINEBOT(myToken=str(xtok), myApp=header)
                        testMID = test.profile.mid
                        if testMID:
                            statusalip["ajsToken"] = xae2
                            statusalip["ajsSecondary"] = xtok
                            sendMentionv2(to, " @! Ajs Login", [testMID])
                            restartBot()
                        else:
                            alip.sendMessage(to, "Failed to login Ajs")

                    elif cmd == "glist":
                        CM = alip.getAllChatMids()
                        r = "</> Group List :"
                        r += f"\n⌖ Groups:"
                        if len(list(CM.memberChatMids)) != 0:
                            for i, x in enumerate(list(CM.memberChatMids)):
                                r += (
                                    f"\n\t\t[{i+1}] "
                                    + str(alip.getChats([x]).chats[0].chatName)[0:15]
                                    + "... ("
                                    + str(
                                        len(
                                            list(
                                                alip.getChats([x])
                                                .chats[0]
                                                .extra.groupExtra.memberMids
                                            )
                                        )
                                    )
                                    + ")"
                                )
                        else:
                            r += f"\n\t\t[x] No Group Joined"
                        r += f"\n⌖ Pendings:"
                        if len(list(CM.invitedChatMids)) != 0:
                            for i, x in enumerate(list(CM.invitedChatMids)):
                                r += (
                                    f"\n\t\t[{i+1}] "
                                    + str(alip.getChats([x]).chats[0].chatName)[0:15]
                                    + "... ("
                                    + str(
                                        len(
                                            list(
                                                alip.getChats([x])
                                                .chats[0]
                                                .extra.groupExtra.inviteeMids
                                            )
                                        )
                                    )
                                    + ")"
                                )
                        else:
                            r += f"\n\t\t[x] No Pending Group"
                        alip.sendMessage(to, str(r))

                    elif cmd == "protect":
                        txt = "</> Commands Bots :"
                        for i in list(statusalip["protect"]):
                            txt += f"\n⌖ {cooms}prot {i} <on/off>"
                        txt += f"\n⌖ {cooms}prot all <on/off>"
                        txt += f"\n⌖ {cooms}protect list"
                        alip.sendMessage(to, str(txt))

                    elif cmd.startswith("prot "):
                        xae1 = cmd.split(" ")[0]
                        xae2 = cmd.replace(xae1 + " ", "")
                        if xae2 == "kick on":
                            if to not in statusalip["protect"]["kick"]:
                                statusalip["protect"]["kick"].append(to)
                            alip.sendMessage(to, "Success add protect kick")
                        elif xae2 == "kick off":
                            if to in statusalip["protect"]["kick"]:
                                statusalip["protect"]["kick"].remove(to)
                            alip.sendMessage(to, "Success remove protect kick")
                        elif xae2 == "join on":
                            if to not in statusalip["protect"]["join"]:
                                statusalip["protect"]["join"].append(to)
                            alip.sendMessage(to, "Success add protect join")
                        elif xae2 == "join off":
                            if to in statusalip["protect"]["join"]:
                                statusalip["protect"]["join"].remove(to)
                            alip.sendMessage(to, "Success remove protect join")
                        elif xae2 == "qr on":
                            if to not in statusalip["protect"]["qr"]:
                                statusalip["protect"]["qr"].append(to)
                            alip.sendMessage(to, "Success add protect qr")
                        elif xae2 == "qr off":
                            if to in statusalip["protect"]["qr"]:
                                statusalip["protect"]["qr"].remove(to)
                            alip.sendMessage(to, "Success remove protect qr")
                        elif xae2 == "invite on":
                            if to not in statusalip["protect"]["invite"]:
                                statusalip["protect"]["invite"].append(to)
                            alip.sendMessage(to, "Success add protect invite")
                        elif xae2 == "invite off":
                            if to in statusalip["protect"]["invite"]:
                                statusalip["protect"]["invite"].remove(to)
                            alip.sendMessage(to, "Success remove protect invite")
                        elif xae2 == "cancel on":
                            if to not in statusalip["protect"]["cancel"]:
                                statusalip["protect"]["cancel"].append(to)
                            alip.sendMessage(to, "Success add protect cancel")
                        elif xae2 == "cancel off":
                            if to in statusalip["protect"]["cancel"]:
                                statusalip["protect"]["cancel"].remove(to)
                            alip.sendMessage(to, "Success remove protect cancel")
                        elif xae2 == "all on":
                            for x in statusalip["protect"]:
                                if to not in statusalip["protect"][x]:
                                    statusalip["protect"][x].append(to)
                            alip.sendMessage(to, "Success add protect all")
                        elif xae2 == "all off":
                            for x in statusalip["protect"]:
                                if to in statusalip["protect"][x]:
                                    statusalip["protect"][x].remove(to)
                            alip.sendMessage(to, "Success remove protect all")

                    elif cmd == "protect list":
                        r = "</> Protect List :"
                        for x in list(statusalip["protect"]):
                            r += f"\n⌖ Protect {x}:"
                            if len(list(statusalip["protect"][x])) != 0:
                                for i, xx in enumerate(list(statusalip["protect"][x])):
                                    r += (
                                        f"\n\t\t[{i+1}] "
                                        + alip.getChats([xx]).chats[0].chatName
                                    )
                            else:
                                r += "\n\t\t[x] No Protect"
                        alip.sendMessage(to, str(r))

                    elif cmd == "profile":
                        txt = "</> Commands Bots :"
                        txt += "\n⌖ " + cooms + "update pict"
                        txt += "\n⌖ " + cooms + "update cover"
                        txt += "\n⌖ " + cooms + "upname [name]"
                        txt += "\n⌖ " + cooms + "upbio [bio]"
                        if ajsMID != None:
                            txt += "\n⌖ " + cooms + "update pict ajs"
                            txt += "\n⌖ " + cooms + "update cover ajs"
                            txt += "\n⌖ " + cooms + "upnameajs [name]"
                            txt += "\n⌖ " + cooms + "upbioajs [bio]"
                        alip.sendMessage(to, str(txt))

                    elif cmd == "update pict":
                        wait["updatepict"] = True
                        alip.sendMessage(to, "Please send pict")

                    elif cmd == "update cover":
                        wait["updatecover"] = True
                        alip.sendMessage(to, "Please send pict")

                    elif cmd.startswith("upname "):
                        xae1 = cmd.split(" ")[0]
                        xae2 = cmd.replace(xae1 + " ", "")
                        alip.updateProfileAttribute(ProfileAttribute.DISPLAY_NAME, xae2)
                        alip.sendMessage(to, f"Success change display name: {xae2}")

                    elif cmd.startswith("upbio "):
                        xae1 = cmd.split(" ")[0]
                        xae2 = cmd.replace(xae1 + " ", "")
                        alip.updateProfileAttribute(
                            ProfileAttribute.STATUS_MESSAGE, xae2
                        )
                        alip.sendMessage(to, f"Success change bio: {xae2}")

                    elif cmd == "update pict ajs":
                        if ajsMID != None:
                            wait["ajs"]["updatepict"] = True
                            alip.sendMessage(to, "Please send pict")

                    elif cmd == "update cover ajs":
                        if ajsMID != None:
                            wait["ajs"]["updatecover"] = True
                            alip.sendMessage(to, "Please send pict")

                    elif cmd.startswith("upnameajs "):
                        if ajsMID != None:
                            xae1 = cmd.split(" ")[0]
                            xae2 = cmd.replace(xae1 + " ", "")
                            ajs.updateProfileAttribute(
                                ProfileAttribute.DISPLAY_NAME, xae2
                            )
                            alip.sendMessage(to, f"Success change display name: {xae2}")

                    elif cmd.startswith("upbioajs "):
                        if ajsMID != None:
                            xae1 = cmd.split(" ")[0]
                            xae2 = cmd.replace(xae1 + " ", "")
                            ajs.updateProfileAttribute(
                                ProfileAttribute.STATUS_MESSAGE, xae2
                            )
                            alip.sendMessage(to, f"Success change bio: {xae2}")

                    elif cmd == "ajs stay":
                        if ajsMID:
                            G = ajs.getChats([to]).chats[0]
                            pends = list(G.extra.groupExtra.inviteeMids)
                            mems = list(G.extra.groupExtra.memberMids)
                            if ajsMID not in pends + mems:
                                alip.inviteIntoChat(to, [ajsMID])
                            elif ajsMID in mems:
                                ajs.deleteSelfFromChat(to)
                                time.sleep(0.8)
                                alip.inviteIntoChat(to, [ajsMID])
                            elif ajsMID not in pends:
                                alip.sendMessage(to, "Ajs Alredy Stay mode")
                        else:
                            alip.sendMessage(to, "in Assist mode, Ajs not found")

                    elif cmd == "ajs denay":
                        if ajsMID:
                            G = ajs.getChats([to]).chats[0]
                            pends = list(G.extra.groupExtra.inviteeMids)
                            mems = list(G.extra.groupExtra.memberMids)
                            if ajsMID in pends:
                                alip.cancelGroupInvitation(to, [ajsMID])
                            elif ajsMID in mems:
                                ajs.deleteSelfFromChat(to)
                            elif ajsMID not in pends + mems:
                                alip.sendMessage(to, "Ajs Not in Stay mode")
                        else:
                            alip.sendMessage(to, "in Assist mode, Ajs not found")

                    elif cmd == "silent on":
                        wait["silent"] = True
                        alip.sendMessage(to, "Bot Mute")
                    elif cmd == "war on":
                        wait["warmode"] = True
                        alip.sendMessage(to, "WarMode on")
                    elif cmd == "war off":
                        wait["warmode"] = False
                        alip.sendMessage(to, "WarMode off")
                    elif cmd == "about":
                        c = "[About LINE CL Assist V2]"
                        if ajsMID != None:
                            tp = "Singel Assist"
                        else:
                            tp = "Assist Ajs"
                        c += "\n> Type: " + tp
                        c += "\n> Ver: " + VersionBot
                        c += "\n> Author:"
                        c += "\n> -Alip Budiman"
                        c += "\n> www.fxgdev.site/alifbudiman.html"
                        alip.sendMessage(to, c)
                    elif cmd == "speed":
                        start = time.time()
                        alip.sendMessage(to, "calculating")
                        total = time.time() - start
                        alip.sendMessage(to, str(total))
                    elif cmd == "out":
                        alip.sendMessage(to, "oke i'm out")
                        alip.deleteSelfFromChat(to)
                    elif cmd == "out all":
                        alip.sendMessage(to, "Processing clear group")
                        for x in list(alip.getAllChatMids().memberChatMids):
                            if x not in to:
                                alip.deleteSelfFromChat(x)
                                time.sleep(random.uniform(1, 2))
                        alip.sendMessage(to, "Success out all groups")
                    elif cmd == "restart":
                        alip.sendMessage(to, "restarted...")
                        restartBot()
                    elif text.lower() == "mykey":
                        if wait["keyCmd"] != "":
                            alip.sendMessage(to, str(wait["keyCmd"]))
                        else:
                            alip.sendMessage(to, "Key is Empty")
                    elif text.lower() == "resetkey":
                        wait["keyCmd"] = ""
                        alip.sendMessage(msg.to, "Reset...")
                    elif cmd.startswith("addkey "):
                        sep = text.split(" ")
                        key = text.replace(sep[0] + " ", "")
                        if key in ["", " ", "\n", None]:
                            alip.sendMessage(msg.to, "Add Key Fail...")
                        else:
                            wait["keyCmd"] = str(key).lower()
                            alip.sendMessage(msg.to, "Key Added: {}".format(str(key)))
                    elif cmd.startswith("kick "):
                        try:
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            nazwa = "kickall.js gid={} token={}".format(
                                to, str(statusalip["assistToken"])
                            )
                            for x in key["MENTIONEES"]:
                                nazwa += " uik={}".format(x["M"])
                                AddBlacklist(x["M"])
                            execute_js(nazwa)
                            time.sleep(0.8)
                        except Exception as e:
                            alip.sendMessage(to, str(e))
                    elif cmd == "nuke":
                        try:
                            group = alip.getChats([to]).chats[0]
                            mems = list(group.extra.groupExtra.memberMids)
                            targk = []
                            for x in mems[0:150]:
                                if x not in alip.FindDuplicatedAndRemove(
                                    creator, owner, Bots
                                ):
                                    targk.append(x)
                            nazwa = "kickall.js gid={} token={}".format(
                                to, str(statusalip["assistToken"])
                            )
                            for x in targk:
                                nazwa += " uik={}".format(x)
                            execute_js(nazwa)
                            time.sleep(0.8)
                        except Exception as e:
                            alip.sendMessage(to, str(e))
                    elif cmd == "nukejoin on":
                        wait["NukeJoin"] = True
                        alip.sendMessage(to, "Becarfule, Kickall Join ON")
                    elif cmd == "nukejoin off":
                        wait["NukeJoin"] = False
                        alip.sendMessage(to, "Becarfule, Kickall Join OFF")
                    elif cmd.startswith("delban"):
                        data = cmd.replace("delban", "")
                        sep = data.split(" ")
                        num = str(sep[1])
                        selection = Archimed(num, range(1, len(Blacklist) + 1))
                        k = len(Blacklist) // 100
                        d = []
                        for a in selection.parse():
                            d.append(Blacklist[int(a) - 1])
                        for a in range(k + 1):
                            if a == 0:
                                super_mention(
                                    to=receiver,
                                    status=statusalip,
                                    text="",
                                    dataMid=d[:100],
                                    pl=-0,
                                    ps="「Delete Blacklist」\n",
                                    pg="DeleteBlacklist",
                                    pt=d,
                                )
                            else:
                                super_mention(
                                    to=receiver,
                                    status=statusalip,
                                    text="",
                                    dataMid=d[a * 100 : (a + 1) * 100],
                                    pl=a * 100,
                                    ps="「Delete Blacklist」\n",
                                    pg="DeleteBlacklist",
                                    pt=d,
                                )
                    elif cmd.startswith("delbot"):
                        data = cmd.replace("delbot", "")
                        sep = data.split(" ")
                        num = str(sep[1])
                        selection = Archimed(num, range(1, len(Bots) + 1))
                        k = len(Bots) // 100
                        d = []
                        for a in selection.parse():
                            d.append(Bots[int(a) - 1])
                        for a in range(k + 1):
                            if a == 0:
                                super_mention(
                                    to=receiver,
                                    status=statusalip,
                                    text="",
                                    dataMid=d[:100],
                                    pl=-0,
                                    ps="「Delete Whitelist」\n",
                                    pg="DeleteWhitelist",
                                    pt=d,
                                )
                            else:
                                super_mention(
                                    to=receiver,
                                    status=statusalip,
                                    text="",
                                    dataMid=d[a * 100 : (a + 1) * 100],
                                    pl=a * 100,
                                    ps="「Delete Whitelist」\n",
                                    pg="DeleteWhitelist",
                                    pt=d,
                                )
                    elif cmd == "clearban":
                        Blacklist = []
                        alip.sendMessage(to, "Done Clear Blacklist")
                    elif cmd == "clearbot":
                        Bots = []
                        alip.sendMessage(to, "Done Clear Whitelist")
                    elif cmd == "banlist":
                        if len(Blacklist) > 0:
                            h = [a for a in Blacklist]
                            k = len(h) // 10
                            for aa in range(k + 1):
                                if aa == 0:
                                    dd = "Blacklist User:\n"
                                    no = aa
                                else:
                                    dd = ""
                                    no = aa * 10
                                msgas = dd
                                for a in h[aa * 10 : (aa + 1) * 10]:
                                    no += 1
                                    if no == len(h):
                                        msgas += "\n{}. @!".format(no)
                                    else:
                                        msgas += "\n{}. @!".format(no)
                                sendMentionv2(to, msgas, h[aa * 10 : (aa + 1) * 10])
                        else:
                            alip.sendMessage(to, "Empty")
                    elif cmd == "botlist":
                        if len(Bots) > 0:
                            h = [a for a in Bots]
                            k = len(h) // 10
                            for aa in range(k + 1):
                                if aa == 0:
                                    dd = "Bots User:\n"
                                    no = aa
                                else:
                                    dd = ""
                                    no = aa * 10
                                msgas = dd
                                for a in h[aa * 10 : (aa + 1) * 10]:
                                    no += 1
                                    if no == len(h):
                                        msgas += "\n{}. @!".format(no)
                                    else:
                                        msgas += "\n{}. @!".format(no)
                                sendMentionv2(to, msgas, h[aa * 10 : (aa + 1) * 10])
                        else:
                            alip.sendMessage(to, "Empty")
                    elif cmd.startswith("addbot "):
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            if x["M"] not in Blacklist:
                                try:
                                    if x["M"] not in Bots:
                                        if x["M"] in alipMID:
                                            pass
                                        else:
                                            Bots.append(x["M"])
                                            alip.findAndAddContactsByMid(x["M"])
                                            sendMentionv2(
                                                to, " @! Add to Access list", [x["M"]]
                                            )
                                    else:
                                        sendMentionv2(
                                            to, " @! Alredy in Access list", [x["M"]]
                                        )
                                except:
                                    pass
                            else:
                                alip.sendMessage(msg.id, to, "In Blacklist user")


def worker(op):
    try:
        if op.type != 0:
            if op.type == 19 or op.type == 133:
                try:
                    NOTIFIED_KICKOUT_FROM_GROUP(op)
                except Exception as e:
                    print(e)
            if op.type == 32 or op.type == 126:
                try:
                    NOTIFIED_CANCEL_INVITATION_GROUP(op)
                except Exception as e:
                    print(e)
            if op.type == 11 or op.type == 122:
                try:
                    NOTIFIED_UPDATE_GROUP(op)
                except Exception as e:
                    print(e)
            if op.type == 13 or op.type == 124:
                try:
                    NOTIFIED_INVITE_INTO_GROUP(op)
                except Exception as e:
                    print(e)
            if op.type == 17 or op.type == 130:
                try:
                    NOTIFIED_ACCEPT_GROUP_INVITATION(op)
                except Exception as e:
                    print(e)
            if op.type == 55:
                try:
                    NOTIFIED_READ_MESSAGE(op)
                except Exception as e:
                    print(e)
            if op.type == 26:
                try:
                    RECEIVE_MESSAGE(op)
                except Exception as e:
                    print(e)
    except Exception as error:
        print(error)
        if error in ["", " ", None]:
            if len(error) < 3:
                python3 = sys.executable
                os.execl(python3, python3, *sys.argv)


if owner == []:
    sys.exit(
        "mid owner tidak boleh kosong, silahkan masukan mid owner di statusalip.sjon"
    )
if creator == []:
    sys.exit(
        "mid creator tidak boleh kosong, silahkan masukan mid creator di statusalip.sjon"
    )


def RunningThreadPollExecutor():
    if ajsMID != None:
        print("Running Singel Thread with Ajs")
        while True:
            try:
                ops = alip.fetchOps()
                for op in ops:
                    if op.revision == -1 and op.param2 != None:
                        alip.globalRev = int(op.param2.split("\x1e")[0])
                    if op.revision == -1 and op.param1 != None:
                        alip.individualRev = int(op.param1.split("\x1e")[0])
                    alip.localRev = max(op.revision, alip.localRev)
                    worker(op)
            except Exception as e:
                e = traceback.format_exc()
                if "EOFError" in e:
                    pass
                elif "ShouldSyncException" in e or "LOG_OUT" in e:
                    python3 = sys.executable
                    os.execl(python3, python3, *sys.argv)
                else:
                    traceback.print_exc()
                continue
            except KeyboardInterrupt:
                sys.exit("##---- KEYBOARD INTERRUPT -----##")
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            print("Multi Singel Thread with Singel Assist mode")
            while True:
                try:
                    ops = alip.fetchOps()
                    for op in ops:
                        if op.revision == -1 and op.param2 != None:
                            alip.globalRev = int(op.param2.split("\x1e")[0])
                        if op.revision == -1 and op.param1 != None:
                            alip.individualRev = int(op.param1.split("\x1e")[0])
                        alip.localRev = max(op.revision, alip.localRev)
                        executor.submit(worker, op)
                except Exception as e:
                    e = traceback.format_exc()
                    if "EOFError" in e:
                        pass
                    elif "ShouldSyncException" in e or "LOG_OUT" in e:
                        python3 = sys.executable
                        os.execl(python3, python3, *sys.argv)
                    else:
                        traceback.print_exc()
                    continue
                except KeyboardInterrupt:
                    sys.exit("##---- KEYBOARD INTERRUPT -----##")


if __name__ == "__main__":
    if ajsMID != None:
        AlipKedua()
    SyncAllFriends()
    RunningThreadPollExecutor()
