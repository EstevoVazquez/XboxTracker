
import json
import requests
import time as stime
from datetime import datetime, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


 
TOKEN = "Your_telegram_token"
URL = "https://api.telegram.org/bot" + TOKEN + "/"
URL_CORTE_INGLES = "https://www.elcorteingles.es/videojuegos/A37047078/"
URL_PC_COMPONENTES= "https://www.pccomponentes.com/microsoft-xbox-series-x-1tb"
URL_GAME ="https://www.game.es/HARDWARE/CONSOLA/XBOX-SERIES-X/XBOX-SERIES-X/182899"
URL_XTRALIFE="https://www.xtralife.com/producto/xbox-series-x-xbox-series/61325"
TELEGRAM_CHAT_ID = "your_telegram_chat_id"

def enviar_mensaje(texto):
    requests.get(URL + "sendMessage?text=" + texto + "&chat_id=" + TELEGRAM_CHAT_ID)

def corte_ingles(driver):
    try:
        print("Mirando Corte Ingles")
        driver.get(URL_CORTE_INGLES)
        stime.sleep(10)
        driver.find_element_by_id("cookies-agree").click()
        WebDriverWait(driver, timeout=4)
        button = driver.find_elements_by_class_name("js-add-to-cart")
        if button:
            print("enviando msg")
            enviar_mensaje("xbox disponible en ->" + URL_CORTE_INGLES)
            return True
        print("no disponible")
        return False
    except :
        print("exception")
        return False

def pc_componentes(driver):
    print("Mirando pc componentes")
    try:
        driver.get(URL_PC_COMPONENTES)
        stime.sleep(10)
        driver.find_elements_by_class_name("accept-cookie")[0].click()
        button = driver.find_element_by_id("add-cart")
        if button:
            print("enviando msg")
            enviar_mensaje("xbox disponible en ->" + URL_PC_COMPONENTES)
            return True
        print("no disponible")
        return False
    except :
        print("exception")
        return False
    

def game(driver):
    print("Mirando game")
    try:
        driver.get(URL_GAME)
        stime.sleep(10)
        driver.find_element_by_id("btnOverlayCookiesClose").click()
        button = driver.find_elements_by_class_name("buy--btn") 
        if button:
            print("enviando msg")
            enviar_mensaje("xbox disponible en ->" + URL_GAME)
            return True
        print("no disponible")
        return False
    except :
        print("no disponible")
        return False

def xtralife(driver):
    print("Mirando xtralife")
    try:
        driver.get(URL_XTRALIFE)
        stime.sleep(10)
        button = driver.find_elements_by_class_name("actionText")
        for b in button:
            html = b .get_attribute('innerHTML')
            #print(html)
            if "agotadas" not in html:
                print("enviando msg")
                enviar_mensaje("xbox disponible en ->" + URL_XTRALIFE)
                return True
        
        print("no disponible")
        return False
    except :
        print("exception")
        return False


def is_time_between(begin_time, end_time, check_time=None):
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: 
        return check_time >= begin_time or check_time <= end_time  

def main():
    while True:
        if is_time_between(time(9,00), time(22,00)) ==True:
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
            corte_ingles(driver)
            pc_componentes(driver)
            game(driver)
            xtralife(driver)
            driver.close()   



if __name__ == '__main__':
    main()