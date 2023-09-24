######################################################################################
                             ### EXECUTOR DE CARGA DE ENERGIA EINSTEIN ###
######################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time


def executaCarga(mesArmazenador):
    mesArmazenador = mesArmazenador

    # ABRIR O NAVEGADOR
    navegador = webdriver.Chrome()

    # ACESSAR O SITE DO CIC:
    navegador.get('http://cic.pbh/')

    # ENCONTRAR O ELEMENTO COM A TAG NAME NO HTML E ESCREVENDO NO CAMPO O LOGIN DO SISTEMA:
    navegador.find_element(By.NAME, 'josso_username').send_keys('thiago.conegundes')

    # ENCONTRAR O ELEMENTO COM A TAG NAME NO HTML E ESCREVER A SENHA PARA ACESSAR O SISTEMA:
    navegador.find_element(By.NAME, 'josso_password').send_keys('Th1505@')

    # Clicar no botão para acessar o sistema:
    navegador.find_element(By.CLASS_NAME, "botao").click()

    #Clicar na opção do Menu Cargaas de Arquivo:
    navegador.find_element(By.XPATH, '//*[@id="geral"]/div[2]/ul/li[3]/a').click()

    #Clicar na opção: Carregar custo com energia:
    navegador.find_element(By.XPATH, '//*[@id="geral"]/div[2]/ul/li[3]/ul/li[4]/a').click()

    time.sleep(3)

    #EXECUÇÃO DE MULTIPLAS CARGAS
    janeiro = ('C:/Users/pres00310855/Desktop/Material de Trabalho/ENERGIA/ENERGIA 2022/CustocomEnergia_012022.zip')
    fevereiro = ('C:/Users/pres00310855/Desktop/Material de Trabalho/ENERGIA/ENERGIA 2022/CustocomEnergia_022022.zip')
    marco = ('C:/Users/pres00310855/Desktop/Material de Trabalho/ENERGIA/ENERGIA 2022/CustocomEnergia_032022.zip')
    abril = ('C:/Users/pres00310855/Desktop/Material de Trabalho/ENERGIA/ENERGIA 2022/CustocomEnergia_042022.zip')
    maio = ('C:/Users/pres00310855/Desktop/Material de Trabalho/ENERGIA/ENERGIA 2022/CustocomEnergia_052022.zip')
    junho = ('C:/Users/pres00310855/Desktop/Material de Trabalho/ENERGIA/ENERGIA 2022/CustocomEnergia_062022.zip')
    julho = ('C:/Users/pres00310855/Desktop/Material de Trabalho/ENERGIA/ENERGIA 2022/CustocomEnergia_072022.zip')
    agosto = ('C:/Users/pres00310855/Desktop/Material de Trabalho/ENERGIA/ENERGIA 2022/CustocomEnergia_082022.zip')
    setembro = ('C:/Users/pres00310855/Desktop/Material de Trabalho/ENERGIA/ENERGIA 2022/CustocomEnergia_092022.zip')
    outurbo = ('C:/Users/pres00310855/Desktop/Material de Trabalho/ENERGIA/ENERGIA 2022/CustocomEnergia_102022.zip')
    novembro = ('C:/Users/pres00310855/Desktop/Material de Trabalho/ENERGIA/ENERGIA 2022/CustocomEnergia_112022.zip')
    dezembro = ('C:/Users/pres00310855/Desktop/Material de Trabalho/ENERGIA/ENERGIA 2022/CustocomEnergia_122022.zip')

    listaArquivos = [janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outurbo, novembro, dezembro]

    #Acessar os arquivos de energia para Up_load
    navegador.find_element(By.XPATH, '//*[@id="arquivo_zip"]').send_keys(listaArquivos[mesArmazenador])

    # Clicando na opção carregar arquivo
    navegador.find_element(By.XPATH, '//*[@id="carregar"]').click()

    # Clicando na opção carregar arquivo
    navegador.find_element(By.XPATH, '//*[@id="gravar"]').click()

    #Esperando agluns segundo;
    time.sleep(150)


print('Lembre-se cada mês ocupa uma posição indice do vetor.')
print('Janiero está na primeira posição referente ao  índice zero do vetor. Caso queira começar de janeiro precione 0')
mesArmazenador = int(input('Informe o mês de referência: exemplo: 4:\n'))

for x in range(1,12):
    try:
        executaCarga(mesArmazenador)
    except:
        executaCarga(mesArmazenador)
    mesArmazenador = mesArmazenador + 1



