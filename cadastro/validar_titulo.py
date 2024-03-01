from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Inicializa o navegador Chrome em modo headless
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

# Abre a página do TSE
driver.get('https://www.tse.jus.br/servicos-eleitorais/titulo-e-local-de-votacao/copy_of_consulta-por-nome')

# Preenche o campo do título de eleitor
titulo_input = driver.find_element(By.XPATH, '//*[@id="SE_NomeTituloCPF"]')
titulo_input.send_keys('139186430337')

# Pressiona a tecla Enter
titulo_input.send_keys(Keys.ENTER)

# Espera até que o parágrafo com as informações seja carregado na página
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="return-form-situacao-eleitoral"]/p[2]'))
    )
except:
    print("Tempo de espera excedido. Não foi possível encontrar as informações.")

# Obtém as informações desejadas
situacao_element = driver.find_element(By.XPATH, '//*[@id="return-form-situacao-eleitoral"]//p[2]')
situacao_texto = situacao_element.text.split(':')[1].strip()
print(situacao_texto)

# Fecha o navegador
driver.quit()
