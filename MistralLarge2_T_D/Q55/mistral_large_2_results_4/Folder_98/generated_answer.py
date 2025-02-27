def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for end in range(n):
            index = (start + end) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == -1:
                result.append(sublist[:])
            if product == 0:
                break
    return result