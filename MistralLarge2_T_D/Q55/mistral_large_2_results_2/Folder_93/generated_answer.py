def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length) % n
            product *= circular_list[end]
            if product == -91:
                if end >= start:
                    results.append(circular_list[start:end + 1])
                else:
                    results.append(circular_list[start:] + circular_list[:end + 1])
            elif product == 0:
                break
    return results