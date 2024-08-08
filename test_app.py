from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pathlib import Path

driver = webdriver.Chrome()

try:
    
    driver.get("http://4.174.210.241:8501")  
    
    file_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )

    path = Path("C:/Users/praha/Desktop/DIRECTED_STUDIES_PROJECT/archive/Data/genres_original/Test/disco.00011.wav")
    file_input.send_keys(str(path))
    time.sleep(10)

finally:
    driver.quit()
