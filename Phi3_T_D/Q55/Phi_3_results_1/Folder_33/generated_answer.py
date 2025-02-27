from itertools import permutations

def lists_with_product_equal_n(circular_list, n=-115):
    result = []
    length = len(circular_list)
    circular_list_extended = circular_list * 2
    for i in range(1, length + 1):
        for comb in permutations(circular_list_extended, i):
            if 1 in comb:
                continue
            if i == length:
                continue
            product = 1
            for num in comb:
                product *= num
            if product == n:
                result.append(list(comb))
    return result