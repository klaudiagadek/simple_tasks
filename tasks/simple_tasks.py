import copy
from typing import List, Any, Dict, Set


def check_if_palindrome(string: str) -> bool:
    """
    Check if string is palindrome
    :param string: string to check
    :return: True if str is palindrome
    """
    return string == string[::-1]


def remove_values(my_list: List[int], value_to_remove: int) -> None:
    """Jak usunac wszystkie elementy z listy liczb calkowitych, ktore odpowiadaja podanej wartosci?"""
    while value_to_remove in my_list:
        my_list.remove(value_to_remove)


def move_item(my_list: list, item_to_move: Any) -> None:
    """Jak usunąć n-ty element od końca listy?"""
    item = my_list.pop(item_to_move)
    my_list.append(item)


def revers_number(number: int) -> int:
    """Code to reverse a number."""
    return int(str(number)[::-1])


def reverse_string(string: str) -> str:
    """Write a function that takes some string as an input and reverse it. (e.g. 'How are you?" -> "you? are How")"""
    splited = string.split()
    return " ".join(splited[::-1])


FIB_CACHE = {0: 0, 1: 1}


def get_fibonacci(number: int) -> int:
    """Write a method to output the Fibonacci sequence."""
    if number not in FIB_CACHE:
        FIB_CACHE[number] = get_fibonacci(number - 2) + get_fibonacci(number - 1)
    return FIB_CACHE[number]


def get_dict(string: str) -> Dict[str, int]:
    """create a dictionary from a string"""
    splited = string[1:-1].split(", ")
    my_dict = {}
    for i in splited:
        key, value = i.split(":")
        if key[0] == "'" and key[-1] == "'":
            key = key[1:-1]
        if value[0] == "'" and value[-1] == "'":
            value = value[1:-1]
        my_dict[key] = value
    return my_dict


def zip_strings(string: str, string_b: str) -> str:
    """Code to merge the string alternatively
    s1 = abc
    s2 = def
    output s3 = adbecf"""
    return "".join(i + j for i, j in zip(string, string_b))


def get_subsets(string: str) -> Set:
    """Finding all possible subsets of String."""
    strings = set()
    str_len = len(string) + 1
    [strings.add(string[start:stop]) for start in range(str_len) for stop in range(str_len) if stop > start]
    return strings


def prepare_set_int(integers: List[int], max_int: int) -> List[int]:
    """Hardest Coding question asked to me in the entire process.
    Given an Array of digits 1-9, 0 excluding and a number N
    Find how many numbers can be formed such that it is less than or equals to N. Digits can be repeated.
    Eg: Arr - {1,4,9}
            N - 10
    Ans - 3 since (1, 4, 9)


    Arr - {1,3,4,5}
    N - 100
    Ans - (1,3,4,5,11,13,14,15,33 ............. )
    """
    all_numbers = copy.copy(integers)
    temp_numbers = copy.copy(integers)
    while True:
        temp_set_to_add = []
        for first in temp_numbers:
            for second in integers:
                new_integer = int(str(first) + str(second))
                if 0 < new_integer < max_int:
                    temp_set_to_add.append(new_integer)
                else:
                    all_numbers.extend(temp_set_to_add)
                    return all_numbers
        all_numbers.extend(temp_set_to_add)
        temp_numbers = temp_set_to_add
