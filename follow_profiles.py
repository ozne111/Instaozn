from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configuração do driver do Selenium
driver_path = "caminho_para_o_seu_driver"  # Substitua pelo caminho para o seu driver

# Informações de login do Instagram
username = "seu_nome_de_usuário"  # Insira seu nome de usuário do Instagram
password = "sua_senha"  # Insira sua senha do Instagram

# Perfis a seguir
perfis_seguir = ["neymarjr", "selenagomez"]

# Função para seguir um perfil
def seguir_perfil(perfil):
    driver.get("https://www.instagram.com/" + perfil)
    time.sleep(2)
    seguir_button = driver.find_element_by_xpath("//button[contains(text(), 'Seguir')]")
    seguir_button.click()
    time.sleep(5)

# Função para fazer login no Instagram
def fazer_login(username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)
    username_input = driver.find_element_by_name("username")
    username_input.send_keys(username)
    password_input = driver.find_element_by_name("password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

# Configuração do driver do Chrome
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")  # Executar em modo headless, sem exibição do navegador

# Inicializar o driver do Chrome
driver = webdriver.Chrome(executable_path=driver_path, options=options)

# Fazer login no Instagram
fazer_login(username, password)

# Seguir perfis
for perfil in perfis_seguir:
    seguir_perfil(perfil)
    time.sleep(5)

# Fechar o driver
driver.quit()
