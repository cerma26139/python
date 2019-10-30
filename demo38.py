from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

browser = Chrome()
browser.get("https://www.python.org")

browser2 = Chrome()
browser2.get("http://www.yahoo.com.tw")

browser3 = Chrome()
browser3.get("https://www.yahoo.co.jp/")

browser4 = Chrome()
browser4.get("https://shopping.pchome.com.tw/")

browser5 = Chrome()
browser5.get("https://www.momoshop.com.tw/main/Main.jsp")
assert "Python" in browser.title
assert "Yahoo" in browser2.title
assert "Yahoo" in browser3.title
# assert "Python".lower() in browser2.title.lower()
# assert "Yahoo" in browser.title
element = browser.find_element_by_name("q")
element.clear()
element.send_keys("pytorch")
element.send_keys(Keys.RETURN)
element2 = browser2.find_element_by_name("p")
element2.clear()
element2.send_keys("pytorch")
element2.send_keys(Keys.RETURN)
element3 = browser3.find_element_by_name("p")
element3.clear()
element3.send_keys("softbank")
element3.send_keys(Keys.RETURN)
element4 = browser4.find_element_by_id("keyword")
element4.clear()
element4.send_keys("寶可夢")
element4.send_keys(Keys.RETURN)
element5 = browser5.find_element_by_id("keyword")
element5.clear()
element5.send_keys("寶可夢")
element5.send_keys(Keys.RETURN)
#browser.close()
#browser2.close()