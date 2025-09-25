from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class DemoImplicitWait():
    def demo_imp_wait(self):
        driver: WebDriver = webdriver.Chrome()

        driver.implicitly_wait(10)
        driver.get("https://app.createsmart.io/login")
        driver.find_element(By.XPATH, "//input[@id='mui-4']").send_keys("omar.moazzam@bssuniversal.com")
        driver.find_element(By.XPATH, "//input[@id='mui-5']").send_keys("Omar@085")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.find_element(By.XPATH, "//*[@id='67a1e306d6d46c42d36c7cc5']/div[3]/div/a[1]/button").click()
        driver.find_element(By.XPATH, "//*[@id='simple-tabpanel-0']/div/div/div/div[1]/div").click()
        driver.find_element(By.XPATH, "//*[@id='confirmDeleteButton']").click()
        driver.find_element(By.XPATH, "//img[@class='cs-image editable']").click()
        driver.find_element(By.XPATH,
                            "//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'upload')]").click()
        driver.find_element(By.XPATH, "//td//img[@alt='duphaston-logo.png']").click()
        driver.find_element(By.XPATH, "//button[text()='Apply']").click()
        driver.find_element(By.XPATH, "//*[@id='propertise_container']/div[3]/div[1]").click()
        driver.find_element(By.XPATH, "//input[@class='PrivateSwitchBase-input css-1m9pwf3' and @checked]").click()
        driver.find_element(By.XPATH, "//*[@id='mui-component-select-action']").click()
        site_map = driver.find_element(By.XPATH, "//li[text()='Site Map']")
        site_map.click()

        #driver.find_element(By.XPATH, "//button[text()='Save All Changes']").click()
        #driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[1]/div/ul/div[1]/li/a").click()

impwait = DemoImplicitWait()
impwait.demo_imp_wait()
