def lists_with_product_equal_n(circular_list, n=13):
    len_list = len(circular_list)
    found_sublists = []
    for length in range(1, len_list):
        for start_index in range(len_list):
            temp_product = 1
            temp_sublist = []
            for i in range(start_index, start_index + length):
                temp_sublist.append(circular_list[i % len_list])
                temp_product *= circular_list[i % len_list]
                if temp_product == n:
                    found_sublists.append(temp_sublist)
                    break
                elif temp_product > n:
                    break
    return found_sublists