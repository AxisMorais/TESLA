##-----------------------------------------------------------------------------------------------
##                                             CARGA SIEST ##
##-----------------------------------------------------------------------------------------------
# Importando os Módulos
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time


class ExecutorCargaSIEST:

    def executarCargaSIEST():
        # ABRIR O NAVEGADOR
        navegador = webdriver.Chrome()

        # ACESSAR O SITE DO CIC:
        navegador.get('http://cic-hm.pbh/')

        # ENCONTRAR O ELEMENTO COM A TAG NAME NO HTML E ESCREVENDO NO CAMPO O LOGIN DO SISTEMA:
        navegador.find_element(By.NAME, 'josso_username').send_keys('Inserir login de acesso')

        # ENCONTRAR O ELEMENTO COM A TAG NAME NO HTML E ESCREVER A SENHA PARA ACESSAR O SISTEMA:
        navegador.find_element(By.NAME, 'josso_password').send_keys('Inserir senha de acesso')

        # Clicar no botão para acessar o sistema:
        navegador.find_element(By.CLASS_NAME, "botao").click()

        # Clicar na opção do Menu Cargas de sistemas
        navegador.find_element(By.XPATH, '//*[@id="geral"]/div[2]/ul/li[5]/a').click()

        # Escolhendo a carga SIEST para ser ralizada:
        navegador.find_element(By.XPATH, '//*[@id="geral"]/div[2]/ul/li[5]/ul/li[2]/a').click()


        #Clicar na opção do agendador
        navegador.find_element(By.ID, "datahora").click()

        #Tempo de espera de 3 segundos
        time.sleep(3)

        #------------------------------------------------------------------------
        #CALCULO TRADICIONAL
        #Calculo do minuto adicional
        #Pegando a data do sistema
        dataCompletaSistema = datetime.now()

        #Formatando a data para o padrão CIC- Brasil
        dataFormatadaString = dataCompletaSistema.strftime('%d/%m/%Y %H:%M')

        #Pegando o minuito, observe que é uma string
        minutoSeparadoString = dataCompletaSistema.strftime('%M')

        #Transformando o munito em int
        minutoSeparadoInt = int(minutoSeparadoString)

        # Caso tradicional: Incrementar um minuto
        minutoIncrementado = (minutoSeparadoInt + 3)

        #Transformando de int prar string para escrever esse minuto calculado no sistema CIC
        minutoIncrementado = str(minutoIncrementado)

        #Fatiando a string para pegar apenas a data e o minuto antigo sem inserir o minuto incrementado
        dataSeparadaComMinuto = dataFormatadaString[0:14]

        #Concatenando o minuto calculado  string junto com a data que foi fatiada string desprezando o minuto antigo
        tempoFinal = (dataSeparadaComMinuto + minutoIncrementado)

       # Escrevendo o horário no campo data hora
        navegador.find_element(By.ID, "datahora").send_keys(tempoFinal)

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
        if (minutoSeparadoInt >= 0 and minutoSeparadoInt <= 7):
            minutoSeparadoInt = minutoSeparadoInt + 2
            minutoSeparadoString = str(minutoSeparadoInt)
            minutoSeparadoString = ('0' + minutoSeparadoString)
            novadata = dataFormatadaString[0:14]
            dataFinal = (novadata + minutoSeparadoString)
            print(dataFinal)
            # Escrevendo o horário no campo data hora
            navegador.find_element(By.ID, "datahora").send_keys(dataFinal)


        # Clicar no botão Gravar
        navegador.find_element(By.ID, "gravar").click()
        time.sleep(250)

    try:
        executarCargaSIEST();
    except:
        executarCargaSIEST();

meuObjetoTeste = ExecutorCargaSIEST
for x in range(0, 6):
    try:
        meuObjetoTeste.executarCargaSIEST()
    except:
        meuObjetoTeste.executarCargaSIEST()

