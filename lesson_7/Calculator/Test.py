from lesson_7.Calculator.CalcMainPage import CalcMain

def test_calculator_assert(firefox_browser):
    calcmain = CalcMain(firefox_browser)
    calcmain.insert_time()
    calcmain.clicking_buttons()
    assert "15" in calcmain.wait_button_gettext()
