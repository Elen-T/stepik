#Задание на execute_script
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    inp = browser.find_element_by_id("answer")
    inp.send_keys(y)

    option = browser.find_element_by_id("robotCheckbox")
    option.click()

    option1 = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

