from itertools import permutations

def lists_with_product_equal_n(circle):
    target_product = -16
    size = len(circle)
    found_sublists = []
    for length in range(1, size + 1):
        for combination in permutations(circle, length):
            if combination[0] == circle[-1] and len(combination) == size:
                continue
            product = 1
            for number in combination:
                product *= number
            if product == target_product:
                found_sublists.append(combination)
    return found_sublists