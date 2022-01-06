# relevant imports and initialization
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome('chromedriver')

try:
        # open url in browser
        url = "https://youtube.com"
        driver.get(url)
        driver.implicitly_wait(3)

        # finding by ID
        element_name = driver.find_element(By.ID, 'video-title-link')
        element_name.click()

        # combining the two lines of code
        # comments
        driver.find_element(By.ID, 'guide-icon').click()

        # finding by CSS
        driver.find_element(By.CSS_SELECTOR, 'yt-icon[id="guide-icon"]').click()

        # finding multiple elements
        elements = driver.find_elements(By.XPATH, '//*[@id="guide-icon"]')
        elements[1].click()
        
        # finding by NAME
        field = driver.find_element(By.NAME, 'search_query')
        
        field.send_keys("truck")
        print(field.get_attribute("value"))
        field.clear()
        field.send_keys("spiderman")
        field.submit()

        first_video = driver.find_element(By.ID, 'video-title')
        print(first_video.get_attribute("aria-label"))

        videos = driver.find_elements(By.ID, 'video-title')
        print([elem.get_attribute("aria-label") for elem in videos[:10]])

        
except Exception as e:
        print(str(e))
        if input("quit?: ") == '':
                driver.quit()

### explicit wait
##try:
##        driver.get("https://youtube.com")
##        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
##finally:
##    driver.quit()
