from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Testin Chrome üzerinde çalışması için webdriver kurulumu yapılır
driver = webdriver.Chrome()

#Adding implicit wait
driver.implicitly_wait(10)

# BaykarTech Kariyer sayfasına gidilir
driver.get("https://kariyer.baykartech.com/tr/")

# Giriş tuşu bulunur ve tıklanır
login_button = driver.find_element("xpath", "//*[@id='home']/nav/div/div[1]/ul/li[2]/a")
login_button.click()

# Kullanıcı adı, şifre ve captcha alanları bulunur
username_field = driver.find_element("name", "login")
password_field = driver.find_element("name", "password")

#Testi görebilmek için bekletiyorum
driver.implicitly_wait(5)

username_field.send_keys("TEST_USER")
password_field.send_keys("-TEST_PASSWORD-")

driver.implicitly_wait(5)

captcha_field = driver.find_element("class", "recaptcha-checkbox-border")
captcha_field.click()
# Login tuşuna basılır
giris_button = driver.find_element("id", "kt_sign_in_submit")
giris_button.click()

#Bu aşamada test yapabilmemiz için bir test kullanıcısı sağlanmadığı için ve
#doğal olarak güvenlik sebeplerinden ötürü kendi bilgilerimi de giremeyeceğim için
#login işlemini gerçekleştiremiyorum. Bu yüzden testi burada sonlandırıyorum.


# Webdriver kapatılır
driver.close()