##-----------------------------------------------------------------------------------------------
                                            ## CARGA SGEE ##
##-----------------------------------------------------------------------------------------------
# Importando os Módulos e bibliotecas

import time
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium import webdriver

# ABRIR O NAVEGADOR

# Inicia o webdriver
driver = webdriver.chrome

navegador = webdriver.Chrome()

navegador.get('http://cic.pbh/')

campo_username = navegador.find_element(by='name', value='josso_username')
campo_username.send_keys('thiago.conegundes')

campo_senha = navegador.find_element(by='name', value='josso_password')
campo_senha.send_keys('Th1505@')

# Clicar no botão para acessar o sistema:
navegador.find_element(By.CLASS_NAME, "botao").click()

# Clicar na opção do Menu Cargaas de sistemas
navegador.find_element(By.XPATH, '//*[@id="geral"]/div[2]/ul/li[5]/a').click()

# Clicar na opção do Menu Cargaas de sistemas
navegador.find_element(By.XPATH, '//*[@id="geral"]/div[2]/ul/li[5]/ul/li[5]/a').click()

# Acessando a opção Carga de produção
navegador.find_element(By.XPATH, '//*[@id="secretaria_educacao-14"]').click()

# Escolhendo a carga SGEE para ser ralizada:
navegador.find_element(By.ID, "superintendencia_limpeza_urbana-15").click()

# Clicar na opção do agendador
navegador.find_element(By.ID, "datahora").click()
# ------------------------------------------------------------------------

##Calculo do minuto adicional
dataCompletaSistema = datetime.now()
dataFormatadaString = dataCompletaSistema.strftime('%d/%m/%Y %H:%M')
minutoSeparadoString = dataCompletaSistema.strftime('%M')
minutoSeparadoInt = int(minutoSeparadoString)

# Caso tradicional: Incrementar um minuto
minutoIncrementado = (minutoSeparadoInt + 2)
minutoIncrementado = str(minutoIncrementado)
dataSeparadaComMinuto = dataFormatadaString[0:14]
tempoFinal = (dataSeparadaComMinuto + minutoIncrementado)

# Caso o minuto chegar em 58 ou 59 é necessário zerar os minutos e incrementar as horas
if (minutoSeparadoInt == 58 or minutoSeparadoInt == 59):
    horaSeparadaString = dataCompletaSistema.strftime('%I')
    horaSeparadaInt = int(horaSeparadaString)
    horaSeparadaInt = horaSeparadaInt + 1
    horaSeparadaString = str(horaSeparadaInt)
    minutoIncrementado = 2
    minutoIncrementadoString = str(minutoIncrementado)
    novaData = dataFormatadaString[0:11]
    horaFinal = (horaSeparadaString + ':0' + minutoIncrementadoString)
    dataFinal = (novaData + horaFinal)
    navegador.find_element(By.ID, "datahora").send_keys(dataFinal)
    print(tempoFinal)

# ----------------------------------------------------------------------------------
# Caso estivermos no intervalo de tempo do minuto 00 à 09
if (minutoSeparadoInt >= 0 and minutoSeparadoInt <= 9):
    minutoSeparadoInt = minutoSeparadoInt + 2
    minutoSeparadoString = str(minutoSeparadoInt)
    minutoSeparadoString = ('0' + minutoSeparadoString)
    novadata = dataFormatadaString[0:14]
    dataFinal = (novadata + minutoSeparadoString)
    print(dataFinal)
    # Escrevendo o horário no campo data hora
    navegador.find_element(By.ID, "datahora").send_keys(dataFinal)
    time.sleep(2)
navegador.find_element(By.ID, "datahora").send_keys(tempoFinal)
time.sleep(10)
# Clicar no botão Gravar
navegador.find_element(By.ID, "gravar").click()
