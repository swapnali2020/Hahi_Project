from selenium.webdriver.common.by import By
from Framework_HAHI.test_data.test_data_file import *

XPATH = By.XPATH
LINK_TEXT = By.LINK_TEXT
ID = By.ID
NAME = By.NAME
CSS_SELECTOR = By.CSS_SELECTOR
CHECK_FEATR = (XPATH, "//body/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/a[1]")
#FLIPCART_FEATR = (XPATH, "//body/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[2]/code[1]/a[1]/div[1]/div[1]")
FLIPCART_FEATR = (XPATH, "//div[@class='rh-hover-tax-head font120 fontbold'][contains(.,'Flipkart')]")
CATEGORIES = (XPATH, "//a[@href='https://www.hahi.in/dealstore/flipkart/?dealcategory=computer-laptop'][contains(.,'Computer & Laptop')]")
LATEST_PRD = (XPATH, "//h4[contains(text(), 'Latest Product & Deal')]")
DISCOUNT_PRD = (XPATH, "//a[@href='https://www.hahi.in/product/discounted-mens-shirt-sale-hurry-hurry-limited-stock/'])[2]")
TOP_OFFERS = (XPATH, "//div[contains(text(), 'Top offers')]")
BUY_ITEM = (XPATH, "//body/div[1]/div[3]/div[1]/aside[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/a[1]")