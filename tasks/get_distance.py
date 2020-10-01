from typing import Set


class Node:
    def __init__(self, head: int) -> None:
        self.head = head
        self.left = None
        self.right = None

    def insert(self, data: int) -> None:
        if self.head > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    @staticmethod
    def get_path(tree: "Node", node_id: int) -> Set[int]:
        path = set()
        current = tree
        while current:
            path.add(current.head)
            if current.head == node_id:
                return path
            current = current.right if current.head < node_id else current.left
        raise Exception(f"Cannot get path for node {node_id}")


def get_distance(tree: list, node_a: int, node_b: int):
    bst = Node(tree[0])
    [bst.insert(x) for x in tree[1:]]
    path_a = Node.get_path(bst, node_a)
    path_b = Node.get_path(bst, node_b)
    common_nodes = len(path_a.intersection(path_b))
    return len(path_a) + len(path_b) - common_nodes*2


if __name__ == "__main__":
    """
    Zadanie 2 

    BST na wejsciu lista i id noda1 i noda 2. Wyznacz dytans miedzy nodem 1 a 2 
    """

    tree_data = [5, 6, 3, 1, 2, 4]
    node1 = 2
    node2 = 4

    print("BST distance: ", get_distance(tree_data, node1, node2))
    tree_data = [5, 6, 3, 1, 2, 4, 7]
    node1 = 2
    node2 = 8

    print("BST distance: ", get_distance(tree_data, node1, node2))
