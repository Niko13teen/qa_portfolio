#Triangle automation test
#URL: https://playground.learnqa.ru/puzzle/triangle
#Browser: Chrome
#WebDriver for Chrome version: ChromeDriver 95.0.4638.69


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://playground.learnqa.ru/puzzle/triangle')
el_a = driver.find_element(By.CLASS_NAME, 'js_a')
el_b = driver.find_element(By.CLASS_NAME, 'js_b')
el_c = driver.find_element(By.CLASS_NAME, 'js_c')
btn = driver.find_element(By.XPATH, '//button[text()="Показать"]')

def field_validation_test_0():
    el_a.send_keys('')
    el_b.send_keys('')
    el_c.send_keys('')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_1():
    el_a.send_keys('60')
    el_b.send_keys('')
    el_c.send_keys('')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_2():
    el_a.send_keys('')
    el_b.send_keys('60')
    el_c.send_keys('')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_3():
    el_a.send_keys('')
    el_b.send_keys('')
    el_c.send_keys('60')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_4():
    el_a.send_keys('60')
    el_b.send_keys('60')
    el_c.send_keys('')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_5():
    el_a.send_keys('')
    el_b.send_keys('60')
    el_c.send_keys('60')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_6():
    el_a.send_keys('60')
    el_b.send_keys('')
    el_c.send_keys('60')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_7():
    el_a.send_keys('60')
    el_b.send_keys('60')
    el_c.send_keys('60')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_8():
    el_a.send_keys('0')
    el_b.send_keys('0')
    el_c.send_keys('0')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_9():
    el_a.send_keys('60')
    el_b.send_keys('90')
    el_c.send_keys('120')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_10():
    el_a.send_keys('10')
    el_b.send_keys('9')
    el_c.send_keys('5')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_11():
    el_a.send_keys('21')
    el_b.send_keys('28')
    el_c.send_keys('35')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_12():
    el_a.send_keys('60')
    el_b.send_keys('30')
    el_c.send_keys('60')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_13():
    el_a.send_keys('1.2')
    el_b.send_keys('1.2')
    el_c.send_keys('1.2')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_14():
    el_a.send_keys('1234567890')
    el_b.send_keys('1234567890')
    el_c.send_keys('1234567890')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_15():
    el_a.send_keys('qwerty')
    el_b.send_keys('qwerty')
    el_c.send_keys('qwerty')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_16():
    el_a.send_keys('<script>alert(123)</script>')
    el_b.send_keys('<script>alert(123)</script>')
    el_c.send_keys('<script>alert(123)</script>')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_17():
    el_a.send_keys('SELECT')
    el_b.send_keys('WHERE')
    el_c.send_keys('SELECT')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_18():
    el_a.send_keys('5')
    el_b.send_keys('10')
    el_c.send_keys('5')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()

def field_validation_test_19():
    btn.click()

def field_validation_test_20():
    el_a.send_keys('<SCRIPT>alert(123)</SCRIPT>')
    el_b.send_keys('<SCRIPT>alert(123)</SCRIPT>')
    el_c.send_keys('<SCRIPT>alert(123)</SCRIPT>')
    btn.click()
    sleep(2)
    el_a.clear()
    el_b.clear()
    el_c.clear()


field_validation_test_0()
field_validation_test_1()
field_validation_test_2()
field_validation_test_3()
field_validation_test_4()
field_validation_test_5()
field_validation_test_6()
field_validation_test_7()
field_validation_test_8()
field_validation_test_9()
field_validation_test_10()
field_validation_test_11()
field_validation_test_12()
field_validation_test_13()
field_validation_test_14()
field_validation_test_15()
field_validation_test_16()
field_validation_test_17()
field_validation_test_18()
field_validation_test_19()
field_validation_test_20()