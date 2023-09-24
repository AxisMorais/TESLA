#---------------------------------------------------------------------------------------------
                             #APAGADOR DE CARGA DE ENERGIA - TESLA
#---------------------------------------------------------------------------------------------
#Importando os Módulos e bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


class ApagadorCargaEnergia:

    def apagarCarga(self):
        quantidade = int(input("Informe a quantidade de cargas a apagar: "))

        for x in range(0, quantidade):
            # ABRIR O NAVEGADOR
            navegador = webdriver.Chrome()

            # ACESSAR O SITE DO CIC:
            navegador.get('http://cic.pbh/')

            # ENCONTRAR O ELEMENTO COM A TAG NAME NO HTML E ESCREVENDO NO CAMPO O LOGIN DO SISTEMA:
            navegador.find_element(By.NAME, 'josso_username').send_keys('Inserir login de acesso ')

            # ENCONTRAR O ELEMENTO COM A TAG NAME NO HTML E ESCREVER A SENHA PARA ACESSAR O SISTEMA:
            navegador.find_element(By.NAME, 'josso_password').send_keys('Inserir senha de acesso')

            # Clicar no botão para acessar o sistema:
            navegador.find_element(By.CLASS_NAME, "botao").click()

            # Acessar a opção Gerenciamento:
            navegador.find_element(By.XPATH, '//*[@id="geral"]/div[2]/ul/li[6]/a').click()

            # Acessar a opção apagar Carga:
            navegador.find_element(By.XPATH, '//*[@id="geral"]/div[2]/ul/li[6]/ul/li[4]/a').click()

            # Clicar na opção para selecionar o tipo de carga a ser apagada
            navegador.find_element(By.ID, 'tipo_dado_carga').click()
            navegador.find_element(By.ID, 'tipo_dado_carga').send_keys('CUSTO COM ENERGIA')

            # Clicar na opção pesquisar:
            navegador.find_element(By.ID, 'carregar').click()

            # Preencher o campo Regional
            navegador.find_element(By.NAME, 'regional').send_keys('Regional Geral PBH')

            # Seleciona a opção ADMINISTRAÇÃO SUPERIOR DO EXECUTIVO MUNICIPAL
            navegador_II = navegador.find_element(By.ID, 'entidade')
            time.sleep(2)
            seletor = Select(navegador_II)
            seletor.select_by_value('1')

            # Clicar no botão pesquisar e acessar a pilha da carga de energia
            navegador.find_element(By.XPATH, '//*[@id="carregar"]').click()

            # Apagar a ultima carga!
            navegador.find_element(By.XPATH, '//*[@id="gravar"]').click()
            time.sleep(3)

            # Confirmando
            alerta = navegador.switch_to.alert
            alerta.accept()
            time.sleep(560)



meuObjetoTeste= ApagadorCargaEnergia
meuObjetoTeste.apagarCarga(0)












