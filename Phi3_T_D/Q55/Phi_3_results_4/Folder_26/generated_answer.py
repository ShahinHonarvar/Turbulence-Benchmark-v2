from itertools import permutations

def product(lst):
    p = 1
    for n in lst:
        p *= n
    return p

def lists_with_product_equal_n(lst):
    circular_perm = [lst[i:i + len(lst)] for i in range(len(lst))] + [lst[-1:] + lst[:1]]
    result = []
    for perm in circular_perm:
        for i in range(1, len(perm) + 1):
            for sublist in permutations(perm, i):
                if product(sublist) == 93:
                    result.append(list(sublist))
    return result