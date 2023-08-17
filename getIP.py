from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://geonode.com/free-proxy-list")

download = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div/d"
                 "iv/div[1]/div/section/div/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div")))
# //*[@id="__next"]/div/div/div[1]/div/section/div/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div

# <span class="flex gap-2 items-center"><svg width="18" height="17" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9.83317 1.15064C9.83317 0.690403 9.46008 0.317307 8.99984 0.317307C8.5396 0.317307 8.1665 0.690403 8.1665 1.15064V10.8055L4.58909 7.22805C4.26366 6.90261 3.73602 6.90261 3.41058 7.22805C3.08514 7.55349 3.08514 8.08113 3.41058 8.40656L8.41058 13.4066C8.73602 13.732 9.26366 13.732 9.58909 13.4066L14.5891 8.40656C14.9145 8.08113 14.9145 7.55349 14.5891 7.22805C14.2637 6.90261 13.736 6.90261 13.4106 7.22805L9.83317 10.8055V1.15064Z" fill="#EDEEEF"></path><path d="M0.666504 16.1506C0.666504 15.6904 1.0396 15.3173 1.49984 15.3173H16.4998C16.9601 15.3173 17.3332 15.6904 17.3332 16.1506C17.3332 16.6109 16.9601 16.984 16.4998 16.984H1.49984C1.0396 16.984 0.666504 16.6109 0.666504 16.1506Z" fill="#EDEEEF"></path></svg> <!-- -->Download<!-- --> </span>
# <button type="button" class="cursor-pointer inline-flex justify-center items-center font-medium rounded shadow-sm bg-primary-base w-full bg-[#4d5674] button-sm text-sm leading-5 px-4 py-2 text-white hover:bg-opacity-70"><span class="flex gap-2 items-center"><svg width="18" height="17" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9.83317 1.15064C9.83317 0.690403 9.46008 0.317307 8.99984 0.317307C8.5396 0.317307 8.1665 0.690403 8.1665 1.15064V10.8055L4.58909 7.22805C4.26366 6.90261 3.73602 6.90261 3.41058 7.22805C3.08514 7.55349 3.08514 8.08113 3.41058 8.40656L8.41058 13.4066C8.73602 13.732 9.26366 13.732 9.58909 13.4066L14.5891 8.40656C14.9145 8.08113 14.9145 7.55349 14.5891 7.22805C14.2637 6.90261 13.736 6.90261 13.4106 7.22805L9.83317 10.8055V1.15064Z" fill="#EDEEEF"></path><path d="M0.666504 16.1506C0.666504 15.6904 1.0396 15.3173 1.49984 15.3173H16.4998C16.9601 15.3173 17.3332 15.6904 17.3332 16.1506C17.3332 16.6109 16.9601 16.984 16.4998 16.984H1.49984C1.0396 16.984 0.666504 16.6109 0.666504 16.1506Z" fill="#EDEEEF"></path></svg> <!-- -->Download<!-- --> </span></button>
# cursor-pointer inline-flex justify-center items-center font-medium rounded shadow-sm bg-primary-base w-full bg-[#4d5674] button-sm text-sm leading-5 px-4 py-2 text-white hover:bg-opacity-70
#<div class="button_buttonWrapper__GGCey font-medium  "><button type="button" class="cursor-pointer inline-flex justify-center items-center font-medium rounded shadow-sm bg-primary-base w-full bg-[#4d5674] button-sm text-sm leading-5 px-4 py-2 text-white hover:bg-opacity-70"><span class="flex gap-2 items-center"><svg width="18" height="17" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9.83317 1.15064C9.83317 0.690403 9.46008 0.317307 8.99984 0.317307C8.5396 0.317307 8.1665 0.690403 8.1665 1.15064V10.8055L4.58909 7.22805C4.26366 6.90261 3.73602 6.90261 3.41058 7.22805C3.08514 7.55349 3.08514 8.08113 3.41058 8.40656L8.41058 13.4066C8.73602 13.732 9.26366 13.732 9.58909 13.4066L14.5891 8.40656C14.9145 8.08113 14.9145 7.55349 14.5891 7.22805C14.2637 6.90261 13.736 6.90261 13.4106 7.22805L9.83317 10.8055V1.15064Z" fill="#EDEEEF"></path><path d="M0.666504 16.1506C0.666504 15.6904 1.0396 15.3173 1.49984 15.3173H16.4998C16.9601 15.3173 17.3332 15.6904 17.3332 16.1506C17.3332 16.6109 16.9601 16.984 16.4998 16.984H1.49984C1.0396 16.984 0.666504 16.6109 0.666504 16.1506Z" fill="#EDEEEF"></path></svg> Download </span></button></div>

# Click the "Download" button
download.click()

driver.quit()
