import selectors
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path='/home/david/Downloads/chromedriver')

driver.get("https://linkedin.com")

user = driver.find_element("id", "session_key")
user.send_keys("")          # INPUT USERNAME
password = driver.find_element("id", "session_password")
password.send_keys("")      #INPUT PASSWORD
password.send_keys(Keys.RETURN)

time.sleep(3)

search = driver.find_element("class name", "search-global-typeahead__collapsed-search-button")
search.click()
search = driver.find_element("class name", "search-global-typeahead__input")
search.send_keys("Software Engineer")       #What type of people you want to connect with
search.send_keys(Keys.RETURN)

time.sleep(3)

people = driver.find_element("class name", "artdeco-pill")
people.click()

time.sleep(3)

connections = driver.find_element("xpath", "//body/div[6]/div[3]/div[2]/section[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/div[1]/span[1]/button[1]")
connections.click()
connections = driver.find_element("xpath", "//body/div[6]/div[3]/div[2]/section[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/fieldset[1]/div[1]/ul[1]/li[2]/label[1]")
connections.click()
connections = driver.find_element("xpath", "//body/div[6]/div[3]/div[2]/section[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/fieldset[1]/div[1]/ul[1]/li[3]/label[1]")
connections.click()
connections = driver.find_element("xpath", "/html[1]/body[1]/div[6]/div[3]/div[2]/section[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/fieldset[1]/div[2]/button[2]")
connections.click()
time.sleep(3)

for y in range(10):
    for x in range(1,11):
        text = driver.find_element("xpath", "/html[1]/body[1]/div[6]/div[3]/div[2]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/ul[1]/li["+ str(x) +"]/div[1]/div[1]/div[3]/div[1]/button[1]/span[1]").text
        connect = driver.find_element("xpath", "/html[1]/body[1]/div[6]/div[3]/div[2]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/ul[1]/li["+ str(x) +"]/div[1]/div[1]/div[3]/div[1]/button[1]")
        ActionChains(driver).scroll_to_element(connect).perform()
        if text == "Connect":
            connect.click()
            time.sleep(1)
            sendmodal = driver.find_element("id", "send-invite-modal").text
            if sendmodal == "Connect":
                driver.find_element("xpath", "/html[1]/body[1]/div[3]/div[1]/div[1]/button[1]").click()
            else:
                driver.find_element("xpath", "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[2]").click()
        else:
            print(text)
        time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")            
    next = driver.find_element("css selector", '[aria-label="Next"]').click()
    time.sleep(3)