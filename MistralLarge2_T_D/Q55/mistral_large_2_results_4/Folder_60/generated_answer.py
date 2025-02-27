def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            index = (start + size - 1) % n
            product *= circular_list[index]
            if product == 49:
                result.append(circular_list[start:start + size] if start + size <= n else circular_list[start:] + circular_list[:(start + size) % n])
            if product > 49:
                break
    return result