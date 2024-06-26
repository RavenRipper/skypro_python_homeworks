from lesson_7.Swag.Shopmain import ShopMainPage
from lesson_7.Swag.Container import ShopContainer

def test_shop(firefox_browser):
    expected_total = "58.29"
    shopmain = ShopMainPage(firefox_browser)
    shopmain.registration_fields()
    shopmain.buy_issue()
    shopmain.click_issue()
    shopmain.into_container()

    container = ShopContainer(firefox_browser)
    container.checkout()
    container.info()
    container.price()
    assert expected_total in container.price()
    print(f"Итоговая сумма равна ${container.price()}")