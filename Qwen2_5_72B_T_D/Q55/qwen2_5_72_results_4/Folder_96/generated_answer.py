def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            index = (start + size - 1) % n
            product *= circular_list[index]
            if product == 0:
                result.append(circular_list[start:index + 1])
            if product != 0:
                for _ in range(size, n):
                    product *= circular_list[(start + _ - 1) % n] // circular_list[(start + _ - size) % n]
                    if product == 0:
                        result.append(circular_list[start:(start + _) % n + 1])
    return result