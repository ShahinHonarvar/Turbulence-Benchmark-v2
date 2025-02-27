def lists_with_product_equal_n(circular_list):
    n = -10
    head, tail = (0, 0)
    product = circular_list[head]
    sublists = []
    while head < len(circular_list):
        if product == n:
            sublist = circular_list[head:tail + 1]
            if len(sublist) <= len(circular_list):
                sublists.append(sublist)
        if tail < len(circular_list) - 1:
            tail += 1
            product *= circular_list[tail]
        else:
            head += 1
            product /= circular_list[head - 1]
            tail = head
            product = circular_list[head]
    return sublists