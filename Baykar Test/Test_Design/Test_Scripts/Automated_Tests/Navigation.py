from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")


# Testin Chrome üzerinde çalışması için webdriver kurulumu yapılır
driver = webdriver.Chrome(options=options)

#Adding implicit wait
driver.implicitly_wait(10)

# BaykarTech Kariyer sayfasına gidilir
driver.get("https://kariyer.baykartech.com/tr/")

#Hover yapacağımız yeri buluyoruz
hover_element = driver.find_element("xpath", "(//*[@class='dropdown-toggle smooth-menu'])[1]")
ActionChains(driver).move_to_element(hover_element).perform()

#Dropdown menüsünün altındaki kısımlara sırayla tıklıyoruz
istatistik_option = driver.find_element_by_xpath("(//*[@class='smooth-menu'])[1]")
istatistik_option.click()


driver.close()