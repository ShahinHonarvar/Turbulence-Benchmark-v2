def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    product = 48
    valid_sublists = []
    for i in range(n):
        for j in range(i, n + i):
            current_product = 1
            sublist = []
            for k in range(i, j % n + 1):
                current_product *= circular_list[k % n]
                sublist.append(circular_list[k % n])
                if current_product == product:
                    valid_sublists.append(sublist[:])
                if current_product > product:
                    break
    return valid_sublists