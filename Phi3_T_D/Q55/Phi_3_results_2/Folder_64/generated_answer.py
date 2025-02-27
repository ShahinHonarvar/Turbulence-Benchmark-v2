from itertools import permutations

def lists_with_product_equal_n(circular_list):

    def prod(lst):
        result = 1
        for i in lst:
            result *= i
        return result
    result = []
    for i in range(1, len(circular_list) + 1):
        for subset in permutations(circular_list, i):
            if prod(subset) == 3:
                if subset not in result:
                    result.append(list(subset))
    return result