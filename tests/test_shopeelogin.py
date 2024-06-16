import pytest
from utils.shopeedriver_manager import DriverManager
from pages.shopeelogin_page import LoginPage
from pages.addMultipleChoice_page import AddMultipleChoice
from pages.addEsai import AddEsai
from pages.addStudyKasus import AddStudyKasus

@pytest.fixture(scope="module")
def driver():
    driver_manager = DriverManager()
    driver = driver_manager.get_driver()
    yield driver
    driver_manager.close_driver()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.login()
    # Tambahkan asersi di sini untuk memvalidasi proses login
    # Contoh: assert "dashboard" in driver.current_url

# def test_pilihanganda(driver):
#     pilihan_ganda = AddMultipleChoice(driver)
#     pilihan_ganda.add_multiplechoice()

# def test_essay(driver):
#     esai = AddEsai(driver)
#     esai.add_esai()

def test_studi_kasus(driver):
    studikasus = AddStudyKasus(driver)
    studikasus.add_studykasus()
    