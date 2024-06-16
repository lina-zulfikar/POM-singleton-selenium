from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.shopeeconfig_manager import ConfigManager
import time
import random

class AddMultipleChoice(BasePage):
    TAMBAH_PILIHAN_GANDA = (By.XPATH, "//p[normalize-space()='Tambah Pilihan Ganda']")
    TAMBAH_PERTANYAAN = (By.ID, 'cke_1_contents')
    PILIH_TINGKAT_SOAL = (By.XPATH, '/html/body/div[1]/main/div/form/div[2]/select')
    TAMBAH_JAWABAN_A = (By.ID, 'cke_2_contents')
    TAMBAH_JAWABAN_B = (By.ID, 'cke_3_contents')
    TAMBAH_JAWABAN_C = (By.ID, 'cke_4_contents')
    TAMBAH_JAWABAN_D = (By.ID, 'cke_5_contents')
    KUNCI_JAWABAN = (By.ID, 'correct_answer')
    PENJELASAN = (By.ID, 'cke_6_contents')
    SIMPAN = (By.XPATH, "//button[normalize-space()='Simpan']")
    ELEMEN = (By.XPATH, '/html/body/div/main/div/div[1]/a')

    def __init__(self, driver):
        super().__init__(driver)
        self.config = ConfigManager.get_config()
    
    def open_menu_tambah_pilgan(self):
        
        open_pilihanganda = self.driver.find_element(*self.TAMBAH_PILIHAN_GANDA)
        open_pilihanganda.click()
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

    def pilih_tingkat_soal(self):
        element = self.driver.find_element(*self.PILIH_TINGKAT_SOAL)
        dropdown = Select(element)

        # Pilih secara acak antara "Pusat" dan "Daerah"
        pilihan_acak = random.choice(["Pusat", "Daerah"])
        dropdown.select_by_visible_text(pilihan_acak)
        time.sleep(3)

    def tambah_jawaban(self, jawaban_id, jawaban):
        self.isi_element(jawaban_id, jawaban)
        time.sleep(3)

    def jawaban_benar(self):
        # Temukan element yang ingin discroll
        target_element = self.driver.find_element(By.XPATH, "//label[normalize-space()='Penjelasan']")

        # Scroll ke element
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
        

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='correct_answer']")))
        element = self.driver.find_element(*self.KUNCI_JAWABAN)
        dropdown = Select(element)

        # Pilih secara acak
        pilihan_acak = random.choice(['A', 'B', 'C', 'D'])
        dropdown.select_by_visible_text(pilihan_acak)

    def simpan_soal(self):
        element = self.driver.find_element(*self.SIMPAN)
        element.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(*self.ELEMEN))



####aksi#####
    def add_multiplechoice(self):
        self.open_menu_tambah_pilgan()
        self.tambah_soal('cke_1_contents', 'Tambah soal singleton dan page object model')
        self.pilih_tingkat_soal()
        self.tambah_jawaban('cke_2_contents', 'Ini jawaban A')
        self.tambah_jawaban('cke_3_contents', 'Ini jawaban B')
        self.tambah_jawaban('cke_4_contents', 'Ini jawaban C')
        self.tambah_jawaban('cke_5_contents', 'Ini jawaban D')
        self.jawaban_benar()
        # self.simpan_soal()
    



    