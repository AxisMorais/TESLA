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

