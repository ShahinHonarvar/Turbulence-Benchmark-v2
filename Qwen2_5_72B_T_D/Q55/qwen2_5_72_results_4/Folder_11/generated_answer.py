def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= circular_list[index]
            if product == -15:
                result.append(circular_list[start:index + 1])
            if product == 0 or abs(product) > 15:
                break
    return result