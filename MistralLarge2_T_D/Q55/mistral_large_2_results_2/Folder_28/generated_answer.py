def lists_with_product_equal_n(circular_list):
    n = 85
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for end in range(length):
            product *= circular_list[(start + end) % length]
            if product == n:
                sublist = [circular_list[(start + i) % length] for i in range(end + 1)]
                result.append(sublist)
            elif product > n:
                break
    return result