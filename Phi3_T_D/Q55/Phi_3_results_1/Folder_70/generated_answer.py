def lists_with_product_equal_n(circular_list, n=32):
    circular_list = circular_list + circular_list[:-1]
    result = []
    for i in range(len(circular_list)):
        product, sublist = (1, [])
        for j in range(i, len(circular_list) + i):
            product *= circular_list[j % len(circular_list)]
            sublist.append(circular_list[j % len(circular_list)])
            if product == n:
                result.append(sublist.copy())
                break
            elif product > n:
                break
    return result