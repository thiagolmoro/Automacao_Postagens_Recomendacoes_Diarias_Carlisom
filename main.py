# Instalar as Bibliotecas que serão utilizados
# Usar no Terminal o Comando no CMD:
# pip install pyautogui pyperclip pyscreenshot pillow

# importar os pacotes que serão utilizados
import pyautogui as pa # importa o pacote pyautogui e dá o apelido de pa
import time # importa o pacote time
import pyperclip # importa o pacote pyperclip
import pyscreenshot # importa o pacote pyscreenshot
from PIL import Image # USADO PARA TRABALHAR COM A IMAGEM
from PIL import ImageDraw # USADO PARA DESENHAR ALGO EM CIMA DA IMAGEM
from PIL import ImageFont # USADA PARA ESPECIFICAR QUAL FONTE SERÁ USADA NO TEXTO

Qualidade_Estatistica = "https://tradergrafico.com.br/Robos/?R=3&T=A"
Menos_Investimento = "https://tradergrafico.com.br/Robos/?R=3&T=B"
Maior_Retorno = "https://tradergrafico.com.br/Robos/?R=3&T=C"

pa.PAUSE = 0.5 # Comando para daixar o código rodar mais lento em 0.5 segundos

dia = "27"
mes = "10"
ano = "2023"

end_facebook = "https://business.facebook.com/creatorstudio/home"
end_twitter = "https://twitter.com/home"
end_telegram = "https://t.me/tradergrafico"


for cont in range (0, 6): # cont vai de 0 a 5, com passo 1
    pa.hotkey("win", "1") # Aperta a combinação de tecla Windows + 1
    time.sleep(10) # Faz o código aguardar 10 segundos antes de executar o próximo comando
    pa.hotkey("ctrl", "l") # Aperta a combinação de tecla Ctrl+l

    if cont <= 1:
        pyperclip.copy(Qualidade_Estatistica) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
    elif cont > 1 and cont <= 3:
        pyperclip.copy(Menos_Investimento) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
    else:
        pyperclip.copy(Maior_Retorno) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç

    pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver
    pa.press("enter") # Aperta a tecla Enter
    time.sleep(15) # Faz o código aguardar 15 segundos antes de executar o próximo comando
    pa.click(x=1838, y=485)
    pa.click(x=393, y=298)
    pa.scroll(-1100) # dá um Scroll na tela para baixo

    if cont == 0 or cont == 2 or cont == 4:
        pa.click(x=612, y=552)
    else:
        pa.click(x=1259, y=554)

    time.sleep(25) # Faz o código aguardar 25 segundos antes de executar o próximo comando

    # Salvar o número da carteira
    pa.doubleClick(x=1025, y=300)
    pa.rightClick(x=1025, y=300)
    pa.press("down")
    pa.press("enter")
    numero_carteira = pyperclip.paste()

    # Salvar o Link da carteira na variável
    pa.rightClick(x=734, y=856)
    pa.press("down")
    pa.press("down")
    pa.press("down")
    pa.press("down")
    pa.press("down")
    pa.press("enter")
    link_carteira = pyperclip.paste()

    # Salva o Valor da Carteira
    pa.scroll(-800) # dá um Scroll na tela para baixo

    if cont == 0 or cont == 2 or cont == 4:
        pa.doubleClick(x=410, y=659)
        pa.rightClick(x=410, y=659)
        pa.press("down")
        pa.press("enter")
        valor_carteira = pyperclip.paste()

        # Salva o valor de retorno da Carteira
        pa.doubleClick(x=742, y=893)
        pa.rightClick(x=742, y=893)
        pa.press("down")
        pa.press("enter")
        valor_retorno_carteira = pyperclip.paste()
    else:
        pa.doubleClick(x=406, y=640)
        pa.rightClick(x=406, y=640)
        # pa.doubleClick(x=416, y=688)
        # pa.rightClick(x=416, y=688)
        pa.press("down")
        pa.press("enter")
        valor_carteira = pyperclip.paste()

        # Salva o valor de retorno da Carteira
        pa.doubleClick(x=742, y=874)
        pa.rightClick(x=742, y=874)
        # pa.doubleClick(x=745, y=924)
        # pa.rightClick(x=745, y=924)
        pa.press("down")
        pa.press("enter")
        valor_retorno_carteira = pyperclip.paste()


    # Salva a imagem do gráfico de desempenho dessa carteira
    pa.scroll(2200) # dá um Scroll na tela para cima
    pa.scroll(-2200) # dá um Scroll na tela para baixo

    if cont == 0 or cont == 2 or cont == 4:
        pa.click(x=325, y=474)
        image_auto_bot = pyscreenshot.grab(bbox=(325, 474, 1143, 909)) # faz a captura da tela com os parametros locais indicados, sendo x1, y1, x2 e y2
        image_auto_bot.save("D:/Google Drive - Trader/0 - Indicações diárias do Carlisom para postar/Postagens do Dia/TG - "+numero_carteira+".png") # salva a imagem capturada e salva nesse caminho com o nome TG - Numero_carteira.png
        # Criar as palavars que serão colocadas sobre a imagem
        texto = "Retorno Médio Mensal:"
        # Abrir a imagem
        imagem = Image.open("D:/Google Drive - Trader/0 - Indicações diárias do Carlisom para postar/Postagens do Dia/TG - "+numero_carteira+".png")
        # Abrir a imagem para fazer a sobreposição
        draw = ImageDraw.Draw(imagem)
        # Selecionar qual fonte irei usar
        fonte_texto = ImageFont.truetype('C:/Users/thiag/AppData/Local/Microsoft/Windows/Fonts/MontserratAlternates-BlackItalic.TTF',31)
        fonte_valor_retorno = ImageFont.truetype('C:/Users/thiag/AppData/Local/Microsoft/Windows/Fonts/MontserratAlternates-BlackItalic.TTF',35)

        # sobrepor (escrever por cima) da imagem algum texto
        draw.text((200,75),texto,font=fonte_texto,fill=(9, 150, 9)) # VERDE
        draw.text((200,115),"R$ "+valor_retorno_carteira,font=fonte_valor_retorno,fill=(9, 150, 9)) # VERDE

        # draw.text((200,75),texto,font=fonte,fill=(0, 0, 0)) # PRETO
        # draw.text((200,115),"R$ "+valor_retorno_carteira,font=fonte,fill=(0, 0, 0)) # PRETO

        # draw.text((200,75),texto,font=fonte,fill=(10, 4, 191)) # AZUL
        # draw.text((200,115),"R$ "+valor_retorno_carteira,font=fonte,fill=(10, 4, 191)) # AZUL

        # draw.text((200,75),texto,font=fonte,fill=(88, 8, 199)) # ROXO
        # draw.text((200,115),"R$ "+valor_retorno_carteira,font=fonte,fill=(88, 8, 199)) # ROXO

        # draw.text((200,75),texto,font=fonte,fill=(227, 114, 9)) # LARANJA
        # draw.text((200,115),"R$ "+valor_retorno_carteira,font=fonte,fill=(227, 114, 9)) # LARANJA

        # draw.text((200,75),texto,font=fonte,fill=(212, 6, 13)) # VERMELHO
        # draw.text((200,115),"R$ "+valor_retorno_carteira,font=fonte,fill=(212, 6, 13)) # VERMELHO

        # salvar a nova imagem
        imagem.save(f'D:/Google Drive - Trader/0 - Indicações diárias do Carlisom para postar/Postagens do Dia/TG - '+numero_carteira+'.png')
    else:
        pa.click(x=325, y=455)
        #  pa.click(x=325, y=530)
        image_auto_bot = pyscreenshot.grab(bbox=(325, 455, 1143, 890)) # faz a captura da tela com os parametros locais indicados, sendo x1, y1, x2 e y2
        # image_auto_bot = pyscreenshot.grab(bbox=(325, 530, 1143, 965)) # faz a captura da tela com os parametros locais indicados, sendo x1, y1, x2 e y2
        image_auto_bot.save("D:/Google Drive - Trader/0 - Indicações diárias do Carlisom para postar/Postagens do Dia/TH - "+numero_carteira+".png") # salva a imagem capturada e salva nesse caminho com o nome TH - Numero_carteira.png
        # Criar as palavars que serão colocadas sobre a imagem
        texto = "Retorno Médio Mensal:"
        # Abrir a imagem
        imagem = Image.open("D:/Google Drive - Trader/0 - Indicações diárias do Carlisom para postar/Postagens do Dia/TH - "+numero_carteira+".png")
        # Abrir a imagem para fazer a sobreposição
        draw = ImageDraw.Draw(imagem)
        # Selecionar qual fonte irei usar
        fonte_texto = ImageFont.truetype('C:/Users/thiag/AppData/Local/Microsoft/Windows/Fonts/MontserratAlternates-BlackItalic.TTF',31)
        fonte_valor_retorno = ImageFont.truetype('C:/Users/thiag/AppData/Local/Microsoft/Windows/Fonts/MontserratAlternates-BlackItalic.TTF',35)

        # sobrepor (escrever por cima) da imagem algum texto
        draw.text((200,75),texto,font=fonte_texto,fill=(9, 150, 9)) # VERDE
        draw.text((200,115),"R$ "+valor_retorno_carteira,font=fonte_valor_retorno,fill=(9, 150, 9)) # VERDE

        # draw.text((200,75),texto,font=fonte,fill=(0, 0, 0)) # PRETO
        # draw.text((200,115),"R$ "+valor_retorno_carteira,font=fonte,fill=(0, 0, 0)) # PRETO

        # draw.text((200,75),texto,font=fonte,fill=(10, 4, 191)) # AZUL
        # draw.text((200,115),"R$ "+valor_retorno_carteira,font=fonte,fill=(10, 4, 191)) # AZUL

        # draw.text((200,75),texto,font=fonte,fill=(88, 8, 199)) # ROXO
        # draw.text((200,115),"R$ "+valor_retorno_carteira,font=fonte,fill=(88, 8, 199)) # ROXO

        # draw.text((200,75),texto,font=fonte,fill=(227, 114, 9)) # LARANJA
        # draw.text((200,115),"R$ "+valor_retorno_carteira,font=fonte,fill=(227, 114, 9)) # LARANJA

        # draw.text((200,75),texto,font=fonte,fill=(212, 6, 13)) # VERMELHO
        # draw.text((200,115),"R$ "+valor_retorno_carteira,font=fonte,fill=(212, 6, 13)) # VERMELHO

        # salvar a nova imagem
        imagem.save(f'D:/Google Drive - Trader/0 - Indicações diárias do Carlisom para postar/Postagens do Dia/TH - '+numero_carteira+'.png')


    time.sleep(15) # Faz o código aguardar 15 segundos antes de executar o próximo comando
    pa.hotkey("alt", "f4") # Aperta a combinação de tecla Alt + f4 para fechar a janela


    # POSTAR NO FACEBOOK E INSTAGRAM
    pa.hotkey("win", "2") # Aperta a combinação de tecla Windows + 2
    time.sleep(15) # Faz o código aguardar 10 segundos antes de executar o próximo comando
    pa.hotkey("ctrl", "l") # Aperta a combinação de tecla Ctrl+l
    time.sleep(5) # Faz o código aguardar 5 segundos antes de executar o próximo comando
    pyperclip.copy(end_facebook) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
    pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver
    pa.press("enter") # Aperta a tecla Enter
    time.sleep(10) # Faz o código aguardar 10 segundos antes de executar o próximo comando
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("enter") # Aperta a tecla Enter
    time.sleep(10) # Faz o código aguardar 10 segundos antes de executar o próximo comando

    # pa.click(x=303, y=147)
    # pa.press("tab") # Aperta a tecla tab
    # pa.press("down") # Aperta a tecla para baixo
    # pa.press("down") # Aperta a tecla para baixo
    # pa.press("space") # Aperta a tecla espaço
    pa.click(x=303, y=147)

    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("enter") # Aperta a tecla Enter
    pa.press("enter") # Aperta a tecla Enter
    time.sleep(5) # Faz o código aguardar 3 segundos antes de executar o próximo comando

    if cont == 0:
        pa.hotkey("ctrl", "l") # Aperta a combinação de tecla Ctrl+l
        time.sleep(5) # Faz o código aguardar 3 segundos antes de executar o próximo comando
        caminho = "D:/Google Drive - Trader/0 - Indicações diárias do Carlisom para postar/Postagens do Dia"
        pyperclip.copy(caminho) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
        pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver
        time.sleep(5) # Faz o código aguardar 5 segundos antes de executar o próximo comando
        pa.press("enter") # Aperta a tecla Enter
        pa.press("tab") # Aperta a tecla tab
        pa.press("tab") # Aperta a tecla tab
        pa.press("tab") # Aperta a tecla tab
        pa.press("tab") # Aperta a tecla tab
        pa.press("tab") # Aperta a tecla tab

    if cont == 0 or cont == 2 or cont == 4:
        pa.write("TG - "+numero_carteira+".png")
    else:
        pa.write("TH - "+numero_carteira+".png")
    time.sleep(2) # Faz o código aguardar 2 segundos antes de executar o próximo comando
    pa.press("enter") # Aperta a tecla Enter

    time.sleep(4) # Faz o código aguardar 2 segundos antes de executar o próximo comando

    # TEXTO PARA O FACEBOOK
    pa.press("tab") # Aperta a tecla tab
    pa.press("space") # Aperta a tecla espaço
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab

    if cont == 0 or cont == 2 or cont == 4:
        texto_facebook = "🚀 Acesse agora uma das carteiras indicada pelo Carlisom, nossa Inteligência Artificial, para operar hoje, dia "+dia+"/"+mes+"/"+ano+", no TG À La Carte e Combo AutoBot até R$ 40 mil. 📈\n\n🤑 Lucro Médio Mensal: R$ "+valor_retorno_carteira+"/mês\n\n💰 Investimento Inicial (fica na sua conta): R$ "+valor_carteira+"\n\nPlanos de Robôs dessa Carteira: Top Hedger / 40k / 10k 🤖💡\n\n"+link_carteira+"\n\nNão fique de fora! Seu sucesso é a nossa maior recompensa. Vem conosco e faça parte dessa revolução! 🌟\n\nAcesse www.tradergrafico.com.br e saiba mais! 📌\n\n⚠ Lembre-se que retornos passados não são garantia de retorno futuro. Investimentos em renda variável envolvem riscos e podem ensejar perdas, inclusive da totalidade do capital investido. ⚠\n\n#b3 #tgautobot #dinheiro #robos #bolsadevalores #sucesso #daytrader #daytrade #cm #mercadofinanceiro #bmf #investimentos #traderlife #bovespa #tophedger #vidadetrader #trader #brasil #daytrading #trading #investidores #tradergrafico #miniindice #daytraderlife #money #traderlifestyle #traderbrasil #riqueza #dolar #investimento 🚀🔝"
    else:
        texto_facebook = "🚀 Acesse agora uma das carteiras indicada pelo Carlisom, nossa Inteligência Artificial, para operar hoje, dia "+dia+"/"+mes+"/"+ano+", no Top Hedger. 📈\n\n🤑 Lucro Médio Mensal: R$ "+valor_retorno_carteira+"/mês\n\n💰 Investimento Inicial (fica na sua conta): R$ "+valor_carteira+"\n\nPlano de Robôs dessa Carteira: Top Hedger 🤖💡\n\n"+link_carteira+"\n\nNão fique de fora! Seu sucesso é a nossa maior recompensa. Vem conosco e faça parte dessa revolução! 🌟\n\nAcesse www.tradergrafico.com.br e saiba mais! 📌\n\n⚠ Lembre-se que retornos passados não são garantia de retorno futuro. Investimentos em renda variável envolvem riscos e podem ensejar perdas, inclusive da totalidade do capital investido. ⚠\n\n#b3 #thautobot #dinheiro #robos #bolsadevalores #sucesso #daytrader #daytrade #cm #mercadofinanceiro #bmf #investimentos #traderlife #bovespa #tophedger #vidadetrader #trader #brasil #daytrading #trading #investidores #tradergrafico #miniindice #daytraderlife #money #traderlifestyle #traderbrasil #riqueza #dolar #investimento 🚀🔝"

    pyperclip.copy(texto_facebook) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
    pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver

    time.sleep(2) # Faz o código aguardar 2 segundos antes de executar o próximo comando

    #TEXTO PARA O INSTAGRAM
    pa.hotkey("shift", "tab") # Aperta a combinação de tecla Shift + Tab
    pa.press("right") # Aperta a tecla para direita
    pa.press("enter") # Aperta a tecla Enter
    pa.press("tab") # Aperta a tecla tab

    if cont == 0 or cont == 2 or cont == 4:
        texto_instagram = "🚀 Acesse agora uma das carteiras indicada pelo Carlisom, nossa Inteligência Artificial, para operar hoje, dia "+dia+"/"+mes+"/"+ano+", no TG À La Carte e Combo AutoBot até R$ 40 mil. 📈\n\n🤑 Lucro Médio Mensal: R$ "+valor_retorno_carteira+"/mês\n\n💰 Investimento Inicial (fica na sua conta): R$ "+valor_carteira+"\n\nPlanos de Robôs dessa Carteira: Top Hedger / 40k / 10k 🤖💡\n\n"+link_carteira+"\n\nNão fique de fora! Seu sucesso é a nossa maior recompensa. Vem conosco e faça parte dessa revolução! 🌟\n\nClique no link na bio e saiba mais! 📌\n\n⚠ Lembre-se que retornos passados não são garantia de retorno futuro. Investimentos em renda variável envolvem riscos e podem ensejar perdas, inclusive da totalidade do capital investido. ⚠\n\n#b3 #tgautobot #dinheiro #robos #bolsadevalores #sucesso #daytrader #daytrade #cm #mercadofinanceiro #bmf #investimentos #traderlife #bovespa #tophedger #vidadetrader #trader #brasil #daytrading #trading #investidores #tradergrafico #miniindice #daytraderlife #money #traderlifestyle #traderbrasil #riqueza #dolar #investimento 🚀🔝"
    else:
        texto_instagram = "🚀 Acesse agora uma das carteiras indicada pelo Carlisom, nossa Inteligência Artificial, para operar hoje, dia "+dia+"/"+mes+"/"+ano+", no Top Hedger. 📈\n\n🤑 Lucro Médio Mensal: R$ "+valor_retorno_carteira+"/mês\n\n💰 Investimento Inicial (fica na sua conta): R$ "+valor_carteira+"\n\nPlano de Robôs dessa Carteira: Top Hedger 🤖💡\n\n"+link_carteira+"\n\nNão fique de fora! Seu sucesso é a nossa maior recompensa. Vem conosco e faça parte dessa revolução! 🌟\n\nClique no link na bio e saiba mais! 📌\n\n⚠ Lembre-se que retornos passados não são garantia de retorno futuro. Investimentos em renda variável envolvem riscos e podem ensejar perdas, inclusive da totalidade do capital investido. ⚠\n\n#b3 #thautobot #dinheiro #robos #bolsadevalores #sucesso #daytrader #daytrade #cm #mercadofinanceiro #bmf #investimentos #traderlife #bovespa #tophedger #vidadetrader #trader #brasil #daytrading #trading #investidores #tradergrafico #miniindice #daytraderlife #money #traderlifestyle #traderbrasil #riqueza #dolar #investimento 🚀🔝"

    pyperclip.copy(texto_instagram) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
    pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver


    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab

    # PARA POSTAR NO INSTRAGRAM, RETIRAR OS TABS ABAIXO
    # pa.press("tab") # Aperta a tecla tab
    # pa.press("tab") # Aperta a tecla tab
    # pa.press("tab") # Aperta a tecla tab
    # pa.press("tab") # Aperta a tecla tab

    pa.press("enter") # Aperta a tecla Enter

    time.sleep(15) # Faz o código aguardar 15 segundos antes de executar o próximo comando


    # POSTAR NO TWITTER
    # pa.hotkey("ctrl", "t") # Aperta a combinação de tecla Ctrl+t para abrir uma nova guia no navegador
    pa.hotkey("ctrl", "l") # Aperta a combinação de tecla Ctrl+l
    time.sleep(2) # Faz o código aguardar 5 segundos antes de executar o próximo comando
    pyperclip.copy(end_twitter) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
    pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver
    time.sleep(2) # Faz o código aguardar 2 segundos antes de executar o próximo comando
    pa.press("enter") # Aperta a tecla Enter
    time.sleep(15) # Faz o código aguardar 5 segundos antes de executar o próximo comando

    pa.click(x=730, y=248)

    if cont == 0 or cont == 2 or cont == 4:
        texto_twitter = "Indicação do Carlisom para hoje!\n\nLucro Médio: R$ "+valor_retorno_carteira+"/mês\nInv. Inicial: R$ "+valor_carteira+"\nPlanos: TH / 40k / 10k\n\n"+link_carteira+"\n\nRetornos passados não são garantia de retorno futuro. Investimentos em renda variável envolvem riscos e podem ensejar perdas, até mesmo Total."
    else:
        texto_twitter = "Indicação do Carlisom para hoje!\n\nLucro Médio: R$ "+valor_retorno_carteira+"/mês\nInv. Inicial: R$ "+valor_carteira+"\nPlano: Top Hedger\n\n"+link_carteira+"\n\nRetornos passados não são garantia de retorno futuro. Investimentos em renda variável envolvem riscos e podem ensejar perdas, até mesmo Total."

    pyperclip.copy(texto_twitter) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
    pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver

    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("enter") # Aperta a tecla Enter
    time.sleep(3) # Faz o código aguardar 3 segundos antes de executar o próximo comando

    if cont == 0:
        pa.hotkey("ctrl", "l") # Aperta a combinação de tecla Ctrl+l
        time.sleep(3) # Faz o código aguardar 3 segundos antes de executar o próximo comando
        pyperclip.copy(caminho) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
        pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver

        time.sleep(5) # Faz o código aguardar 5 segundos antes de executar o próximo comando
        pa.press("enter") # Aperta a tecla Enter
        pa.press("tab") # Aperta a tecla tab
        pa.press("tab") # Aperta a tecla tab
        pa.press("tab") # Aperta a tecla tab
        pa.press("tab") # Aperta a tecla tab
        pa.press("tab") # Aperta a tecla tab

    if cont == 0 or cont == 2 or cont == 4:
        pa.write("TG - "+numero_carteira+".png")
    else:
        pa.write("TH - "+numero_carteira+".png")
    time.sleep(2) # Faz o código aguardar 2 segundos antes de executar o próximo comando
    pa.press("enter") # Aperta a tecla Enter

    time.sleep(2) # Faz o código aguardar 2 segundos antes de executar o próximo comando

    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("tab") # Aperta a tecla tab
    pa.press("enter") # Aperta a tecla Enter

    time.sleep(10) # Faz o código aguardar 10 segundos antes de executar o próximo comando

    pa.hotkey("alt", "f4") # Aperta a combinação de tecla Alt + f4 para fechar a janela


    # # POSTAR NO TELEGRAM
    # pa.hotkey("win", "2") # Aperta a combinação de tecla Windows + 2
    # time.sleep(5) # Faz o código aguardar 5 segundos antes de executar o próximo comando
    # pa.hotkey("ctrl", "l") # Aperta a combinação de tecla Ctrl+l
    # time.sleep(5) # Faz o código aguardar 5 segundos antes de executar o próximo comando
    # pyperclip.copy(end_telegram) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
    # pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver
    # pa.press("enter") # Aperta a tecla Enter
    # time.sleep(15) # Faz o código aguardar 15 segundos antes de executar o próximo comando

    # pa.click(x=709, y=1012)

    # if cont == 0:
    #     pa.hotkey("ctrl", "l") # Aperta a combinação de tecla Ctrl+l
    #     time.sleep(6) # Faz o código aguardar 6 segundos antes de executar o próximo comando
    #     caminho = "D:/Google Drive - Trader/0 - Indicações diárias do Carlisom para postar/Postagens do Dia"
    #     pyperclip.copy(caminho) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
    #     pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver
    #     time.sleep(6) # Faz o código aguardar 6 segundos antes de executar o próximo comando
    #     pa.press("enter") # Aperta a tecla Enter
    #     pa.press("tab") # Aperta a tecla tab
    #     pa.press("tab") # Aperta a tecla tab
    #     pa.press("tab") # Aperta a tecla tab
    #     pa.press("tab") # Aperta a tecla tab
    #     pa.press("tab") # Aperta a tecla tab

    # if cont == 0 or cont == 2 or cont == 4:
    #     pa.write("TG - "+numero_carteira+".png")
    # else:
    #     pa.write("TH - "+numero_carteira+".png")
    # time.sleep(3) # Faz o código aguardar 3 segundos antes de executar o próximo comando
    # pa.press("enter") # Aperta a tecla Enter

    # time.sleep(3) # Faz o código aguardar 3 segundos antes de executar o próximo comando

    # pa.press("tab") # Aperta a tecla tab
    # pa.press("tab") # Aperta a tecla tab

    # if cont == 0 or cont == 2 or cont == 4:
    #     texto_telegram = "🚀 Acesse agora uma das carteiras indicada pelo Carlisom, nossa Inteligência Artificial, para operar hoje, dia "+dia+"/"+mes+"/"+ano+", no TG À La Carte e Combo AutoBot até R$ 40 mil. 📈\n\n🤑 Lucro Médio Mensal: R$ "+valor_retorno_carteira+"/mês\n\n💰 Investimento Inicial (fica na sua conta): R$ "+valor_carteira+"\n\nPlanos de Robôs dessa Carteira: Top Hedger / 40k / 10k 🤖💡\n\n"+link_carteira+"\n\nNão fique de fora! Seu sucesso é a nossa maior recompensa. Vem conosco e faça parte dessa revolução! 🌟\n\nAcesse www.tradergrafico.com.br e saiba mais! 📌\n\n⚠ Lembre-se que retornos passados não são garantia de retorno futuro. Investimentos em renda variável envolvem riscos e podem ensejar perdas, inclusive da totalidade do capital investido. ⚠\n\n#b3 #tgautobot #dinheiro #robos #bolsadevalores #sucesso #daytrader #daytrade #cm #mercadofinanceiro #bmf #investimentos #traderlife #bovespa #tophedger #vidadetrader #trader #daytrading #trading #investidores #tradergrafico #miniindice #daytraderlife 🚀🔝"
    # else:
    #     texto_telegram = "🚀 Acesse agora uma das carteiras indicada pelo Carlisom, nossa Inteligência Artificial, para operar hoje, dia "+dia+"/"+mes+"/"+ano+", no Top Hedger. 📈\n\n🤑 Lucro Médio Mensal: R$ "+valor_retorno_carteira+"/mês\n\n💰 Investimento Inicial (fica na sua conta): R$ "+valor_carteira+"\n\nPlano de Robôs dessa Carteira: Top Hedger 🤖💡\n\n"+link_carteira+"\n\nNão fique de fora! Seu sucesso é a nossa maior recompensa. Vem conosco e faça parte dessa revolução! 🌟\n\nAcesse www.tradergrafico.com.br e saiba mais! 📌\n\n⚠ Lembre-se que retornos passados não são garantia de retorno futuro. Investimentos em renda variável envolvem riscos e podem ensejar perdas, inclusive da totalidade do capital investido. ⚠\n\n#b3 #thautobot #dinheiro #robos #bolsadevalores #sucesso #daytrader #daytrade #cm #mercadofinanceiro #bmf #investimentos #traderlife #bovespa #tophedger #vidadetrader #trader #daytrading #trading #investidores #tradergrafico #miniindice #daytraderlife 🚀🔝"

    # pyperclip.copy(texto_telegram) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
    # pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver
    # time.sleep(2) # Faz o código aguardar 2 segundos antes de executar o próximo comando
    # pa.press("enter") # Aperta a tecla Enter

    # time.sleep(5) # Faz o código aguardar 5 segundos antes de executar o próximo comando
    # pa.hotkey("win", "2") # Aperta a combinação de tecla Windows + 2
    # time.sleep(4) # Faz o código aguardar 4 segundos antes de executar o próximo comando
    # pa.hotkey("alt", "f4") # Aperta a combinação de tecla Alt + f4 para fechar a janela