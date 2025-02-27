def lists_with_product_equal_n(circular_list):
    n = -22
    result = []
    for start in range(len(circular_list)):
        product = 1
        for end in range(start, start + len(circular_list)):
            product *= circular_list[end % len(circular_list)]
            if product == n:
                result.append(circular_list[start:end + 1])
            elif product > n:
                break
    return result