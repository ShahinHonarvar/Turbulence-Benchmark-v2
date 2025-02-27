def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            end = (start + size) % n
            if size == 1:
                product = circular_list[start]
            else:
                product *= circular_list[end - 1]
            if product == -1:
                result.append(circular_list[start:end] if start < end else circular_list[start:] + circular_list[:end])
            if product == 0 or abs(product) > 1:
                break
    return result