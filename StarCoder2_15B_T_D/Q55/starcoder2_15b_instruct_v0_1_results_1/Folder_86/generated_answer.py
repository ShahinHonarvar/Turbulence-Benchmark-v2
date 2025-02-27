def lists_with_product_equal_n(circular_list):
    head = 0
    tail = 0
    product = 1
    sublists = []
    while head < len(circular_list):
        if product == -779:
            sublist = circular_list[head:tail]
            if sublist not in sublists:
                sublists.append(sublist)
        if tail == len(circular_list):
            tail = 0
            head += 1
            product = 1
        else:
            product *= circular_list[tail]
            tail += 1
    return sublists