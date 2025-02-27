def lists_with_product_equal_n(circular_list):
    n = -968
    found_sublists = []
    for i in range(len(circular_list)):
        current_product = 1
        sublist = []
        for j in range(len(circular_list)):
            sublist.append(circular_list[(i + j) % len(circular_list)])
            current_product *= sublist[-1]
            if current_product == n:
                found_sublists.append(sublist[:])
            if current_product > n:
                break
    return found_sublists