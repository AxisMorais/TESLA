from datetime import time, datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import datetime
from datetime import datetime
from selenium import webdriver 

class ExecutorCargaCAT:
    
    def executarCargaCat(quantidade):
    
        for x in range(0, quantidade):
            
            #Inicia o webdriver 
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

            # Acessando a opção Carga de produção
            navegador.find_element(By.XPATH, '//*[@id="geral"]/div[2]/ul/li[5]/ul/li[5]/a').click()

            # Escolhendo a carga CAT para ser ralizada:
            navegador.find_element(By.ID, "secretaria_educacao-18").click()

            time.sleep(3)

            # Clicar na opção do agendador
            navegador.find_element(By.ID, "datahora").click()
          
            # ------------------------------------------------------------------------------
            # Esperando por 3 segundo a finalização da esrita
            time.sleep(3)

            # Clicar no botão Gravar
            #navegador.find_element(By.ID, "gravar").click()

            # Esperando por 3 segundo a finalização da esrita
            time.sleep(5)

            # Clicar no botão Gravar
            #navegador.find_element(By.ID, "gravar").click()

            # Esperar 5 segundos para sair
            time.sleep(3)
            navegador.quit()
