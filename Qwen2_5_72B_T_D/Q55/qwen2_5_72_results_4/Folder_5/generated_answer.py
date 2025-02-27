def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= circular_list[index]
            if product == -33:
                result.append(circular_list[start:index + 1])
            elif abs(product) > 33:
                break
    return result