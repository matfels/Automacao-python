import pyautogui
import time
import pandas
#pyautogui.click -> Clica em algum lugar
#pyautogui.press -> Aperta 1 tecla
#pyautogui.write -> Escreve um texto
#pyautogui.hotkey -> Apertar uma combinação de teclas
#pyautogui.position -> Saber a posição do mouse

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no site: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# - Abrir o Chrome 
# - Digitar o Site

# Abrir navegador
pyautogui.press("win")
pyautogui.write("CHOROME")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")


# Difitar Site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(3)

pyautogui.press("enter")
time.sleep(3)


# Espera 3 segundos
time.sleep(3)


# Realizar login
pyautogui.click(x=714, y=372)
pyautogui.write("meu-mail@email.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")


# Espera 3 segundos
time.sleep(3)

# Preencher formulário

tabela = pandas.read_csv("produtos.csv")
pyautogui.click(x=680, y=259)

tabela = pandas.read_csv("produtos.csv")


for linha in tabela.index:
    pyautogui.click(x=680, y=259)

    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    
    pyautogui.press("tab")
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))


    pyautogui.press("tab")
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))

    pyautogui.press("tab")
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    
    
    pyautogui.press("tab")
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(str(obs))
    
    pyautogui.press("tab")
    pyautogui.press("enter")

#subir a tela utiliando scroll
    pyautogui.scroll(-10000)
    time.sleep(3)
    pyautogui.scroll(10000)




pyautogui.click(x=680, y=259)