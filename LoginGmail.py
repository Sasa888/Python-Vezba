from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def login():
	browser = webdriver.Firefox()
	browser.get('https://accounts.google.com/ServiceLogin/signinchooser?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

	emailElem = browser.find_element_by_class_name('whsOnd')
	emailElem.send_keys('')
	nextButton = browser.find_element_by_class_name('CwaK9')
	nextButton.click()

	time.sleep(5)

	passwordElem = browser.find_element_by_class_name('whsOnd')
	passwordElem.send_keys('')
	nextButton = browser.find_element_by_class_name('CwaK9')
	nextButton.click()

login()