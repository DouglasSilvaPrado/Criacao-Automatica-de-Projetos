# Importando 
import pyautogui as pg

# Dados de entrada
email = input("Informe o Email do GitHub: ")
senha = input("Informe a senha do GitHub: ")
nome_repositorio = input("Qual Nome do Projeto: ").replace(" ","-")
descriçao = input("Qual Descrição do Projeto: ")
pg.PAUSE = 2.0

# Alerta inicio
pg.alert('A Automaçao começou aperte ok, e tire a mão do mouse e teclado')

# Abrindo uma nova aba
pg.press('win')
pg.write("chrome")
pg.sleep(1)
pg.press('enter')
pg.sleep(3)
pg.hotkey('alt', 'space')
pg.sleep(1)
pg.press('x')
# Digitando o link e apertando enter
pg.write('https://github.com/')
pg.sleep(1)
pg.press('enter')
pg.sleep(3)

# lougout
pg.click(x=1389, y=134)
pg.sleep(2)
pg.click(x=1276, y=605)
pg.sleep(2)

# clickando em sing in
pg.click(x=1235, y=136)
pg.sleep(2)

# logando
## email
pg.hotkey("ctrl", 'a')
pg.press('backspace')
pg.write(email)
pg.press('tab')
## senha
pg.hotkey("ctrl", 'a')
pg.press('backspace')
pg.write(senha)
## sign in
pg.click(x=709, y=458)
pg.sleep(3)

# Criando novo repositorio
pg.click(x=1326, y=135)
pg.sleep(2)
pg.click(x=1293, y=169)
pg.sleep(2)

# prenchendo campos
pg.press("tab")
pg.write(nome_repositorio)
pg.press("tab")
pg.write(descriçao)
pg.click(x=368, y=718)
pg.press("pagedown")
pg.sleep(1)
pg.click(x=446, y=689)
pg.sleep(3)

# colocando arquivos no github
pg.hotkey("win", "d")
pg.sleep(1)
## coloque a pasta dos arquivos na area de trabalho no canto superio esquerdo
pg.moveTo(x=10, y=10)
pg.mouseDown()
pg.moveTo(x=705, y=431, duration=1.5)
pg.hotkey("win", "d")
pg.mouseUp()
pg.sleep(10)
pg.press('pagedown')
pg.sleep(0.5)
pg.click(x=248, y=679)
# alerta fim do programa
pg.alert('Fim, Pode usar seu PC, Obrigado por espera.')