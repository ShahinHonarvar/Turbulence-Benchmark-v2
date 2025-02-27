def lists_with_product_equal_n(circular_list):
    N = -22
    valid_sublists = []
    list_length = len(circular_list)
    for start in range(list_length):
        product = 1
        sublist = []
        for end in range(start, start + list_length):
            index = end % list_length
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == N:
                valid_sublists.append(list(sublist))
                break
            elif product > N:
                break
    return valid_sublists