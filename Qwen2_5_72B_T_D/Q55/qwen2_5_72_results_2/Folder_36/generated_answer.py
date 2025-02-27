def lists_with_product_equal_n(circular_list):
    target_product = 714
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for current in range(length):
            index = (start + current) % length
            product *= circular_list[index]
            if product == target_product:
                result.append(circular_list[start:index + 1])
            elif product > target_product:
                break
    return result