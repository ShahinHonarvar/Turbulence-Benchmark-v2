def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            idx = (start + end) % n
            product *= circular_list[idx]
            if product == 6:
                result.append(circular_list[start:end + 1] + circular_list[:end + 1 - n])
            elif product > 6:
                break
    return result