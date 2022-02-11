from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


route = "https://results.digitallocker.gov.in/cbseXII2021.html"

current_role = int('start role number ex: 12345678')

candidate_name = 'CNAME'

for i in range(0,int('difference between start and end role number')):

    driver = webdriver.Chrome(executable_path= 'path_to_chromedriver')

    driver.get(route)

    sleep(0.5)

    roll_input = driver.find_element_by_xpath('/html/body/main/section/div[2]/div[1]/div[2]/div[1]/input')

    roll_input.send_keys(str(current_role + i))

    school_code_input = driver.find_element_by_xpath('/html/body/main/section/div[2]/div[1]/div[2]/div[3]/input')

    school_code_input.send_keys('<school_code>')

    search = driver.find_element_by_xpath('/html/body/main/section/div[2]/div[1]/div[2]/div[5]/div[1]/div/button')
    sleep(0.5)

    search.click()

    sleep(0.5)

    name = driver.find_element_by_id(candidate_name).text


    driver.save_screenshot(f'directory_to_save_ss_at/{str(name)}.png')



