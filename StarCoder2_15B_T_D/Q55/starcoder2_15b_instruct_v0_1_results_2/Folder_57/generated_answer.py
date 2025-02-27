def lists_with_product_equal_n(circular_list):
    head = 0
    tail = 0
    product = 1
    sublists = []
    while head < len(circular_list):
        if product == -75:
            sublists.append(circular_list[head:tail] + circular_list[:head])
            product /= circular_list[head]
            head += 1
        elif product < -75:
            product /= circular_list[head]
            head += 1
        else:
            product *= circular_list[tail]
            tail += 1
        if tail == len(circular_list):
            tail = 0
            head += 1
            if head == len(circular_list):
                break
    return sublists