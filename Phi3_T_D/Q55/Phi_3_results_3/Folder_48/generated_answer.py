def lists_with_product_equal_n(circular_list):
    n = 990
    results = []
    length = len(circular_list)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= circular_list[j % length]
            if product == n:
                results.append(circular_list[i:j + 1])
            if product > n:
                break
    return results