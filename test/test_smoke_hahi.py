from time import sleep
from Framework_HAHI.src.app_logic import *
from Framework_HAHI.test_data.test_data_file import *
import pytest

def test_new_prd(setup):
    sleep(5)
    setup.get_feature()
    sleep(5)
    setup.get_flipcart_feature()
    sleep(10)

    setup.get_categories()

    sleep(10)

    #setup.get_latest_prd()
    #setup.get_discounted_mens_prd()
    #setup.get_top_offers()
    #setup.buy_this_item()
