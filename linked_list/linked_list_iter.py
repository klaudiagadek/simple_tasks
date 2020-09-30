"""Prepare linked list with iterator."""
from typing import Any

from linked_list.node import Node


class LinkedList:
    """Linked list with iterator."""
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def add_item(self, data: Any):
        self.head = Node(data) if self.head is None else Node(data, self.head)
        self.length = self.length + 1

    def __iter__(self) -> "LinkedList":
        return self

    def __next__(self) -> Any:
        if self.head is None:
            raise StopIteration
        data = self.head.data
        self.head = self.head.next_item
        self.length = self.length - 1
        return data


if __name__ == "__main__":
    linked_list = LinkedList()
    for i in range(10):
        linked_list.add_item(i)
    for item in linked_list:
        print(item)
