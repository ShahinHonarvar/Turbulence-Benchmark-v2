def lists_with_product_equal_n(circular_list):
    N = 90
    length = len(circular_list)
    sublists = []
    for start in range(length):
        product = 1
        sublist = []
        for end in range(start, start + length):
            index = end % length
            product *= circular_list[index]
            if product == N:
                sublist = circular_list[start:index + 1]
                sublists.append(sublist)
                break
            elif product > N:
                product = 1
                break
        if sublist:
            sublists.append(sublist)
    return sublists