def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            end = (start + size) % n
            product *= circular_list[end]
            if product == 714:
                result.append(circular_list[start:end + 1] if end >= start else circular_list[start:] + circular_list[:end + 1])
            elif product > 714:
                break
    return result