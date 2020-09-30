"""Prepare linked list with generator."""
from typing import Any

from linked_list.node import Node


class LinkedList:
    """Linked list with generator."""
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def add_item(self, data: Any):
        self.head = Node(data) if self.head is None else Node(data, self.head)
        self.length = self.length + 1

    def __iter__(self) -> Any:
        while self.head is not None:
            yield self.head.data
            self.head = self.head.next_item
            self.length = self.length - 1


if __name__ == "__main__":
    linked_list = LinkedList()
    for i in range(10):
        linked_list.add_item(i)
    for item in linked_list:
        print(item)
