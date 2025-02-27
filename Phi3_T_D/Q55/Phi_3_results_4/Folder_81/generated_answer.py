def lists_with_product_equal_n(circ_list):
    n = -8
    result = []
    for start in range(len(circ_list)):
        for end in range(start + 1, start + len(circ_list)):
            product = 1
            sublist = []
            for i in range(start, end % len(circ_list)):
                product *= circ_list[i % len(circ_list)]
                sublist.append(circ_list[i % len(circ_list)])
                if product == n:
                    result.append(sublist.copy())
                    break
            if product == n:
                break
    return result