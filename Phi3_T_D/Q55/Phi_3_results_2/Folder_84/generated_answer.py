def lists_with_product_equal_n(circular_list):
    target = -906
    n = len(circular_list)
    circular_list = circular_list * 2
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= circular_list[j % n]
            sublist.append(circular_list[j % n])
            if product == target:
                result.append(sublist.copy())
                break
            elif product > target:
                break
        if product == target:
            break
    return result