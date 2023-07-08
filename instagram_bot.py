from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configuração do driver do Selenium
driver = webdriver.Chrome()

# URL da página de login do Instagram
url = "https://www.instagram.com/accounts/login/"

# Informações de login
username = "seu_nome_de_usuário"
password = "sua_senha"

# Perfis a seguir e parar de seguir
perfis_seguir = ["neymarjr", "leomessi"]

# Função para seguir um perfil
def seguir_perfil(perfil):
    driver.get("https://www.instagram.com/" + perfil)
    time.sleep(2)
    seguir_button = driver.find_element_by_xpath("//button[contains(text(), 'Seguir')]")
    seguir_button.click()
    time.sleep(5)

# Função para parar de seguir um perfil
def parar_de_seguir_perfil(perfil):
    driver.get("https://www.instagram.com/" + perfil)
    time.sleep(2)
    seguir_button = driver.find_element_by_xpath("//button[contains(text(), 'Seguindo')]")
    seguir_button.click()
    time.sleep(2)
    confirmar_button = driver.find_element_by_xpath("//button[contains(text(), 'Deixar de seguir')]")
    confirmar_button.click()
    time.sleep(5)

# Fazer login
driver.get(url)
time.sleep(2)
username_input = driver.find_element_by_name("username")
username_input.send_keys(username)
password_input = driver.find_element_by_name("password")
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)
time.sleep(5)

# Seguir e parar de seguir perfis
while True:
    for perfil in perfis_seguir:
        seguir_perfil(perfil)
        time.sleep(5)
    for perfil in perfis_seguir:
        parar_de_seguir_perfil(perfil)
        time.sleep(5)

# Fechar o driver
driver.quit()
