def lists_with_product_equal_n(circular_list):
    target_product = -87
    head, *tail = circular_list
    results = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for value in circular_list[i:] + circular_list[:i]:
            sublist.append(value)
            product *= value
            if product == target_product:
                results.append(sublist.copy())
                break
            elif product > target_product:
                break
    return results