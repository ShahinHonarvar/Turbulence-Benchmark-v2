def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    target = 96
    result = []
    for start in range(size):
        product = 1
        for i in range(size):
            index = (start + i) % size
            product *= circular_list[index]
            if product == target:
                result.append(circular_list[start:index + 1])
            if product > target:
                break
    return result