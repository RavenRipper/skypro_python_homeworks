from typing import Literal
import pytest
from string_utils import StringUtils

utils = StringUtils()

"""capitalize"""
def test_capitalize():
    """POSITIVE"""
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("hello world") == "Hello world"
    assert utils.capitilize("123") == "123"
    """NEGATIVE"""
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("12345тест") == "12345тест" 

"""trim"""

def test_trim():
    """POSITIVE"""
    assert utils.capitilize( "skypro") == "Skypro"
    assert utils.capitilize( "hello world") == "Hello world"
    assert utils.capitilize( "123") == "123"
    """NEGATIVE"""
    assert utils.capitilize("") == ""

@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim(12345) == "12345"

@pytest.mark.xfail()
def test_trim_with_spaces_output():
    assert utils.trim(" SKY ") == " SKY "


"""to_list"""

@pytest.mark.parametrize('string, delimeter, result', [
    #POSITIVE 
    ("яблоко, банан, апельсин", ",", ["яблоко", "банан", "апельсин"]),
    ("1,2,3,4,5", ",", ["1","2","3","4","5"]),
    ("*@$#$", "@", ["*","@","$","#","$"]),
    # NEGATIVE
    ("", None, []),
    ("1,2,3,4,5", None, ["1","2","3","4 5"])
])
def test_to_list(string: Literal['яблоко, банан, апельсин'] | Literal['1,2,3,4,5'] | Literal['*@$#$'] | Literal[''], delimeter: None | Literal[','] | Literal['@'], result: list[str]):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result

"""contains"""

@pytest.mark.parametrize('string, symbol, result', [
    ("банан", "б", True),
    ("гвоздь","д", True),
    ("мир ","р", True),
    ("диван-кровать","-", True),
    ("145","1", True),
    ("", "", True),
    ("Москва","м", False),
    ("привет","з", False),
    ("кот","№", False),
    ("","з", False),
    ("12345","h", False),
])
def test_contains(string: Literal['банан'] | Literal['гвоздь'] | Literal['мир '] | Literal['диван-кровать'] | Literal['145'] | Literal[''] | Literal['Москва'] | Literal['привет'] | Literal['кот'] | Literal['12345'], symbol: Literal['б'] | Literal['д'] | Literal['р'] | Literal['-'] | Literal['1'] | Literal[''] | Literal['м'] | Literal['з'] | Literal['№'] | Literal['h'], result: bool):
    res = utils.contains(string, symbol)
    assert res == result

""""delete_symbol"""

@pytest.mark.parametrize('string, symbol, result', [
    ("корень", "к", "орень"),
    ("Женя", "н", "Жея"),
    ("Море", "М", "оре"),
    ("123", "1", "23"),
    ("Красная Площадь", " ", "КраснаяПлощадь"),

    ("ножик", "з", "ножик"),
    ("", "", ""),
    ("", "с", ""),
    ("кофе", "", "кофе"),
    ("зелень", "", "зелень"),
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


"""starts_with"""


@pytest.mark.parametrize('string, symbol, result', [
    ("светофор", "с", True),
    ("", "", True),
    ("Москва", "М", True),
    ("Film", "F", True),
    ("Мира-Зина", "М", True),
    ("123", "1", True),

    ("Ваня", "в", False),
    ("мир", "М", False),
    ("", "@", False),
    ("плащь", "ж", False),
    ("зверь", "н", False),
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


"""end_with"""


@pytest.mark.parametrize('string, symbol, result', [
    ("Мария", "я", True),
    ("ТОРТИК", "К", True),
    ("", "", True),
    ("собака", "", True),
    ("67", "7", True),
    ("ONE-TWo", "o", True),
    ("Петр1", "1", True),
    ("баобаб", "Б", True),

    ("природа", "л", False),
    ("тигр", "с", False),
    ("дверь", "Ь", False),
    ("", "*", ),
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result



"""is_empty"""


@pytest.mark.parametrize('string, result', [
    ("", True),
    (" ", True),
    ("  ", True),

    ("не пусто", False),
    (" не пусто с пробелом", False),
    ("345", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result



"""list_to_string"""

@pytest.mark.parametrize('lst, joiner, result', [
    (["s", "o", "s"], ",", "s,o,s"),
    ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
    (["Первый", "Второй"], "-", "Первый-Второй"),
    (["Первый", "Второй"], "Середина", "ПервыйСерединаВторой"),
    (["в", "у", "з"], "", "вуз"),

    ([], None, ""),
    ([], ",", ""),
    ([], "кот", ""),
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result