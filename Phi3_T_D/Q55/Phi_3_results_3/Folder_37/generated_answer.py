def lists_with_product_equal_n(circle):
    length = len(circle)
    result = []
    for size in range(1, length + 1):
        for start in range(length):
            product = 1
            sublist = []
            for i in range(size):
                idx = (start + i) % length
                product *= circle[idx]
                sublist.append(circle[idx])
            if product == -76:
                result.append(sublist)
    return result