from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://bilibili.com")

signin_link = browser.find_element_by_class_name("name")
signin_link.click()

username_box = browser.find_element_by_class_name("item username status-box")
username_box.send_keys("1104325473@qq.com")
password_box = browser.find_element_by_class_name("item password status-box")
password_box.send_keys("cbycby")
password_box.submit()

assert "mei_nagano0924" in browser.page_source

profile_link = browser.find_element_by_class_name("nickname nickname--")
link_label = profile_link.get_attribute("innerHTML")
assert "mei_nagano0924" in link_label
