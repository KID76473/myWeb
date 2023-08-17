from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

# proxy_ip = "119.17.192.97"
# proxy_port = "1080"
# proxy = f"https://{proxy_ip}:{proxy_port}"
#
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f'--proxy-server={proxy}')  # change IP address
chrome_options.add_experimental_option("detach", True)  # does not close webpage automatically

driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")

# email = "kid76473@gmail.com"
email = "13161133872@163.com"
password = "Hjjhjjhjj007"

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

email_elem = driver.find_element(By.ID, "username")
email_elem.send_keys(email)

password_elem = driver.find_element(By.ID, "password")
password_elem.send_keys(password)

button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"organic-div\"]/for"
                                                                                   "m/div[3]/button")))
button.click()

search = driver.find_element(By.XPATH, "/html/body")

sleep(10)

driver.quit()
