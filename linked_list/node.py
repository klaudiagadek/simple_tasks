"""Base node class."""
from typing import Any, Optional


class Node:
    """Base node class."""
    def __init__(self, data: Any, next_item: Optional[Any] = None) -> None:
        self.data = data
        self.next_item = next_item
