from pages.swag_labs import SwagLabs


icon_swag_labs = "div.login_logo"
icon_username = "#user-name"
icon_password = "#password"



def test_find_icon_swag_labs(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    assert swag_labs.exist_icon(name_locator=icon_swag_labs)

def test_find_icon_username(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    assert swag_labs.exist_icon(name_locator=icon_username)

def test_find_icon_password(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    assert swag_labs.exist_icon(name_locator=icon_password)



