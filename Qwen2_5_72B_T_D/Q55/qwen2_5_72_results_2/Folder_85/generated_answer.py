def lists_with_product_equal_n(lst):
    length = len(lst)
    target_product = -97
    result = []
    for start in range(length):
        product = 1
        for end in range(length):
            actual_end = (start + end) % length
            product *= lst[actual_end]
            if product == target_product:
                result.append(lst[start:actual_end + 1])
            elif product != 0:
                product /= lst[actual_end]
    return result