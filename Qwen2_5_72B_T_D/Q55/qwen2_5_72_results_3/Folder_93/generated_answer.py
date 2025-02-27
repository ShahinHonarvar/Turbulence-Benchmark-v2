def lists_with_product_equal_n(circular_list):

    def helper(start, length):
        product = 1
        for i in range(length):
            product *= circular_list[(start + i) % len(circular_list)]
        return product
    result = []
    for size in range(1, len(circular_list) + 1):
        for start in range(len(circular_list)):
            if helper(start, size) == -91:
                sublist = circular_list[start:start + size]
                if size > start:
                    sublist += circular_list[:size - start]
                result.append(sublist)
    return result