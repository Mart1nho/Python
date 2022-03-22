import telebot

CHAVE_API = "5124527966:AAFe-JyTwHrOhfUrYrSSvBfQ5Af3tc3hpLI"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
Adicione o link abaixo em seu Aplicativo de IPTV.
http://bit.ly/PlutoTvBR"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """
Adicione o link abaixo em seu Aplicativo de IPTV.
https://i.mjh.nz/PlutoTV/br.m3u8
"""

    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    texto = """
Para acessar o Grupo Pluto TV Fâ Clube no Facebook.
Acesse: https://www.facebook.com/groups/plutotvbrasilfaclube
"""

    bot.send_message(mensagem.chat.id, texto)



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """

Clique em uma das opções abaixo para continuar:
/opcao1 Lista IPTV com canais da Pluto TV de todo mundo
/opcao2 Lista IPTV com canais da Pluto TV Brasil
/opcao3 Grupo Pluto TV Fã Clube no Facebook"""
    bot.reply_to(mensagem, texto)

bot.polling()