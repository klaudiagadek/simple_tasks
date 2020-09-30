import time
from linked_list.linked_list_iter import LinkedList as IterLinkedList
from linked_list.linked_list_gen import LinkedList as GenLinkedList


if __name__ == "__main__":
    iter_linked_list = IterLinkedList()
    gen_linked_list = GenLinkedList()
    for i in range(1000):
        iter_linked_list.add_item(i)
        gen_linked_list.add_item(i)
    start_time = time.time()
    for item in iter_linked_list:
        ...
    print(f"Linked list with iter {time.time()-start_time}")
    start_time = time.time()
    for item in gen_linked_list:
        ...
    print(f"Linked list with gen {time.time()-start_time}")