def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for i in range(n):
        product = 1
        for j in range(n):
            idx = (i + j) % n
            product *= circular_list[idx]
            if product == 632:
                results.append(circular_list[i:i + j + 1] if i + j + 1 <= n else circular_list[i:] + circular_list[:(i + j + 1) % n])
            elif product > 632:
                break
    return results