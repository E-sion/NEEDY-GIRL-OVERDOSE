from selenium import webdriver

# options = Options()
# options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()  # this will open a Chrome browser
driver.get("https://faucet.openkey.cloud/")  # this will go to the web page
input_element = driver.find_element_by_id("text")  # this will find the input element by id
input_element.send_keys(str(input("请输入邮箱地址")))  # this will enter "Hello" in the input box
yes_element = driver.find_element_by_id("checkbox")
yes_element.click()
button_element = driver.find_element_by_id("button.Home_button__main__SJpCH")  # this will find the button element by id
button_element.click()  # this will click on the button

print("a  ")
