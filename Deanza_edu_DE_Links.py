# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class ALinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/"
        self.verificationErrors = []
    
    def test_a_links(self):
        link_title = {
            "Office of Equity, Social Justice and Multicultural Education" : "De Anza College :: Office of Equity :: Home",
            "Donors" : "De Anza College :: Friends :: Home",
            "Dropping Classes" : "De Anza College :: Registration :: Adding and Dropping Classes",
            "ETS" : "Educational Technology Services : Your District IT Department",
            "E-mail" : "De Anza College :: Current Students :: You Need a Current Email Address",
            "Eco Pass" : "De Anza College :: Eco Pass :: Overview",
            "Economics Department" : "De Anza College :: Economics :: Home",
            "Educational Diagnostic Center" : "De Anza College :: Educational Diagnostic Center :: Home",
            "Equity, Social Justice and Multicultural Education" : "De Anza College :: Office of Equity :: Home",
            }
        
        driver = self.driver
        driver.get(self.base_url + "directory/dir-az.html")

        for link in link_title:
            title = link_title[link]
            driver.find_element_by_link_text(link).click()
            try: self.assertEqual(title, driver.title)
            except AssertionError as e: self.verificationErrors.append(str(e))
            driver.back()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
