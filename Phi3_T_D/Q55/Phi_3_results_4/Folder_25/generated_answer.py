def lists_with_product_equal_n(circular_list):
    n = -32
    sublists = []
    for size in range(1, len(circular_list) + 1):
        for i in range(len(circular_list)):
            product = 1
            for j in range(size):
                product *= circular_list[(i + j) % len(circular_list)]
            if product == n:
                sublist = circular_list[i:i + size]
                sublists.append(sublist)
                if circular_list * (size - 1) not in sublists:
                    sublists.append(circular_list * (size - 1))
    return sublists