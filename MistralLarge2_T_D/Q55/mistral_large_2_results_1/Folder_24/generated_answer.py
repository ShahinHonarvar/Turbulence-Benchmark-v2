def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            end = (start + size) % n
            product *= circular_list[end]
            if product == -89:
                sublist = circular_list[start:start + size]
                if start + size > n:
                    sublist += circular_list[:end + 1]
                result.append(sublist)
    return result