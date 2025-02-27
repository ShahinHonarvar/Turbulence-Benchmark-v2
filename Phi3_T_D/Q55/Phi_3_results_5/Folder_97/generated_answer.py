def lists_with_product_equal_n(circular_list):
    n = -938
    sublists = []
    for start in range(len(circular_list)):
        product = 1
        for end in range(start, len(circular_list) + start):
            index = end % len(circular_list)
            product *= circular_list[index]
            if product == n:
                sublist = circular_list[start:index + 1]
                if sublist not in sublists:
                    sublists.append(sublist[:])
            elif product > n:
                break
    return sublists