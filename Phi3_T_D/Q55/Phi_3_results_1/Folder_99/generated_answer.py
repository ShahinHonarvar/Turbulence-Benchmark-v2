def lists_with_product_equal_n(circular_list, n=415):
    seen = set()
    original_list = circular_list[:]
    results = []
    for i in range(len(circular_list)):
        current_product = 1
        for j in range(len(circular_list)):
            current_product *= circular_list[(i + j) % len(circular_list)]
            if current_product > n:
                break
            if current_product == n:
                sublist = circular_list[i:i + j + 1]
                if frozenset(sublist) not in seen:
                    results.append(sublist)
                    seen.add(frozenset(sublist))
    for result in results:
        if result in original_list:
            original_list[original_list.index(result[0]):original_list.index(result[-1]) + 1] = []
    return result