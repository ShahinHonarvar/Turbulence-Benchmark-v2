from itertools import combinations

def lists_with_product_equal_n(circular_list, n=6):
    circular_list = circular_list + circular_list[:-1]
    result = []
    for i in range(1, len(circular_list) + 1):
        for combo in combinations(circular_list, i):
            if n == 1 and 1 in combo and (len(combo) == combo.count(1)):
                result.append(list(combo))
            elif len(combo) > 0 and n % combo[0] == 0:
                product = 1
                for num in combo:
                    product *= num
                if product == n:
                    result.append(list(combo))
    result = [list(t) for t in set((tuple(sublist) for sublist in result))]
    return result