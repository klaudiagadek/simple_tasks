def check_if_palindrome(list_a):
    return list_a == list_a[::-1]


def remove_values(my_list, value_to_remove):
    """Jak usunac wszystkie elementy z listy liczb calkowitych, ktore odpowiadaja podanej wartosci?"""
    while value_to_remove in my_list:
        my_list.remove(value_to_remove)


def move_item(my_list: list, item_to_move):
    """Jak usunąć n-ty element od końca listy?"""
    item = my_list.pop(item_to_move)
    my_list.append(item)


if __name__ == "__main__":
    print(check_if_palindrome([1, 2, 1]))
    list_a = [1, 2, 3, 4, 5, 6, 7, 89, 2, 54, 2, 5, 2, 2]
    remove_values(list_a, 2)
    print(list_a)
    list_a = [1, 2, 3, 4, 5, 6, 7, 89, 2, 54, 2, 5, 2, 2]
    move_item(list_a, 2)
    print(list_a)
