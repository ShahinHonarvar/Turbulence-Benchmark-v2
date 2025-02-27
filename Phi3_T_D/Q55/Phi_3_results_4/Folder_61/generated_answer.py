from itertools import cycle, combinations

def lists_with_product_equal_n(circular_list):
    target_product = -10
    sublists = []
    n = len(circular_list)
    circular_cycle = cycle(circular_list)
    for r in range(1, n + 1):
        for combination in combinations(circular_cycle, r):
            if n == len(set(combination)):
                product = 1
                for number in combination:
                    product *= number
                if product == target_product and combination not in sublists:
                    sublists.append(list(combination))
    return sublists