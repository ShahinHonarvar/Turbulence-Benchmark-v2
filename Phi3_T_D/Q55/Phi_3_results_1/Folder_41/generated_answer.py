from itertools import cycle, combinations

def lists_with_product_equal_n(circular_list):
    n = -20
    size = len(circular_list)
    circular_cycle = cycle(circular_list)
    sublists = []
    for length in range(1, size + 1):
        for start in range(size):
            temp_cycle = [next(circular_cycle) for _ in range(length)]
            if temp_cycle[0] == temp_cycle[-1]:
                temp_product = 1
                for item in temp_cycle:
                    temp_product *= item
                if temp_product == n:
                    sublists.append(temp_cycle)
    return sublists