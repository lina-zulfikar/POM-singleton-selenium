from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.shopeeconfig_manager import ConfigManager
import time
import random

class AddEsai(BasePage):
    TAMBAH_PILIHAN_ESAI = (By.XPATH, "//p[normalize-space()='Tambah Esai']")
    SIMPAN = (By.XPATH, '/html/body/div/main/div/form/div[4]/div/button')
    TAMBAH_PERTANYAAN = (By.ID, 'cke_1_contents')
    PILIH_TINGKAT_SOAL = (By.XPATH, "//*[@id='question_type']")
    KUNCI_JAWABAN = (By.ID, 'cke_2_contents')
    ELEMEN = (By.XPATH, '/html/body/div/main/div/div[1]/a')

    def __init__(self, driver):
        super().__init__(driver)
        self.config = ConfigManager.get_config()
    
    def open_menu_tambah_esai(self):
        open_esai = self.driver.find_element(*self.TAMBAH_PILIHAN_ESAI)
        open_esai.click()
        time.sleep(3)

    def isi_element(self, element_id, nilai):
        # Temukan element yang ingin discroll
        target_element = self.driver.find_element(By.ID, element_id)

        # Scroll ke element
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
        time.sleep(1)

        editorFrame = self.driver.find_element(By.CSS_SELECTOR,  f"#{element_id} > iframe")
        self.driver.switch_to.frame(editorFrame)
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.click()
        body.send_keys(nilai)
        self.driver.switch_to.default_content()

    def tambah_soal(self, text_id, isi_soal):
        self.isi_element(text_id, isi_soal)
        time.sleep(3)

    def kunci_jawaban(self, text_id, isi_kuncijawaban):
        self.isi_element(text_id, isi_kuncijawaban)
        time.sleep(3)

    def pilih_tingkat_soal(self):
        element = self.driver.find_element(*self.PILIH_TINGKAT_SOAL)
        dropdown = Select(element)

        # Pilih secara acak antara "Pusat" dan "Daerah"
        pilihan_acak = random.choice(["Pusat", "Daerah"])
        dropdown.select_by_visible_text(pilihan_acak)
        time.sleep(3)

    # def simpan_soal(self):
    #     target_element = self.driver.find_element(By.XPATH, "//button[normalize-space()='Simpan']")
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
    #     element = self.driver.find_element(*self.SIMPAN)
    #     WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Simpan']")))
    #     element.click()
    #     WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(*self.ELEMEN))

    def simpan_soal(self):
        target_element = self.driver.find_element(By.XPATH, "//button[normalize-space()='Simpan']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
        time.sleep(1)  # Tambahkan jeda waktu setelah di-scroll ke dalam pandangan
        
        # Tunggu hingga elemen bisa diklik
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(target_element))
        
        # Klik elemen
        target_element.click()
        
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.ELEMEN))


####aksi#####
    def add_esai(self):
        self.open_menu_tambah_esai()
        self.tambah_soal('cke_1_contents', 'Tambah soal ESAI singleton dan page object model')
        self.pilih_tingkat_soal()
        self.kunci_jawaban('cke_2_contents', 'kunci jawaban ESAI')
        self.simpan_soal()

    