from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://geonode.com/free-proxy-list")

# Wait for the "Download" button to be clickable
wait = WebDriverWait(driver, 10)
# button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bg-primary-base")))
button = driver.find_element(By.CLASS_NAME, "bg-primary-base")

# Click the "Download" button
button.click()

driver.quit()
