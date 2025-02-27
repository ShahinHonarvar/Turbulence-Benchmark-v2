import itertools

def lists_with_product_equal_n(lst, n):
    result = []
    for i in range(1, len(lst) + 1):
        for combination in itertools.combinations(lst, i):
            if n == 1:
                result.append(combination)
            elif len(combination) > 1:
                product = 1
                for num in combination:
                    product *= num
                if product == n:
                    result.append(combination)
    return result