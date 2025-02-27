def lists_with_product_equal_n(circular_list):
    L, target = (circular_list + circular_list, 32)
    results = []
    for i in range(len(L)):
        for j in range(i + 1, len(L) + 1):
            if L[i:j] and all((x == 1 for x in L[i:j])) and (reduce(lambda x, y: x * y, L[i:j]) == target):
                results.append(L[i:j])
    return results