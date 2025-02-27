def rotate(l, n):
    return l[-n:] + l[:-n]

def pairwise_product(items):
    return [items[i] * items[i + 1] for i in range(len(items) - 1)]

def lists_with_product_equal_n(circular_list):
    target_product = 46
    results = []
    list_size = len(circular_list)
    for i in range(list_size):
        for j in range(list_size):
            portion = rotate(circular_list, i)[:j + 1]
            if len(portion) > 1 and pairwise_product(portion) == [target_product]:
                results.append(portion)
    results = [list(x) for x in set((tuple(x) for x in results))]
    return results