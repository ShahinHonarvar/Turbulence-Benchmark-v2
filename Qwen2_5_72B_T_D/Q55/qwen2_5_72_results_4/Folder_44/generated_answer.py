def lists_with_product_equal_n(circular_list):
    target_product = 29
    n = len(circular_list)
    circular_list = circular_list + circular_list
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            product = 1
            for i in range(start, end):
                product *= circular_list[i]
            if product == target_product:
                result.append(circular_list[start:end])
    return result