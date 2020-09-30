"""How do you find the middle element of a singly linked list in one pass?"""
from typing import Any

from linked_list.linked_list_iter import LinkedList


def get_middle_of_linked_list(linked_list: LinkedList) -> Any:
    """
    Find the middle element of a singly linked list in one pass.
    :param linked_list:
    :return: middle value or None
    """
    value = None
    if linked_list.length % 2 == 0:
        print("This linked list doesn't have middle value.")
        return value
    for item in range(int((linked_list.length-1)/2)):
        value = next(linked_list)
    print(f"Middle of a liked list {value}.")
    return value


if __name__ == "__main__":
    linked_list = LinkedList()
    for i in range(11):
        linked_list.add_item(i)
    get_middle_of_linked_list(linked_list)
    for i in range(10):
        linked_list.add_item(i)
    get_middle_of_linked_list(linked_list)
