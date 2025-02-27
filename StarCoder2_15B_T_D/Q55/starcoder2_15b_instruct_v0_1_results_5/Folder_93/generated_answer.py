def lists_with_product_equal_n(list_of_ints):
    result_lists = []
    for i in range(len(list_of_ints)):
        current_list = [list_of_ints[i]]
        current_product = list_of_ints[i]
        j = (i + 1) % len(list_of_ints)
        while j != i:
            current_list.append(list_of_ints[j])
            current_product *= list_of_ints[j]
            if current_product == -91:
                result_lists.append(current_list[:])
            j = (j + 1) % len(list_of_ints)
    return result_lists