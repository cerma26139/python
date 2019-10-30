from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
browser = Chrome()
browser.get("https://shopping.pchome.com.tw/")

element = browser.find_element_by_id("keyword")
element.clear()
element.send_keys("寶可夢")
element.send_keys(Keys.RETURN)

time.sleep(3)

element1 = browser.find_element_by_id("MinPrice")
element1.clear()
element1.send_keys("0",Keys.TAB,"555")
element1.send_keys(Keys.RETURN)





