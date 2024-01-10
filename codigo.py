# passo a passo
# passo 1 - entrar no sistema da hashtag
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip install pyautogui
import pyautogui
import time
# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey("ctrl" + "C"), serve como um atalho
# para deixar mais lento -> pyautogui.PAUSE = (quantidade de segundos que você quer que rode o comando)
pyautogui.PAUSE = 0.5

# apertar a tecla do windows
pyautogui.press("win")
# digitar o nome do programa(chrome)
pyautogui.write("chrome")
# apertar enter
pyautogui.press("enter")

# digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
# apertar enter
pyautogui.press("enter")
# o time é um comando para fazer com que seu comando espere algum tempo para executar a próxima tarefa
time.sleep(1)
pyautogui.click(x=792, y=406)

# passo 2 - Fazer login
# digitar o e-mail
pyautogui.write("mateus.santos@gmail.com")
# passar para o campo da senha        

pyautogui.press("tab")
# digitar a senha
pyautogui.write("minhasenha")
# e logar
pyautogui.click(x=963, y=572)

# passo 3 - importar base de dados
# pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")

# passo 4 - cadastrar um produto

for line in tabela.index:
    codigo = tabela.loc[line, "codigo"]
    
    marca = tabela.loc[line, "marca"]
    
    tipo = tabela.loc[line, "tipo"]
    
    categoria = tabela.loc[line, "categoria"]   
    
    preco = tabela.loc[line, "preco_unitario"]
    
    custo = tabela.loc[line, "custo"]
    
    obs = tabela.loc[line, "obs"]
    
    
    pyautogui.click(x=785, y=291)
    # codigo
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    # preco
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    # obs
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    # enviar 
    pyautogui.press("enter")
    pyautogui.scroll(1000)

# passo 5 - repetir isso acabar a base de dados