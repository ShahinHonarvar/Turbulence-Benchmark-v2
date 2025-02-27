def lists_with_product_equal_n(circular_list):
    target_product = 37
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            for i in range(length):
                index = (start + i) % n
                product *= circular_list[index]
            if product == target_product:
                sublist = [circular_list[(start + i) % n] for i in range(length)]
                result.append(sublist)
            product = 1
    return result