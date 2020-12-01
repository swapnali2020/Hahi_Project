from Framework_HAHI.test_data.test_data_file import *
from Framework_HAHI.Browser_Action.browser_action import *
from Framework_HAHI.src.locators import *

class App_Function(BrowserAction):
    def __init__(self,browser,url,wait_time):
        self.url = url
        super().__init__(browser,wait_time)
        self.launch_app()

    def launch_app(self):
        self.spdriver.get(self.url)





#Get Latest Product
    def get_feature(self):
        self.click_element(CHECK_FEATR)

    def get_flipcart_feature(self):
        self.click_element(FLIPCART_FEATR)

    def get_categories(self):
        self.click_element(CATEGORIES)

    def get_latest_prd(self):
        (self.get_element_text(LATEST_PRD))

    def get_discounted_mens_prd(self):
        self.click_element(DISCOUNT_PRD)

    def get_top_offers(self):
        self.click_element(TOP_OFFERS)


    def buy_this_item(self):
        self.click_element(BUY_ITEM)

