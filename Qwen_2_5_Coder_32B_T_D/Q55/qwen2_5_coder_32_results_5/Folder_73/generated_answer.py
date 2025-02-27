def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end % n]
            if product == 40:
                result.append(circular_list[start % n:end % n + 1])
            elif product > 40:
                break
    return result