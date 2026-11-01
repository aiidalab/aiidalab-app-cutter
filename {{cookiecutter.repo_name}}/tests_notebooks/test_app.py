from selenium.webdriver.common.by import By


def test_example(selenium_driver, final_screenshot):
    selenium = selenium_driver("notebooks/example.ipynb")
    selenium.find_element(By.ID, "ipython-main-app")
    selenium.find_element(By.ID, "notebook-container")
    selenium.find_element(By.CLASS_NAME, "jupyter-widgets-view")
