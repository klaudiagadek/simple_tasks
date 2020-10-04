from tasks.simple_tasks import check_if_palindrome, remove_values, move_item, revers_number, reverse_string,\
    get_fibonacci, get_dict, zip_strings, get_subsets, prepare_set_int


def test_check_if_palindrome():
    assert check_if_palindrome([1, 2, 1])


def test_remove_values():
    list_a = [1, 2, 3, 4, 5, 6, 7, 89, 2, 54, 2, 5, 2, 2]
    remove_values(list_a, 2)
    assert list_a == [1, 3, 4, 5, 6, 7, 89, 54, 5]


def test_move_item():
    list_a = [1, 2, 3, 4, 5, 6, 7, 89, 2, 54, 2, 5, 2, 2]
    move_item(list_a, 2)
    assert list_a == [1, 2, 4, 5, 6, 7, 89, 2, 54, 2, 5, 2, 2, 3]


def test_revers_number():
    assert revers_number(12345) == 54321


def test_reverse_string():
    assert reverse_string("How are you?") == "you? are How"


def test_get_fibonacci():
    assert get_fibonacci(2) == 1
    assert get_fibonacci(20) == 6765


def test_get_dict():
    string = "{'A':13, 'B':14, 'C':15}"
    assert get_dict(string) == {'A': '13', 'B': '14', 'C': '15'}


def test_zip_str():
    assert zip_strings("abc", "def") == "adbecf"


def test_get_subsets():
    assert get_subsets("abcd") == {'a', 'b', 'bcd', 'abcd', 'c', 'cd', 'd', 'bc', 'abc', 'ab'}
    assert get_subsets("abc") == {'abc', 'c', 'a', 'bc', 'ab', 'b'}


def test_prepare_set_int():
    assert prepare_set_int([1, 2, 3], 1000) == [1, 2, 3, 11, 12, 13, 21, 22, 23, 31, 32, 33, 111, 112, 113, 121, 122,
                                                123, 131, 132, 133, 211, 212, 213, 221, 222, 223, 231, 232, 233, 311,
                                                312, 313, 321, 322, 323, 331, 332, 333]
    assert prepare_set_int([1, 2], 50) == [1, 2, 11, 12, 21, 22]
    assert prepare_set_int([1, 2, 3, 4, 5], 100) == [1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33,
                                                     34, 35, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55]
