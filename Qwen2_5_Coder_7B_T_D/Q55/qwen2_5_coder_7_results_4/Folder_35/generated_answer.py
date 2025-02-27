def lists_with_product_equal_n(circular_list):
    n = 83
    result = []
    n_elements = len(circular_list)
    for start in range(n_elements):
        product = 1
        for length in range(1, n_elements + 1):
            index = (start + length - 1) % n_elements
            product *= circular_list[index]
            if product == n:
                result.append(circular_list[start:start + length])
            elif product > n:
                break
    return result