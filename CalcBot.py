import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton


token = 'TOKEN' #Da cambiare

Menu=['/start','/riavvia','Anulla','Menu']

numeri=['1','2','3','4','5','6','7','8','9','0','.']
op=['/','X','-','+','=']
basi=['BASE2','BASE8','BASE10','BASE16']

valori=['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','.']

class puntatore:
    v = 2.0
    admin   = 'NOME'  #Da cambiare
    adminid =  000 #Da cambiare
    userID  = []
    userLOG = ''

calcStato       = {}
x1              = {}
x2              = {}
operatore       = {}
risultato       = {}
convStato       = {}
valore          = {}
base2           = {}
base8           = {}
base10          = {}
base16          = {}

def handle(msg):


    chatid   = msg['chat']['id']
    text     = msg['text']

    username = msg['chat']['username']
    fname    = msg['chat']['first_name']
    lang     = msg['from']['language_code']


    def ac():
        calcStato[chatid] = 'numero1'
        convStato[chatid] = ''
        x1[chatid] = ''
        x2[chatid] = ''
        operatore[chatid] = ''
        risultato[chatid] = ''

    def ac1():
        valore[chatid]  = ''
        base2[chatid]   = ''
        base8[chatid]   = ''
        base10[chatid]  = ''
        base16[chatid]  = ''

    def calcola(op):
        if op == '+':
            risultato[chatid] = str(float(x1[chatid]) + float(x2[chatid]))
        elif op == '-':
            risultato[chatid] = str(float(x1[chatid]) - float(x2[chatid]))
        elif op == '/':
            risultato[chatid] = str(float(x1[chatid]) / float(x2[chatid]))
        elif op == 'X':
            risultato[chatid] = str(float(x1[chatid]) * float(x2[chatid]))

        x1[chatid] = risultato[chatid]
        x2[chatid] = ''

    #---------------------LOG_UTENTI-----------------------------------------------
    if chatid not in puntatore.userID:
        puntatore.userID.append(chatid)
        puntatore.userLOG = puntatore.userLOG + str(chatid) + ':' + str(username) + ':' + str(fname) +  ':' + str(lang) + '\n'

    #---------------------COMANDI--------------------------------------------------
    if text in Menu:
        bot.sendMessage(chatid,'Menu',
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="Calcolatrice"),KeyboardButton(text="Convertitore")],
                    [KeyboardButton(text="Info")],
                ]))
        ac1()
        ac()

    elif text == '/ping':
        bot.sendMessage(chatid,'pong')

    elif text == 'Info':
        bot.sendMessage(chatid,'Sviluppatore: @'+puntatore.admin+'\n Versione: '+str(puntatore.v) + "\nAltri BOT:\n @ErliCarteBOT")

        if chatid == puntatore.adminid:
            bot.sendMessage(chatid,"Contatti recenti:\n" + puntatore.userLOG)

    #---------------------CONVERTITORE---------------------------------------------
    elif text == 'Convertitore':
        bot.sendMessage(chatid,'Convertitore',
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="BASE 2"),KeyboardButton(text="BASE 8")],
                    [KeyboardButton(text="BASE 10"),KeyboardButton(text="BASE 16")],
                    [KeyboardButton(text="Menu")],
                ]))
        ac1()
        ac()

    elif text == 'BASE 2':
        convStato[chatid] = 'BASE2'
        bot.sendMessage(chatid,'Base 2',
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="0"),KeyboardButton(text="1")],
                    [KeyboardButton(text="Menu"),KeyboardButton(text='Fatto')],
                ]))


    elif text == 'BASE 8':
        convStato[chatid] = 'BASE8'
        bot.sendMessage(chatid,'Base 8',
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="0"),KeyboardButton(text="1"),KeyboardButton(text="2"),KeyboardButton(text="3")],
                    [KeyboardButton(text="4"),KeyboardButton(text="5"),KeyboardButton(text="6"),KeyboardButton(text="7")],
                    [KeyboardButton(text="Menu"),KeyboardButton(text='Fatto')],
                ]))


    elif text == 'BASE 10':
        convStato[chatid] = 'BASE10'
        bot.sendMessage(chatid,'Base 10',
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="7"),KeyboardButton(text="8"),KeyboardButton(text="9")],
                    [KeyboardButton(text="4"),KeyboardButton(text="5"),KeyboardButton(text="6")],
                    [KeyboardButton(text="1"),KeyboardButton(text="2"),KeyboardButton(text="3")],
                    [KeyboardButton(text="Menu"),KeyboardButton(text="0"),KeyboardButton(text='Fatto')],
                ]))


    elif text == 'BASE 16':
        convStato[chatid] = 'BASE16'
        bot.sendMessage(chatid,'Base 16',
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="0"),KeyboardButton(text="1"),KeyboardButton(text="2"),KeyboardButton(text="3")],
                    [KeyboardButton(text="4"),KeyboardButton(text="5"),KeyboardButton(text="6"),KeyboardButton(text="7")],
                    [KeyboardButton(text="8"),KeyboardButton(text="9"),KeyboardButton(text="A"),KeyboardButton(text="B")],
                    [KeyboardButton(text="C"),KeyboardButton(text="D"),KeyboardButton(text="E"),KeyboardButton(text="F")],
                    [KeyboardButton(text="Menu"),KeyboardButton(text='Fatto')],
                ]))

    elif text in valori and convStato[chatid] in basi:
        if convStato[chatid] == 'BASE2':
            base2[chatid] = base2[chatid] + text
        elif convStato[chatid] == 'BASE8':
            base8[chatid] = base8[chatid] + text
        elif convStato[chatid] == 'BASE10':
            base10[chatid] = base10[chatid] + text
        elif convStato[chatid] == 'BASE16':
            base16[chatid] = base16[chatid] + text

    elif text  == 'Fatto':
        if convStato[chatid] == 'BASE2':
            base10[chatid] = int(base2[chatid],base=2)
            base8[chatid] = oct(int(base10[chatid]))
            base16[chatid] = hex(int(base10[chatid]))
        elif convStato[chatid] == 'BASE8':
            base10[chatid] = int(base8[chatid],base=8)
            base2[chatid] = bin(int(base10[chatid]))
            base16[chatid] = hex(int(base10[chatid]))
        elif convStato[chatid] == 'BASE10':
            base2[chatid] = bin(int(base10[chatid]))
            base8[chatid] = oct(int(base10[chatid]))
            base16[chatid] = hex(int(base10[chatid]))
        elif convStato[chatid] == 'BASE16':
            base10[chatid] = int(base16[chatid],base=16)
            base2[chatid] = bin(int(base10[chatid]))
            base8[chatid] = oct(int(base10[chatid]))
        else:
            bot.sendMessage(chatid,'Errore')

        base8[chatid]   =       base8[chatid].replace('0o','')
        base16[chatid]  =       base16[chatid].replace('0x','')
        base2[chatid]   =       base2[chatid].replace('0b','')
        bot.sendMessage(chatid,'Base 2: '+base2[chatid]+
            '\n Base 8: '+str(base8[chatid])+
            '\n Base 10: '+str(base10[chatid])+
            '\n Base 16: '+str(base16[chatid]))
        ac1()
    #---------------------CALCOLATRICE---------------------------------------------
    elif text == 'Calcolatrice':
        bot.sendMessage(chatid,'Calcolatrice',
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="7"),KeyboardButton(text="8"),KeyboardButton(text="9"),KeyboardButton(text="/")],
                    [KeyboardButton(text="4"),KeyboardButton(text="5"),KeyboardButton(text="6"),KeyboardButton(text="X")],
                    [KeyboardButton(text="1"),KeyboardButton(text="2"),KeyboardButton(text="3"),KeyboardButton(text="-")],
                    [KeyboardButton(text="AC"),KeyboardButton(text="0"),KeyboardButton(text="."),KeyboardButton(text="+")],
                    [KeyboardButton(text="Menu"),KeyboardButton(text="=")],
                ]))
        ac()

    elif text in numeri and convStato[chatid] != basi:
        if calcStato[chatid] == 'numero1':
            x1[chatid] = x1[chatid]+text
        elif calcStato[chatid] == 'numero2':
            x2[chatid] = x2[chatid]+text

    elif text in op:
        if calcStato[chatid] == 'numero1':
            calcStato[chatid] = 'numero2'
            operatore[chatid] = text
        elif calcStato[chatid] == 'numero2':
            try:
                if operatore[chatid] == '+':
                    calcola('+')
                elif operatore[chatid] == '-':
                    calcola('-')
                elif operatore[chatid] == '/':
                    calcola('/')
                elif operatore[chatid] == 'X':
                    calcola('X')
                operatore[chatid] = text
                if text == '=':
                    bot.sendMessage(chatid,risultato[chatid])
            except:
                bot.sendMessage(chatid,'Errore')
                ac()



    elif text == 'AC':
        ac()
        bot.sendMessage(chatid,'Pulito')

#----------------------------------------------------------------------------

bot = telepot.Bot(token)

bot.message_loop(handle)

bot.sendMessage(puntatore.adminid,'Bot acceso')

print("Avviso: bot acceso")

while True:
    time.sleep(3600)
