def lists_with_product_equal_n(circular_list):
    n = 90
    min_len = 0
    sublists = set()
    product = 1
    for _ in range(len(circular_list)):
        while product != n and min_len < len(circular_list):
            product *= circular_list[-min_len]
            min_len += 1
            if product == n:
                sublists.add(tuple(circular_list[-min_len:]))
            if min_len == len(circular_list):
                product = product // circular_list[-1]
                min_len = 0
        product = 1
        min_len = 0
    return [list(sublist) for sublist in sublists]