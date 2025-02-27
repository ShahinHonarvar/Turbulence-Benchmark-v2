def lists_with_product_equal_n(circular_list, n=-5):
    result = []
    for i in range(len(circular_list)):
        sublist = [circular_list[i]]
        product = circular_list[i]
        for j in range(i + 1, i + len(circular_list)):
            sublist.append(circular_list[j % len(circular_list)])
            product *= circular_list[j % len(circular_list)]
            if product == n:
                result.append(sublist)
            elif product < n:
                continue
            else:
                break
    return result