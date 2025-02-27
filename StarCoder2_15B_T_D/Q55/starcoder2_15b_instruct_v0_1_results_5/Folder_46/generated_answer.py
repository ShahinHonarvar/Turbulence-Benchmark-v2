def lists_with_product_equal_n(circular_list):
    n = 53
    sublists = []
    length = len(circular_list)
    for i in range(length):
        product = 1
        j = i
        while product < n:
            product *= circular_list[j]
            j = (j + 1) % length
            if product == n:
                sublist = circular_list[i:j]
                if sublist not in sublists:
                    sublists.append(sublist)
    return sublists