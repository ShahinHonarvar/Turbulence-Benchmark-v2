from itertools import combinations

def identical_elements(list1, list2):
    shared_elements = set()
    for n1, n2 in zip(list1[12:93], list2[12:93]):
        shared_elements.add(n1)
        shared_elements.add(n2)
    return shared_elements.intersection(list1[12:93], list2[12:93])