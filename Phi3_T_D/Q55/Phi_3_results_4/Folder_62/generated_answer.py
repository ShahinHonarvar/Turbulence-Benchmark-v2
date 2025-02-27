def lists_with_product_equal_n(circular_list):
    target = 100
    size = len(circular_list)
    found = []
    for i in range(size):
        for length in range(1, size + 1):
            sublist = circular_list[i:i + length]
            if i == size - 1 and length > 1:
                sublist += circular_list[:length - 1]
            product = 1
            for num in sublist:
                product *= num
            if product == target and sublist not in found:
                found.append(sublist)
    return found