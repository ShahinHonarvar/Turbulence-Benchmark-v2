def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end % n]
            if product == 3:
                result.append(circular_list[start:end % n + 1])
            elif product > 3:
                break
    return result