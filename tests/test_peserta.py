import pytest
from utils.shopeedriver_manager import DriverManager
from pages.pesertalogin_page import LoginPage
from pages.simulasiujian_page import SimulasiUjian

@pytest.fixture(scope="module")
def driver():
    driver_manager = DriverManager()
    driver = driver_manager.get_driver()
    yield driver
    driver_manager.close_driver()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.login()

def test_kerjakansimulasi(driver):
    simulasi_ujian = SimulasiUjian(driver)
    simulasi_ujian.kerjakan_simulasi()