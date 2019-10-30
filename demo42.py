from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import demo41

browser4 = Chrome()
browser4.get("https://shopping.pchome.com.tw/")
element4 = browser4.find_element_by_id("keyword")
element4.clear()
element4.send_keys("寶可夢")
element4.send_keys(Keys.RETURN)
# time.sleep(1)
# container = browser4.find_element_by_id("ItemContainer")
# print(type(container))
elements = WebDriverWait(browser4,10).until(
    EC.presence_of_element_located((By.ID,"ItemContainer")))

items = elements.find_elements_by_class_name("col3f")
print(len(items))
count = 1
for item in items:
    itemName = item.find_element_by_class_name("nick")
    print(itemName.text)
    # image = item.find_element_by_class_name('prod_img')
    imageLink = item.find_element_by_tag_name('img')
    print(imageLink.get_property("src"))
    demo41.saveImage(imageLink.get_property("src"),"image\\%s.jpg"%count)
    count += 1