from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1200,800', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    return driver

driver = iniciar_driver()





#entrar no site do facebook
driver.get('https://facebook.com/')
sleep(3)
driver.maximize_window()
sleep(2)
#encontrar campo de usuário e digitar
campo_usuario = driver.find_element(By.XPATH,"//input[@id='email']")
sleep(2)
campo_usuario.send_keys("seuemail@email.com")
sleep(2)
#encontrar campo de senha e digitar
campo_senha = driver.find_element(By.XPATH,"//input[@id='pass']")
sleep(2)
campo_senha.send_keys("senha")
sleep(2)
#apertar botão login
botao_login = driver.find_element(By.XPATH,"//button[@name='login']")
botao_login.click()
sleep(6)
#encontrar e clicar no campo de postagem
postagem = driver.find_element(By.XPATH, "//div[@class='xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe']")
sleep(3)
postagem.click()
sleep(3)
#clicar dentro do campo de status
dentro_status = driver.find_element(By.XPATH, "//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
sleep(3)
#digitar no campo status
dentro_status.send_keys('Opa, beleza? Aqui está o exemplo!')
sleep(3)
#clicar em publicar
publicar = driver.find_element(By.XPATH,"//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 x1r8uery x1iyjqo2 xs83m0k xeuugli x1qughib x6s0dn4 xozqiw3 x1q0g3np x1pi30zi x1swvt13 xyamay9 xcud41i x139jcc6 x4vbgl9 x1rdy4ex']")
publicar.click()
sleep(3)
driver.execute_script("window.scrollTo(0,150);")




# %USERPROFILE%






input('')
driver.close()