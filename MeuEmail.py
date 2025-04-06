from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.wait import WebDriverWait # type: ignore
import time
from selenium.webdriver.common.action_chains import ActionChains #type: ignore
from selenium.webdriver.common.keys import Keys #type: ignore
from selenium.webdriver.firefox.options import Options#type: ignore


emails = ['vitornc31@gmail.com', 'pessoa3@gmail.com', 'pessoa4@gmail.com', 'pessoa5@gmail.com']

caminhoPerfil = r"C:\Users\Gilberto\AppData\Roaming\Mozilla\Firefox\Profiles\wbsbgekg.default-release-1612880842279"
#caminho do seu navegador

options = Options()
options.add_argument("-profile")
options.add_argument(caminhoPerfil)


nav = webdriver.Firefox(options=options)
nav.get('https://mail.google.com')
time.sleep(5)
botaoEnviar = nav.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/div[1]/div[1]/div/div')
botaoEnviar.click()
time.sleep(3)
for email in emails:
    ActionChains(nav)\
        .send_keys(email)\
        .pause(1)\
        .send_keys(Keys.TAB)\
        .pause(1)\
        .perform()
Assunto = 'Este é o assunto'
CorpoMsg = 'Este é o corpo da mensagem.'
ActionChains(nav)\
        .send_keys(Keys.TAB)\
        .send_keys(Assunto)\
        .pause(1)\
        .send_keys(Keys.TAB)\
        .pause(1)\
        .send_keys(CorpoMsg)\
        .perform()
