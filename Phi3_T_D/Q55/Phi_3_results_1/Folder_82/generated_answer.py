from itertools import permutations

def lists_with_product_equal_n(circular_list):

    def product(subset):
        prod = 1
        for num in subset:
            prod *= num
        return prod == 8
    result = []
    for i in range(1, len(circular_list) + 1):
        for subset in permutations(circular_list, i):
            if product(subset):
                result.append(list(subset))
    return list(map(list, set(map(tuple, result))))