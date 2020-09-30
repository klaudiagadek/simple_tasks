from collections import defaultdict


def count_words_with_filter(data: str, filter_data: list):
    data = data.lower()
    filter_list = [x.lower() for x in filter_data]
    filter_list.append("")
    for x in ["\n", ",", "." "!", "--"]:
        data = data.replace(x, " ")

    words_count = defaultdict(int)
    for word in data.split(" "):
        if word in filter_list:
            continue
        words_count[word] += 1
    for word in [w for w, _ in sorted(words_count.items(), key=lambda x: x[1], reverse=True)]:
        print(word)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    @staticmethod
    def get_path(thr, node_id):
        path = list()
        current = thr
        while True:
            path.append(current.data)
            if current.data == node_id:
                break
            else:
                if current.data < node_id:
                    current = current.right
                else:
                    current = current.left
        return path


def get_distance(three: list, node_a: int, node_b: int):
    bst = Node(three[0])
    for x in three[1:]:
        bst.insert(x)
    path_a = Node.get_path(bst, node_a)
    path_b = Node.get_path(bst, node_b)

    common_nodes = 0
    for i in range(min(len(path_a), len(path_b))):
        if path_a[i] == path_b[i]:
            common_nodes += 1
        else:
            break

    return len(path_a) + len(path_b) - common_nodes*2


if __name__ == "__main__":
    """
    Zadanie 1

    masz podany dlugi tests z nowymi liniami bialymi znakiami itp i liste slow zabronionych.
    Wypisz liste zawiarajaco slowa ktore sie najczesciej powtarzaja (wykluczajac zabronione).
    """

    Text = """
    bands which have connected them with another, and to assume among the
    powers of the earth, the separate and equal station to which the Laws
    of Nature and of Nature's God entitle them, a decent respect to the
    opinions of mankind requires that they should declare the causes which
    impel them to the separation.  We hold these truths to be
    self-evident, that all men are created equal, that they are endowed by
    their Creator with certain unalienable Rights, that among these are
    Life, Liberty and the pursuit of Happiness.--That to secure these
    rights, Governments are instituted among Men, deriving their just
    powers from the consent of the governed, --That whenever any Form of
    Government becomes destructive of these ends, it is the Right of the
    People to alter or to abolish it, and to institute new Government,
    laying its foundation on such principles and organizing its powers in
    such form, as to them shall seem most likely to effect their Safety
    and Happiness. """

    filters = ["the", "with"]

    count_words_with_filter(Text, filters)

    """
    Zadanie 2 

    BST na wejsciu lista i id noda1 i noda 2. Wyznacz dytans miedzy nodem 1 a 2 
    """

    tree_data = [5, 6, 3, 1, 2, 4]
    node1 = 2
    node2 = 4

    print("BST distance: ", get_distance(tree_data, node1, node2))
