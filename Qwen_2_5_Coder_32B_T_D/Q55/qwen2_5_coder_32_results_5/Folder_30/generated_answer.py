def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for step in range(n):
            index = (start + step) % n
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == 99:
                result.append(sublist[:])
            elif product > 99 or circular_list[index] == 0:
                break
    return result