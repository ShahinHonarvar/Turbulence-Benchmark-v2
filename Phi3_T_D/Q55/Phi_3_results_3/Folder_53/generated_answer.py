def lists_with_product_equal_n(circular_list):
    n = -87
    if not circular_list:
        return []
    product = 1
    sublists = []
    start = 0
    for end in range(len(circular_list)):
        product *= circular_list[end]
        while product < n and end > start:
            product //= circular_list[start]
            start += 1
        if product == n:
            sublist = circular_list[start:end + 1]
            if sublist not in sublists:
                sublists.append(sublist)
        if end == len(circular_list) - 1 and circular_list[start] != 0:
            product //= circular_list[0]
            start += 1
    circular_list += [circular_list[0]]
    for end in range(1, len(circular_list)):
        product = 1
        for i in range(start, len(circular_list)):
            product *= circular_list[i]
            if product == n:
                sublists.append(circular_list[i:end + 1])
                break
            elif product > n:
                break
        start += 1
    return sublists