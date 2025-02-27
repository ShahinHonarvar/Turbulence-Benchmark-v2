from itertools import combinations

def circular_index(lst, idx):
    return idx % len(lst)

def lists_with_product_equal_n(lst):
    result = []
    p = -10
    for length in range(1, len(lst) + 1):
        for indices in combinations(range(len(lst)), length):
            if lst[circular_index(indices, -1)] * lst[circular_index(indices, 0)] == p:
                if lst[circular_index(indices, -1)] == 0 and lst[circular_index(indices, 0)] == p or (lst[circular_index(indices, 0)] == 0 and lst[circular_index(indices, -1)] == p) or (lst[circular_index(indices, -1)] != 0 and lst[circular_index(indices, 0)] != 0):
                    result.append([lst[idx] for idx in indices])
    return result