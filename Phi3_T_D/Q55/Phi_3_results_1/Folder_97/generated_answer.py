def lists_with_product_equal_n(circular_list):
    result_sublists = []
    n = -938
    list_length = len(circular_list)
    for i in range(list_length):
        product = 1
        sublist = []
        for j in range(i, i + list_length):
            product *= circular_list[j % list_length]
            sublist.append(circular_list[j % list_length])
            if product == n:
                result_sublists.append(sublist[:])
            if product > n:
                product //= circular_list[j % list_length]
                sublist.pop()
            if len(sublist) > list_length:
                break
    return result_sublists