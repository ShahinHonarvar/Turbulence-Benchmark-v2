def lists_with_product_equal_n(circular_list):
    n = 42
    length = len(circular_list)
    sublists = []

    def get_sublists(start):
        product = 1
        for i in range(length):
            product *= circular_list[(start + i) % length]
            if product == n:
                sublists.append(circular_list[start:start + i + 1])
        if product == n:
            sublists.append(circular_list[start:])
    for start in range(length):
        get_sublists(start)
    return sublists