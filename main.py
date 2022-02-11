from helpers import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys



result_dict = {}
role = int('start role number ex: 12345678')

for j in range(0,int('difference between start and end role number')):
    route = "https://results.digitallocker.gov.in/cbseXII2021.html"
    driver = webdriver.Chrome(executable_path= '/Users/Afraz/Desktop/Codes/JoeBot/chromedriver 3')

    driver.get(route)

    sleep(0.5)

    roll_input = driver.find_element_by_xpath('/html/body/main/section/div[2]/div[1]/div[2]/div[1]/input')

    roll_input.send_keys(role+j)

    school_code_input = driver.find_element_by_xpath('/html/body/main/section/div[2]/div[1]/div[2]/div[3]/input')

    school_code_input.send_keys('<school_code>')

    search = driver.find_element_by_xpath('/html/body/main/section/div[2]/div[1]/div[2]/div[5]/div[1]/div/button')
    sleep(0.5)

    search.click()

    sleep(0.5)


    cname = driver.find_element_by_id('CNAME').text
    i = 1
    temp_dict = {}

    while i<6:
        subject = driver.find_element_by_id(f'SNAME{i}').text
        marks_theory = driver.find_element_by_id(f'MRK{i}1').text
        marks_prac = driver.find_element_by_id(f'MRK{i}2').text
        marks_total = driver.find_element_by_id(f'MRK{i}3').text
        grade = driver.find_element_by_id(f'GR{i}').text
        i+=1
        
        temp_dict[subject] = {
            "theory":marks_theory,
            "prac":marks_prac,
            "total":marks_total,
            'grade': grade
        }
    
    result_dict[cname] = temp_dict
    append_json(result_dict, 'json_file_name_to_save_result')
