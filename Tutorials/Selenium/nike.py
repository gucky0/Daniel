# relevant imports and initialization
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome('chromedriver')

url = "https://www.nike.com/sg/launch?s=upcoming"
shoe = "womens-dunk-low-disrupt-2-phantom-university-blue"
url = f"https://www.nike.com/sg/launch/t/{shoe}"
driver.get(url)
driver.implicitly_wait(3)

##shoe = 'aria-label="Women\'s Dunk Low Disrupt 2"'
##element = driver.find_element(By.CSS_SELECTOR, f'a[{shoe}]').click()

find name and 10AM
need a few cards

##beforehand put in billing address

# select shoe size
li data-qa="size-available" text: US 9 // button data-qa="size-dropdown" text: ?
# enter raffle
button type="button"

#card number, expiry and cvv
id="cardNumber-input"
id="cardExpiry-input"
id="cardCvc-input"

# agree to TNC
class="container isChecked"
span class="checkmark"

# buy
button class="button-submit"

##________________________
##hover then click on element
WebDriverWait(driver,15).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src='https://unodc.shinyapps.io/GSH_App/']")))
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'ul.nav.navbar-nav a[data-value="National Data"]'))).click()
##try:
##        # open url in browser
##        url = "https://youtube.com"
##        driver.get(url)
##        driver.implicitly_wait(3)
##
##        # finding by ID
##        element_name = driver.find_element(By.ID, 'video-title-link')
##        element_name.click()
##
##        # combining the two lines of code
##        # comments
##        driver.find_element(By.ID, 'guide-icon').click()
##
##        # finding by CSS
##        driver.find_element(By.CSS_SELECTOR, 'yt-icon[id="guide-icon"]').click()
##
##        # finding multiple elements
##        elements = driver.find_elements(By.XPATH, '//*[@id="guide-icon"]')
##        elements[1].click()
##        
##        # finding by NAME
##        field = driver.find_element(By.NAME, 'search_query')
##        
##        field.send_keys("truck")
##        print(field.get_attribute("value"))
##        field.clear()
##        field.send_keys("spiderman")
##        field.submit()
##
##        first_video = driver.find_element(By.ID, 'video-title')
##        print(first_video.get_attribute("aria-label"))
##
##        videos = driver.find_elements(By.ID, 'video-title')
##        print([elem.get_attribute("aria-label") for elem in videos[:10]])
##
##        
##except Exception as e:
##        print(str(e))
##        if input("quit?: ") == '':
##                driver.quit()
##
##### explicit wait
####try:
####        driver.get("https://youtube.com")
####        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
####finally:
####    driver.quit()
