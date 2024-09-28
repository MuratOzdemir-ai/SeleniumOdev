from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_driver_path = "C:\\Users\\MURAT\\Desktop\\chromedriver-win64\\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

vw_araclar = {
    "Tiguan": "https://binekarac.vw.com.tr/tr/modeller-fiyatlar/arac-modelleri/vw-yeni-tiguan.html",
    "Passat": "https://binekarac.vw.com.tr/tr/modeller-fiyatlar/arac-modelleri/yeni-passat.html",
    "Polo": "https://binekarac.vw.com.tr/tr/modeller-fiyatlar/arac-modelleri/yeni-polo.html",
    "T-Cross": "https://binekarac.vw.com.tr/tr/modeller-fiyatlar/arac-modelleri/yeni-t-cross.html",
    "Taigo": "https://binekarac.vw.com.tr/tr/modeller-fiyatlar/arac-modelleri/taigo.html",
    "Golf": "https://binekarac.vw.com.tr/tr/modeller-fiyatlar/arac-modelleri/yeni-golf.html",
    "T-Roc": "https://binekarac.vw.com.tr/tr/modeller-fiyatlar/arac-modelleri/yeni-t-roc.html",
    "Touareg":"https://binekarac.vw.com.tr/tr/modeller-fiyatlar/arac-modelleri/yeni-touareg.html",
}

fiyatlar = {}

for arac, url in vw_araclar.items():
    driver.get(url)
    time.sleep(5)
    try:
        fiyat_elementi = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/main/div/div/div[1]/div/div/div[2]/div/div/section/div/ul/li[1]'))
        )
        fiyatlar[arac] = fiyat_elementi.text
    except Exception as e:
        print(f"{arac} için hata: {e}")


for arac, fiyat in fiyatlar.items():
    print(f"{arac}  {fiyat}")

driver.quit()

