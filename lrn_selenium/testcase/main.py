import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r"/Users/np/Z_Folder/web-driver/geckodriver")
        self.driver.get("https://www.python.org")

    def test_example(self): #function name should start with test else it wont work
        print("test")
        assert True

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


'''note
setup -> test case 1 -> teardown ->setup -> test case 2 -> teardown
it repeats
'''