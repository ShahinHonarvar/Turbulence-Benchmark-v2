from itertools import product

def lists_with_product_equal_n(lst):

    def is_circular(seq, n):
        return seq[n:] + seq[:n]
    sublists = []
    for size in range(1, len(lst) + 1):
        for indices in product(range(len(lst)), repeat=size):
            if 0 in lst[indices]:
                circular_sublist = is_circular(lst, sum(indices) % len(lst))
                if all((a == 0 for a in circular_sublist[indices])):
                    sublists.append(circular_sublist[indices])
    return sublists