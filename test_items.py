import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_exist(browser):
    browser.get(link)
    time.sleep(30)
    btn = browser.find_elements_by_css_selector("#add_to_basket_form>button")
    assert len(btn)>0 , 'There is no "Add to basket" button'