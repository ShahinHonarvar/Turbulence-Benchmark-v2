def lists_with_product_equal_n(lst):
    length = len(lst)
    result = []
    for sublist_size in range(1, length + 1):
        for start_index in range(length):
            sublist_product = 1
            for i in range(start_index, start_index + sublist_size):
                index = i % length
                sublist_product *= lst[index]
            if sublist_product == -7:
                sublist = []
                for i in range(start_index, start_index + sublist_size):
                    index = i % length
                    sublist.append(lst[index])
                result.append(sublist)
    return result