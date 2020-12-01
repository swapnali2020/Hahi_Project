import pytest
from Framework_HAHI.test_data.test_data_file import *
from Framework_HAHI.src.app_logic import *

@pytest.fixture(scope="module")
def setup():
    obj = App_Function(browser,url,wait_time)
    return obj