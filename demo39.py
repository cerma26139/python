#Scrapy
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")

browser = Chrome(options=chrome_options)

browser.get("https://www.python.org")
element = browser.find_element_by_name("q")
element.clear()
element.send_keys("tensorflow")
element.send_keys(Keys.RETURN)

result = browser.find_elements_by_css_selector(".list-recent-events.menu")
allItems = result[0].find_elements_by_tag_name("li")
for r in allItems:
    linkTitle = r.find_elements_by_tag_name("a")
    print(linkTitle[0].text)
    contents = r.find_elements_by_tag_name("p")
    for c in contents:
        print(c.text)

browser.close()