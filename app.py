# ===== ===== ===== ===== ===== 【宣告區域】 ===== ===== ===== ===== =====

    ##### 版本 ######
strVer = '(MA14)1214'
    # ***** ***** ***** ***** *****

    ##### (SJ)推播 ######
import requests
    # ***** ***** ***** ***** *****


    ##### 時間函數 ######
from datetime import datetime
import time
    # ***** ***** ***** ***** *****

    ##### Line ######
from config import * 
# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
# from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction

line_bot_api = LineBotApi(strchannel_access_token)
handler = WebhookHandler(strchannel_secret)
    # ***** ***** ***** ***** *****

    ##### Flask ######
from flask import Flask, abort, request
app = Flask(__name__)
    # ***** ***** ***** ***** *****

    ##### 日期時間 ######
from datetime import datetime
    # ***** ***** ***** ***** *****

    ##### 自訂函數功能 ######
from rm_initial import *
from ri_text_01 import *
from ri_parameters_01 import *
from rf_string_01 import *
from rf_string_02 import *
from rf_datetime_01 import *
import rf_sqldb_01 as pymsdb
from rf_sqldb_02 import *
from rf_line_01 import *
    # ***** ***** ***** ***** *****

    ##### Line Callback ######
@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"
    # ***** ***** ***** ***** *****

# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 取得事件變數
    strEventMSG = event.message.text

    ##### 取得Line訊息 #####
    pfProfile = line_bot_api.get_profile(event.source.user_id)
    strLineDisplayName = pfProfile.display_name
    strLineUserID = pfProfile.user_id
    # ***** ***** ***** ***** *****

    ##### 取得當下時間 #####
    FVdatNow = datetime.now()
    FVstrToday = FVdatNow.strftime("%Y-%m-%d") 
    FVstrNow = FVdatNow.strftime("%Y-%m-%d %H:%M:%S") 
    # FVstrLCNow = time.strftime("%Y-%m-%d %H:%M:%S.%f", time.localtime())
    FVstrGMNow = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    FVdatGMNow = datetime.strptime(FVstrGMNow, "%Y-%m-%d %H:%M:%S") 
    # ***** ***** ***** ***** *****

    ##### 全型符號轉換 #####
    strEventMSG = RS_Replace_FullChar_2_SemiChar(strEventMSG)
    # ***** ***** ***** ***** *****

    ##### 關鍵字處理大寫消兩側空白 #####
    strEventMSG = strEventMSG.upper()
    strEventMSG = strEventMSG.strip()
    # ***** ***** ***** ***** *****

    # 確認資料類別
    get_TYPE_message = 'Initial'

    if strEventMSG == '您好':
        # (A)禮貌回覆
        strReply_MSG = '『臺南市新吉工業區廠協會』：您好' + event.message.text

    ##### (SJ)推播 #####
    elif (strEventMSG[0:4].upper() == 'SJ推播'):
        ##### 此項需有權限才能執行 #####
        strAUTHKWQuery = 'SJPUSH'
        strAUTH_CHK = RS_CHECK_KWAUTH_by_UserId(strLineUserID, strAUTHKWQuery)
        if strAUTH_CHK[0:2] == 'GO':            
            #類別
            get_TYPE_message = 'SYS_ASSIGN_PUSH_MSG_Text'
            #開頭的關鍵字長度
            if strEventMSG[0:4].upper() == 'SJ推播':
                intInitialKWLen = 4
            strPushKW = RS_RIGHT_String_NotLeftStrNum(strEventMSG, intInitialKWLen)
            #strReply_MSG
            if (strPushKW[0:5].upper() == 'ECTOR'):
                intKWLength = 5
                strPush2Who = strEctorToken
                strStartInfo = '(只推Ector)\n'
                strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
            if (strPushKW[0:2].upper() == '智弘'):
                intKWLength = 2
                strPush2Who = strJohnboToken
                strStartInfo = '(只推智弘)\n'
                strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
            if (strPushKW[0:2].upper() == '冠伶'):
                intKWLength = 2
                strPush2Who = strGwenToken
                strStartInfo = '(只推冠伶)\n'
                strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
            if (strPushKW[0:2].upper() == '昆霖'):
                intKWLength = 2
                strPush2Who = strKunToken
                strStartInfo = '(只推昆霖)\n'
                strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
            if (strPushKW[0:2].upper() == '宜庭'):
                intKWLength = 2
                strPush2Who = strMichelleToken
                strStartInfo = '(只推宜庭)\n'
                strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
            if (strPushKW[0:2].upper() == '全部'):
                intKWLength = 2
                strPush2Who = 'SYS_PUSH_ALL'
                strStartInfo = '(推全部)\n'
                strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()            
        else:
            strReply_MSG = '權限不足!'
        # ***** ***** ***** ***** *****
    # ***** ***** ***** ***** *****
    
    ##### SJ樣版 #####
    elif (strEventMSG[0:2].upper() == 'SJ') and \
            ('樣版' in strEventMSG.upper()):
        get_TYPE_message = 'SJ樣版'   
    # ***** ***** ***** ***** *****


    ##### 關鍵字 #####
    elif ('最近' in strEventMSG or '最新' in strEventMSG) and \
            ('訊息' in strEventMSG or '活動' in strEventMSG or '新聞' in strEventMSG or '消息' in strEventMSG or '資訊' in strEventMSG):
        strTitle = '最近訊息/新聞(最近20筆)'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if GVstrSQL_FW_Switch == 'ON':
            ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = 'SELECT TOP (20) [SJBTCode] ,[SJBTText] ,[SJBTStatus] , CONVERT(nvarchar, [SJBTEditDate], 111) ' + \
                        ' FROM [TIM_DB].[dbo].[tbl0A_SJBT_NewsList] ' + \
                        ' WHERE [SJBTDelFlag] = 0 ' + \
                        ' ORDER BY SJBTSEQ, SJBTEditDate DESC, SJBTID '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJBTCode, SJBTText, SJBTStatus, SJBTEditDate) in resList:
                intCount += 1
                strTemp += '(' + str(intCount) + ') 案號 【' + str(SJBTCode) + '】\n' + \
                            '  更新日期：[ ' + str(SJBTEditDate) + ' ]\n' + \
                            '  ' + str(SJBTText) + '\n' + \
                            '  ' + str(SJBTStatus) + '\n\n'
            if len(strTemp)>= GVintMaxLineMSGString :
                strTemp = strTemp[0:GVintMaxLineMSGString ] + '...(資料過多)'
            strReply_MSG = strTitle + '：資料筆數[ ' + str(intCount) + ' ]\n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif ('最近' in strEventMSG or '最新' in strEventMSG) and \
            ('公告' in strEventMSG):
        strTitle = '最近公告(最近20筆)'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if GVstrSQL_FW_Switch == 'ON':
            ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = 'SELECT TOP (20) [SJBTCode] ,[SJBTText] ,[SJBTStatus] , CONVERT(nvarchar, [SJBTEditDate], 111) ' + \
                        ' FROM [TIM_DB].[dbo].[tbl0A_SJBT_NewsList] ' + \
                        ' WHERE [SJBTDelFlag] = 0 AND SJBTText LIKE \'%公告%\' ' + \
                        ' ORDER BY SJBTSEQ, SJBTEditDate DESC, SJBTID '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJBTCode, SJBTText, SJBTStatus, SJBTEditDate) in resList:
                intCount += 1
                strTemp += '(' + str(intCount) + ') 案號 【' + str(SJBTCode) + '】\n' + \
                            '  更新日期：[ ' + str(SJBTEditDate) + ' ]\n' + \
                            '  ' + str(SJBTText) + '\n' + \
                            '  ' + str(SJBTStatus) + '\n\n'
            if len(strTemp)>= GVintMaxLineMSGString :
                strTemp = strTemp[0:GVintMaxLineMSGString ] + '...(資料過多)'
            strReply_MSG = strTitle + '：資料筆數[ ' + str(intCount) + ' ]\n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif ('最近' in strEventMSG or '最新' in strEventMSG) and \
            ('參考' in strEventMSG):
        strTitle = '最近參考文件(最近20筆)'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if GVstrSQL_FW_Switch == 'ON':
            ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = 'SELECT TOP (20) [SJBTCode] ,[SJBTText] ,[SJBTStatus] , CONVERT(nvarchar, [SJBTEditDate], 111) ' + \
                        ' FROM [TIM_DB].[dbo].[tbl0A_SJBT_NewsList] ' + \
                        ' WHERE [SJBTDelFlag] = 0 AND SJBTText LIKE \'%參考%\' ' + \
                        ' ORDER BY SJBTSEQ, SJBTEditDate DESC, SJBTID '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJBTCode, SJBTText, SJBTStatus, SJBTEditDate) in resList:
                intCount += 1
                strTemp += '(' + str(intCount) + ') 案號 【' + str(SJBTCode) + '】\n' + \
                            '  更新日期：[ ' + str(SJBTEditDate) + ' ]\n' + \
                            '  ' + str(SJBTText) + '\n' + \
                            '  ' + str(SJBTStatus) + '\n\n'
            if len(strTemp)>= GVintMaxLineMSGString :
                strTemp = strTemp[0:GVintMaxLineMSGString ] + '...(資料過多)'
            strReply_MSG = strTitle + '：資料筆數[ ' + str(intCount) + ' ]\n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif ('立案' in strEventMSG or '成立' in strEventMSG):
        strReply_MSG = GVstrEstablish_Info_Text

    elif ('如何加入' in strEventMSG or '加入會員' in strEventMSG):
        strReply_MSG = GVstrHow_To_Join_Info_Text

    elif ('會址' in strEventMSG or '地址' in strEventMSG or '位置' in strEventMSG or \
             '住址' in strEventMSG or '電話' in strEventMSG) and ('在哪' in strEventMSG or '在那' in strEventMSG or \
             '聯絡' in strEventMSG):
        strReply_MSG = GVstrLocation_Phone_Info_Text

    elif (strEventMSG.count('理事長') > 0) and \
            ('誰' in strEventMSG or '名單' in strEventMSG or '清單' in strEventMSG or '列表' in strEventMSG):
        strReply_MSG = GVstrChairman_Info_Text

    elif ('總幹事' in strEventMSG) and \
            ('誰' in strEventMSG or '名單' in strEventMSG or '清單' in strEventMSG or '列表' in strEventMSG):
        strReply_MSG = GVstrDirectorGeneral_Info_Text

    elif (('統編' in strEventMSG) or ('統一編號' in strEventMSG) or ('立案' in strEventMSG)):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = GVstrUniNumber_Info_Text


    ##### 下載 #####
    elif ('LOGO' in strEventMSG.upper()):
        get_TYPE_message = 'SJ_LOGO'

    elif ('名片' in strEventMSG) and (('製作' in strEventMSG) or ('格式' in strEventMSG)):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = GVstrNameCard_Info_Config

    elif (('使用' in strEventMSG) or ('設定' in strEventMSG) or ('通話' in strEventMSG)) and ('VOWIFI' in strEventMSG) :
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = GVstrVoWiFi_Info_Config

    elif (('廠協會' in strEventMSG) or ('下載' in strEventMSG)) and ('章程' in strEventMSG):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = GVstrBylaws_DL_Info_Text


    ##### 資料庫 #####
    elif ('工業區' in strEventMSG or '會員' in strEventMSG or '廠協會' in strEventMSG) and \
            ('誰' in strEventMSG or '名單' in strEventMSG or '清單' in strEventMSG or '列表' in strEventMSG or '會員' in strEventMSG):
        strTitle = '(SJ)臺南市新吉工業區廠商協進會'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if GVstrSQL_FW_Switch == 'ON':
            ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, ' + \
                        ' SJMBPRTitle ' + \
                        ' FROM [TIM_DB].[dbo].[VIEW_0A_SJ_MemList] ' + \
                        ' ORDER BY SEQ_TYPE, SJMBCode '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, SJMBPRTitle) in resList:
                intCount += 1
                if SJMBPRType == '一般會員':
                    strTemp += '(' + str(intCount) + ') 編號【' + str(SJMBCode) + '】 \n' + \
                                '  (' + str(SJMBCorpUniNum) + ') ' + str(SJMBCorpName) + '\n' + \
                                '  ' + str(SJMBPRName) + ' ' + str(SJMBPRTitle) + '\n\n'
                else:
                    strTemp += '(' + str(intCount) + ') 編號【' + str(SJMBCode) + '】 ' + str(SJMBPRType) + '\n' + \
                                '  (' + str(SJMBCorpUniNum) + ') ' + str(SJMBCorpName) + '\n' + \
                                '  ' + str(SJMBPRName) + ' ' + str(SJMBPRTitle) + '\n\n'
            if len(strTemp) >= GVintMaxLineMSGString:
                strTemp = strTemp[0:GVintMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strTitle + '：\n資料筆數：[ ' + str(intCount) + ' ]\n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif ('理事' in strEventMSG or '監事' in strEventMSG or '理監事' in strEventMSG) and \
            ('誰' in strEventMSG or '名單' in strEventMSG or '清單' in strEventMSG or '列表' in strEventMSG):
        strTitle = '(SJ)新吉廠協會理監事名單'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if GVstrSQL_FW_Switch == 'ON':
            ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, ' + \
                        ' SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum, SJMBCorpTel, SJMBCorpProd ' + \
                        ' FROM [TIM_DB].[dbo].[VIEW_0A_SJ_LeaderList] ' + \
                        ' ORDER BY SEQ_TYPE, SJMBCode '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, \
                    SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum, SJMBCorpTel, SJMBCorpProd) in resList:
                intCount += 1
                if len(SJMBCorpProd)>= GVintMaxItemString:
                    strCorpProdText = SJMBCorpProd[0:GVintMaxItemString] + '...'
                else:
                    strCorpProdText = SJMBCorpProd
                strTemp += '(' + str(intCount) + ') ' + str(SJMBPRType) + '：' + str(SJMBPRName) + ' ' + str(SJMBPRTitle) + '\n' + \
                            '  編號 【' + str(SJMBCode) + '】' + '\n' + \
                            '  (' + str(SJMBCorpUniNum) + ') ' + str(SJMBCorpName) + '\n' + \
                            '  廠址：' + str(SJMBCorpAddress) + '\n' + \
                            '  電話：' + str(SJMBCorpTel) + '\n' + \
                            '  > 營業項目：' + str(strCorpProdText) + ' <\n\n'
            if len(strTemp) >= GVintMaxLineMSGString:
                strTemp = strTemp[0:GVintMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strTitle + '(' + str(len(strTemp)) + ')：\n' + \
                            '資料筆數：[ ' + str(intCount) + ' ] \n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif ('常用' in strEventMSG or '電話' in strEventMSG or '網址' in strEventMSG) and \
            ('名單' in strEventMSG or '清單' in strEventMSG or '列表' in strEventMSG):
        strTitle = '(SJ)常用電話網址清單'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if GVstrSQL_FW_Switch == 'ON':
            ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT SJCTType, SJCTCTMain, SJCTCTUnit, SJCTCTTel, SJCTCTWindow, ' + \
                        ' SJCTCTAddress, SJCTCTUrl ' + \
                        ' FROM [TIM_DB].[dbo].[tbl0A_SJCT_ContactTelList] ' + \
                        ' WHERE SJCTDelFlag = 0 ' + \
                        ' ORDER BY SJCTSeq '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJCTType, SJCTCTMain, SJCTCTUnit, SJCTCTTel, SJCTCTWindow, SJCTCTAddress, SJCTCTUrl) in resList:
                intCount += 1
                strTemp += '(' + str(intCount) + ') ' + str(SJCTType) + '：' + \
                            '' + str(SJCTCTMain)
                if len(str(SJCTCTUnit)) > 0:
                    strTemp += '-' + str(SJCTCTUnit)
                strTemp += '\n'

                if len(str(SJCTCTTel)) > 0:
                    strTemp += '  【電話】' + str(SJCTCTTel) + '' + '\n'
                if len(str(SJCTCTUrl)) > 0:
                    strTemp += '  【網址】' + str(SJCTCTUrl) + '' + '\n'
                if len(str(SJCTCTWindow)) > 0:
                    strTemp += '  【聯絡窗口】' + str(SJCTCTWindow) + '' + '\n'
                if len(str(SJCTCTAddress)) > 0:
                    strTemp += '  【地址】' + str(SJCTCTAddress) + '' + '\n'
                strTemp += '\n'
            if len(strTemp) >= GVintMaxLineMSGString:
                strTemp = strTemp[0:GVintMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strTitle + '(' + str(len(strTemp)) + ')：\n' + \
                            '資料筆數：[ ' + str(intCount) + ' ] \n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (strEventMSG[0:4].upper() == 'FIND') or \
            (strEventMSG[0:1].upper() == '找'):
        if (strEventMSG[0:4].upper() == 'FIND'):
            strCond = strEventMSG[-(len(strEventMSG)-4):]
        elif (strEventMSG[0:1].upper() == '找'):
            strCond = strEventMSG[-(len(strEventMSG)-1):]
        strCond=strCond.strip()

        strTitle = '(Query)查詢廠區會員/優質供應商通訊錄'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if GVstrSQL_FW_Switch == 'ON':
            ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, ' + \
                        ' SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum, SJMBCorpProd, SJMBCorpTel, ' + \
                        ' SJMBCorpSince, SJMBCorpPRName, SJMBCorpPRTitle ' + \
                        ' FROM [TIM_DB].[dbo].[VIEW_0A_SJ_MemList] ' + \
                        ' WHERE [SJMBCorpName] LIKE ' + '\'%' + strCond + '%\'' + \
                            ' OR [SJMBPRName] LIKE ' + '\'%' + strCond + '%\'' + \
                            ' OR [SJMBCorpPRName] LIKE ' + '\'%' + strCond + '%\'' + \
                            ' OR [SJMBCorpProd] LIKE ' + '\'%' + strCond + '%\'' + \
                        ' ORDER BY SEQ_TYPE, SJMBCode '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, \
                    SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum, SJMBCorpProd, SJMBCorpTel, \
                    SJMBCorpSince, SJMBCorpPRName, SJMBCorpPRTitle) in resList:
                intCount += 1
                strTemp += '(' + str(intCount) + ') 編號 【' + str(SJMBCode) + '】 ' + str(SJMBPRType) + ' (' + str(SJMBCorpEmpNum) + '人)\n' + \
                            '  (' + str(SJMBCorpUniNum) + ') ' + str(SJMBCorpName) + '\n' + \
                            '  ' + str(SJMBPRName) + ' ' + str(SJMBPRTitle) + '\n' + \
                            '  成立：' + str(SJMBCorpSince) + '\n' + \
                            '  廠址：' + str(SJMBCorpAddress) + '\n' + \
                            '  電話：' + str(SJMBCorpTel) + '\n' + \
                            '  公司負責人：' + str(SJMBCorpPRName) + ' ' + str(SJMBCorpPRTitle) + '\n' + \
                            '  > 營業項目：' + str(SJMBCorpProd) + ' <\n\n'


            ##### 外部廠商 #####
            strTemp += ' ===== 下方為外部非會員廠商 ===== \n\n '

            ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT [SJVDCode],[SJVDPRType],[SJVDCorpName],[SJVDPRName],[SJVDPRTitle], ' + \
                        ' [SJVDCorpTel],[SJVDCorpEMail],[SJVDCorpAddress],[SJVDCorpGoodText],[SJVDCorpWeb], ' + \
                        ' [SJVDCorpProd],[SJVDLastContact],[SJVDCPPT],[SJVDSVPT] ' + \
                        ' FROM [TIM_DB].[dbo].[tbl0A_SJVD_VendorList] ' + \
                        ' WHERE [SJVDCorpName] LIKE ' + '\'%' + strCond + '%\'' + \
                            ' OR [SJVDPRName] LIKE ' + '\'%' + strCond + '%\'' + \
                            ' OR [SJVDPRType] LIKE ' + '\'%' + strCond + '%\'' + \
                            ' OR [SJVDCorpProd] LIKE ' + '\'%' + strCond + '%\'' + \
                        ' ORDER BY SJVDCode '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            # strTemp=''
            for (SJVDCode, SJVDPRType, SJVDCorpName, SJVDPRName, SJVDPRTitle, \
                    SJVDCorpTel, SJVDCorpEMail, SJVDCorpAddress, SJVDCorpGoodText, SJVDCorpWeb, \
                    SJVDCorpProd,SJVDLastContact,SJVDCPPT,SJVDSVPT) in resList:
                intCount += 1
                strTemp += '(' + str(intCount) + ') 編號 【' + str(SJVDCode) + '】 ' + '\n' + \
                            '→ 類別：' + str(SJVDPRType) + '\n' + \
                            '【廠商名稱】' + str(SJVDCorpName) + '\n'
                ##### 選填項目 #####
                if (SJVDPRName is not None):
                    if len(SJVDPRName.strip()) > 0:
                        strTemp += '⊚ 廠商窗口：' + str(SJVDPRName) + '\n'
                if (SJVDCorpTel is not None):
                    if len(SJVDCorpTel.strip()) > 0:
                        strTemp += '⊚ 聯絡方式：' + str(SJVDCorpTel) + '\n'
                if (SJVDCorpAddress is not None):
                    if len(SJVDCorpAddress.strip()) > 0:
                        strTemp += '⊚ 廠商住址：' + str(SJVDCorpAddress) + '\n'
                if (SJVDCorpEMail is not None):
                    if len(SJVDCorpEMail.strip()) > 0:
                        strTemp += '⊚ 郵件：' + str(SJVDCorpEMail) + '\n'
                if (SJVDCorpWeb is not None):
                    if len(SJVDCorpWeb.strip()) > 0:
                        strTemp += '⊚ 網站：' + str(SJVDCorpWeb) + '\n'
                if (SJVDCPPT is not None):
                    if (SJVDCPPT > 0):
                        if (SJVDSVPT > 1):
                            strTemp += '⊚ 推薦評分(5分最高)：【' + str(SJVDCPPT) + '】' + '（' + str(SJVDSVPT) + '則）\n'
                        else:
                            strTemp += '⊚ 推薦評分(5分最高)：【' + str(SJVDCPPT) + '】\n'
                if (SJVDCorpGoodText is not None):
                    if len(SJVDCorpGoodText.strip()) > 0:
                        strTemp += '\n※※ 優點描述 ※※\n'
                        strTemp += str(SJVDCorpGoodText) + '\n'
                if (SJVDCorpProd is not None):
                    if len(SJVDCorpProd.strip()) > 0:
                        strTemp += '\n※※※ 實績或合作經驗 ※※※\n'
                        strTemp += str(SJVDCorpProd) + '\n'
                strTemp += '..... ..... ..... .....\n\n\n'
            ##### ##### ##### ##### #####

            if len(strTemp) >= GVintMaxLineMSGString:
                strTemp = strTemp[0:GVintMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strTitle + '：\n' + \
                            '資料筆數：[ ' + str(intCount) + ' ] \n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    ##### 內部使用 #####
    elif (strEventMSG[0:2].upper() == 'SJ') and \
            ('MEMBER' in strEventMSG.upper() or \
            'DETAIL' in strEventMSG.upper() or \
            '內用名單' in strEventMSG.upper() or \
            '詳細名單' in strEventMSG.upper()):
        strTitle = '(SJ)臺南市新吉工業區廠商協進會'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if GVstrSQL_FW_Switch == 'ON':
            ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, ' + \
                        ' SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum ' + \
                        ' FROM [TIM_DB].[dbo].[VIEW_0A_SJ_MemList] ' + \
                        ' ORDER BY SEQ_TYPE, SJMBCode '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum) in resList:
                intCount += 1
                strTemp += '(' + str(intCount) + ') 編號 【' + str(SJMBCode) + '】 ' + str(SJMBPRType) + ' (' + str(SJMBCorpEmpNum) + '人)\n' + \
                            '  (' + str(SJMBCorpUniNum) + ') ' + str(SJMBCorpName) + '\n' + \
                            '  ' + str(SJMBPRName) + ' ' + str(SJMBPRTitle) + '\n' + \
                            '  廠址：' + str(SJMBCorpAddress) + '\n\n'
            if len(strTemp) >= GVintMaxLineMSGString:
                strTemp = strTemp[0:GVintMaxLineMSGString] + '...(資料過多)'
            strContent = strTitle + '(' + str(len(strTemp)) + ')：\n' + \
                            '資料筆數：[ ' + str(intCount) + ' ] \n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
            ##### 此項需有權限才能執行 #####
            strAUTHKWQuery = 'SJDETAIL'
            strAUTH_CHK = RS_CHECK_KWAUTH_by_UserId(strLineUserID, strAUTHKWQuery)
            if strAUTH_CHK[0:2] == 'GO':
                strReply_MSG = strContent
            else:
                strReply_MSG = '權限不足!'
            # ***** ***** ***** ***** *****
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (strEventMSG[0:2].upper() == 'SJ') and \
            ('120' in strEventMSG.upper() or \
            '$' in strEventMSG.upper() or \
            'CASH' in strEventMSG.upper() or \
            '零用金' in strEventMSG.upper()):
        strTitle = '零用金使用狀況'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if GVstrSQL_FW_Switch == 'ON':
            ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT TOP (50) SJCSCode, CONVERT(nvarchar, [SJCSEditDate], 111), SJCSText, SJCSStatus, SJCSNum, ' + \
                        ' SJCSPrice, SJCSNow ' + \
                        ' FROM [TIM_DB].[dbo].[tbl0A_SJCS_CashUseList] ' + \
                        ' WHERE [SJCSDelFlag] = 0 ' + \
                        ' ORDER BY SJCSEditDate DESC, SJCSCode '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJCSCode, SJCSEditDate, SJCSText, SJCSStatus, SJCSNum, SJCSPrice, SJCSNow) in resList:
                intCount += 1
                strTemp += '(' + str(intCount) + ') 案號 【' + str(SJCSCode) + '】\n' + \
                            '  更新日期：[ ' + str(SJCSEditDate) + ' ]\n' + \
                            '  ' + str(SJCSText) + '：\n' + \
                            '  ' + str(SJCSStatus) + '：\n' + \
                            '  金額：' + str(SJCSPrice) + ' (數量：' + str(SJCSNum) + ')\n' + \
                            '  餘額可用：' + str(SJCSNow) + '\n\n'
            if len(strTemp) >= GVintMaxLineMSGString:
                strTemp = strTemp[0:GVintMaxLineMSGString] + '...(資料過多)'
            strContent = strTitle + '：資料筆數[ ' + str(intCount) + ' ]\n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
            ##### 此項需有權限才能執行 #####
            strAUTHKWQuery = 'SJCASH'
            strAUTH_CHK = RS_CHECK_KWAUTH_by_UserId(strLineUserID, strAUTHKWQuery)
            if strAUTH_CHK[0:2] == 'GO':
                strReply_MSG = strContent
            else:
                strReply_MSG = '權限不足!'
            # ***** ***** ***** ***** *****
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (strEventMSG[0:2].upper() == 'SJ') and \
            ('BANK' in strEventMSG.upper() or \
            '銀行' in strEventMSG):
        strTitle = '銀行帳戶資訊'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if GVstrSQL_FW_Switch == 'ON':
            ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT TOP (50) SJBKCode, CONVERT(nvarchar, [SJBKEditDate], 111) , SJBKText, SJBKStatus, SJBKNum, ' + \
                        ' SJBKPrice, SJBKNow ' + \
                        ' FROM [TIM_DB].[dbo].[tbl0A_SJBK_BankUseList] ' + \
                        ' WHERE [SJBKDelFlag] = 0 ' + \
                        ' ORDER BY SJBKCode DESC'
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJBKCode, SJBKEditDate, SJBKText, SJBKStatus, SJBKNum, SJBKPrice, SJBKNow) in resList:
                intCount += 1
                strTemp += '(' + str(intCount) + ') 案號 【' + str(SJBKCode) + '】\n' + \
                            '  更新日期：[ ' + str(SJBKEditDate) + ' ]\n' + \
                            '  ' + str(SJBKText) + '：\n' + \
                            '  ' + str(SJBKStatus) + '：\n' + \
                            '  金額：' + str(SJBKPrice) + ' (數量：' + str(SJBKNum) + ')\n' + \
                            '  餘額可用：' + str(SJBKNow) + '\n\n'
            if len(strTemp) >= GVintMaxLineMSGString:
                strTemp = strTemp[0:GVintMaxLineMSGString] + '...(資料過多)'
            strContent = strTitle + '：資料筆數[ ' + str(intCount) + ' ]\n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            GVstrBankAccount_Info_Text + '\n' + \
                            strTemp
            ##### 此項需有權限才能執行 #####
            strAUTHKWQuery = 'SJBANK'
            strAUTH_CHK = RS_CHECK_KWAUTH_by_UserId(strLineUserID, strAUTHKWQuery)
            if strAUTH_CHK[0:2] == 'GO':
                strReply_MSG = strContent
            else:
                strReply_MSG = '權限不足!'
            # ***** ***** ***** ***** *****
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'


    ##### 教學 #####
    elif (strEventMSG[0:2].upper() == 'SJ') and \
            ('官方帳號教學' in strEventMSG):
        strReply_MSG = GVstrLessonLearning
    # ***** ***** ***** ***** *****


    ##### (Ver)版本 #####
    elif strEventMSG.upper().count('VER') > 0:
        strReply_MSG = '『臺南市新吉工業區廠協會』版本：\n' + strVer
    # ***** ***** ***** ***** *****


    ##### 列出全部的關鍵字清單 #####
    elif (strEventMSG[0:2].upper() == 'SJ' or strEventMSG[0:4].upper() == 'TOYO') and ('!ALL' in strEventMSG):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strContent = GVstrCMKeyWord
        ##### 此項需有權限才能執行 #####
        strAUTHKWQuery = 'SJKW'
        strAUTH_CHK = RS_CHECK_KWAUTH_by_UserId(strLineUserID, strAUTHKWQuery)
        if strAUTH_CHK[0:2] == 'GO':
            strReply_MSG = strContent
        else:
            strReply_MSG = '權限不足!'
        # ***** ***** ***** ***** *****
    # ***** ***** ***** ***** *****


    ##### 修改權限 #####
    elif ('權限' in strEventMSG[0:4]) and ('修改' in strEventMSG[0:4]):
        ##### 此項需有權限才能執行 #####
        strAUTHKWQuery = 'SJPL'
        strAUTH_CHK = RS_CHECK_KWAUTH_by_UserId(strLineUserID, strAUTHKWQuery)
        if strAUTH_CHK[0:2] == 'GO':
            # RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN(strLineName, strLineUserID, strModUserDBName, strModAUTHItemName, strModYN):
            strEventMSG = RS_RIGHT_String_NotLeftStrNum(strEventMSG, 4)
            strEventMSG = strEventMSG.replace('，', ',')
            strEventMSG = strEventMSG.strip() + ',,'
            lstCond = strEventMSG.split(',')
            # strCHKUserDBName = 'ECTOR,宜庭,智弘,冠伶,昆霖,玉敏'
            # strCHKAUTHItemName = '推播,全關鍵字,銀行狀態,零用金狀態,會員詳細資料'
            strModName = lstCond[0].strip().upper()
            strModAUTH = lstCond[1].strip().upper()
            strModYN = lstCond[2].strip().upper()
            strCall = RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN(strLineDisplayName, strLineUserID, strModName, strModAUTH, strModYN)
            strReply_MSG = strCall
        else:
            strReply_MSG = '權限不足!'
        # ***** ***** ***** ***** *****
    # ***** ***** ***** ***** *****


    ##### 程式開發使用 #####
    elif (strEventMSG[0:5].upper() == 'ECTOR'):
        if len(strEventMSG) == 5:
            strCond = ''
        else:
            strCond = RS_RIGHT_String_NotLeftStrNum(strEventMSG, 5).strip()
        #比對輸入[小時分鐘](1225)
        strHHNN = RS_DateTime_2_HHNN()
        #範例：if (strHHNN in strCond) and ('KW' in strCond):

        #開發者關鍵字清單
        if ('KW' in strCond):
            get_TYPE_message = 'SYS_ADMIN_MSG'
            strContent = GVstrECKeyWord
        #官方帳號教學
        elif ('LINE' in strCond):
            get_TYPE_message = 'SYS_ADMIN_MSG'
            strContent = GVstrLessonLearning
        else:
            get_TYPE_message = 'SYS_ADMIN_MSG'
            strContent = 'EC' + strCond + '\n' * 100 + strHHNN[-2:] + 'OK'
        ##### 此項需有權限才能執行 #####
        strAUTHKWQuery = 'SYSADMIN'
        strAUTH_CHK = RS_CHECK_KWAUTH_by_UserId(strLineUserID, strAUTHKWQuery)
        if strAUTH_CHK[0:2] == 'GO':
            strReply_MSG = strContent
        else:
            strReply_MSG = '權限不足!'
        # ***** ***** ***** ***** *****


    ##### 如何使用 #####
    elif ('如何使用' in strEventMSG or 'HELP' in strEventMSG.upper() or '?' in strEventMSG.strip() or '？' in strEventMSG.strip()):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = GVstrHowToUse
    # ***** ***** ***** ***** *****

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

    else:
        get_TYPE_message = 'SYS_NOT_KW_INPUT_MSG'
        strReply_MSG = GVstrHowToUse
#        strCond = strEventMSG.strip()
#        strTitle = '(Query)關鍵字查詢'
#        if GVstrSQL_FW_Switch == 'ON':
#            ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
#            strSQL = ' SELECT SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, ' + \
#                        ' SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum, SJMBCorpProd, SJMBCorpTel, ' + \
#                        ' SJMBCorpSince, SJMBCorpPRName, SJMBCorpPRTitle ' + \
#                        ' FROM [TIM_DB].[dbo].[VIEW_0A_SJ_MemList] ' + \
#                        ' WHERE [SJMBCorpName] LIKE ' + '\'%' + strCond + '%\'' + \
#                            ' OR [SJMBPRName] LIKE ' + '\'%' + strCond + '%\'' + \
#                            ' OR [SJMBCorpPRName] LIKE ' + '\'%' + strCond + '%\'' + \
#                            ' OR [SJMBCorpProd] LIKE ' + '\'%' + strCond + '%\'' + \
#                        ' ORDER BY SEQ_TYPE, SJMBCode '
#            resList = ms.RS_SQL_ExecQuery(strSQL)
#            intCount=0
#            strTemp=''
#            for (SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, \
#                    SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum, SJMBCorpProd, SJMBCorpTel, \
#                    SJMBCorpSince, SJMBCorpPRName, SJMBCorpPRTitle) in resList:
#                intCount += 1
#                strTemp += '(' + str(intCount) + ') 編號 【' + str(SJMBCode) + '】 ' + str(SJMBPRType) + ' (' + str(SJMBCorpEmpNum) + '人)\n' + \
#                            '  (' + str(SJMBCorpUniNum) + ') ' + str(SJMBCorpName) + '\n' + \
#                            '  ' + str(SJMBPRName) + ' ' + str(SJMBPRTitle) + '\n' + \
#                            '  成立：' + str(SJMBCorpSince) + '\n' + \
#                            '  廠址：' + str(SJMBCorpAddress) + '\n' + \
#                            '  電話：' + str(SJMBCorpTel) + '\n' + \
#                            '  公司負責人：' + str(SJMBCorpPRName) + ' ' + str(SJMBCorpPRTitle) + '\n' + \
#                            '  > 營業項目：' + str(SJMBCorpProd) + ' <\n\n'
#            if len(strTemp) >= GVintMaxLineMSGString:
#                strTemp = strTemp[0:GVintMaxLineMSGString] + '...(資料過多)'
#            if intCount == 0:
#                get_TYPE_message = 'SYS_NOT_KW_INPUT_MSG'
#                strReply_MSG = GVstrHowToUse
#            else:
#                get_TYPE_message = 'SYS_KW_INPUT_MSG'
#                strReply_MSG = strTitle + '：\n' + \
#                            '資料筆數：[ ' + str(intCount) + ' ] \n' + \
#                            '查詢時間：' + FVstrNow  + '\n\n' + \
#                            strTemp
#        else:
#            get_TYPE_message = 'SYS_KW_INPUT_MSG'
#            strReply_MSG = strTitle + '：\n' + \
#                            '目前ECTOR關閉防火牆\n' + \
#                            '暫停使用..有急用可找ECTOR'


# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====

    ##### Send To Line #####
    if get_TYPE_message == 'Initial':
        reply = TextSendMessage(text=f"{strReply_MSG}")
        line_bot_api.reply_message(event.reply_token,  reply)
    # ***** ***** ***** ***** *****

    ##### LOGO #####
    elif get_TYPE_message == 'SJ_LOGO':
        # https://github.com/EctorLiu/Ector01/raw/main/img/A.jpg
        reply = ImageSendMessage(
            original_content_url='https://raw.githubusercontent.com/EctorLiu/Ector01/main/img/A.jpg',
            preview_image_url='https://raw.githubusercontent.com/EctorLiu/Ector01/main/img/A.jpg'
        )
        line_bot_api.reply_message(event.reply_token,  reply)
    # ***** ***** ***** ***** *****

    ##### 推播Line Notify內容 #####
    elif get_TYPE_message == 'SYS_ASSIGN_PUSH_MSG_Text':
        #推播訊息編輯
        push_message = '\n來自[' + strLineDisplayName + ']推播訊息：\n' + strReply_MSG
        #推播ALL or 個人
        if strPush2Who == 'SYS_PUSH_ALL':
            # EctorLiu權杖:
            token = strEctorToken
            RS_lineNotifyMessage(token, push_message)
            # 智弘權杖:
            token = strJohnboToken
            RS_lineNotifyMessage(token, push_message)
            # 冠伶權杖:
            token = strGwenToken
            RS_lineNotifyMessage(token, push_message)
            # 昆霖權杖:
            token = strKunToken
            RS_lineNotifyMessage(token, push_message)
            # 宜庭權杖:
            token = strMichelleToken
            RS_lineNotifyMessage(token, push_message)   
        else:
            # 個人:            
            token = strPush2Who
            RS_lineNotifyMessage(token, push_message)
    # ***** ***** ***** ***** *****


    ##### 推播Line Notify內容 #####
    elif get_TYPE_message == 'SYS_KW_INPUT_MSG':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        push_message = '\n來自[' + strLineDisplayName + ']輸入訊息：\n' + strEventMSG
        #推播訊息編輯
        push_message = '『KeyWord』\nDebugModeForEctor：' + push_message
        # EctorLiu權杖：
        token = strEctorToken
        RS_lineNotifyMessage(token, push_message)

        #使用者取得的訊息
        reply = TextSendMessage(text=f"{strReply_MSG}")
        line_bot_api.reply_message(event.reply_token,  reply)


    elif get_TYPE_message == 'SYS_NOT_KW_INPUT_MSG':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        push_message = '\n來自[' + strLineDisplayName + ']輸入訊息：\n' + strEventMSG
        if GVstrPush_NotKeyWord2All_Switch == 'ON': 
            # EctorLiu權杖：
            token = strEctorToken
            RS_lineNotifyMessage(token, push_message)
            # 智弘權杖：
            token = strJohnboToken
            RS_lineNotifyMessage(token, push_message)
            # 冠伶權杖：
            token = strGwenToken
            RS_lineNotifyMessage(token, push_message)
            # 昆霖權杖：
            token = strKunToken
            RS_lineNotifyMessage(token, push_message)
            # 宜庭權杖：
            token = strMichelleToken
            RS_lineNotifyMessage(token, push_message)
        else:
            #推播訊息編輯
            push_message = '『非關鍵字』\nDebugModeForEctor：' + push_message
            # EctorLiu權杖：
            token = strEctorToken
            RS_lineNotifyMessage(token, push_message)

        #使用者取得的訊息
        reply = TextSendMessage(text=f"{strReply_MSG}")
        line_bot_api.reply_message(event.reply_token,  reply)
    # ***** ***** ***** ***** *****


    elif get_TYPE_message == 'SJ樣版':
        reply = TemplateSendMessage(alt_text='樣版：需使用手機版方可顯示', \
                    template=ButtonsTemplate( \
                    title='標題：標題說明', \
                    text='樣版可以傳送文字、網址', \
                    actions=[MessageTemplateAction(label='最近活動', text='最近活動'), \
                             URITemplateAction(label='新吉工業區之動畫介紹', \
                             uri='https://www.youtube.com/watch?v=THMFMCY65co&ab_channel=%E5%8F%B0%E5%8D%97%E5%B8%82%E5%B7%A5%E5%95%86%E7%99%BC%E5%B1%95%E6%8A%95%E8%B3%87%E7%AD%96%E9%80%B2%E6%9C%83' ), \
                             PostbackTemplateAction(label='最近活動2', text='最近活動2', data='postback1') \
                    ] \
                ) \
        )
        line_bot_api.reply_message(event.reply_token, reply)

    else:
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        push_message = '\n來自[' + strLineDisplayName + ']輸入訊息：\n' + strEventMSG
        #推播訊息編輯
        push_message = '『特殊狀況』\nDebugModeForEctor：' + push_message
        # EctorLiu權杖：
        token = strEctorToken
        RS_lineNotifyMessage(token, push_message)

        #使用者取得的訊息
        reply = TextSendMessage(text=f"{strReply_MSG}")
        line_bot_api.reply_message(event.reply_token,  reply)

# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====

    # SQL_LOG紀錄
    strEventMSG = strEventMSG.replace("'", '.')
    strEventMSG = strEventMSG.replace('"', '.')
    strReply_MSG = strReply_MSG.replace("'", '.')
    strReply_MSG = strReply_MSG.replace('"', '.')
    strSQLReturn = RS_Line_LOG_ADD(strLineDisplayName, strLineUserID, strEventMSG, strReply_MSG)

# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====

