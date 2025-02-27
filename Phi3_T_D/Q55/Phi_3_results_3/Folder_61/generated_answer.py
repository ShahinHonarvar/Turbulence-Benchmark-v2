def lists_with_product_equal_n(circular_list):
    n = -10
    len_list = len(circular_list)
    result = []

    def helper(index, sublist):
        if index == len_list:
            index = 0
        curr_product = 1
        new_sublist = []
        for i in range(index, len_list):
            curr_product *= circular_list[i]
            new_sublist.append(circular_list[i])
            if curr_product == n:
                result.append(new_sublist)
            elif curr_product < n and len(new_sublist) < len_list - 1:
                continue
            elif curr_product > n:
                curr_product = 1 / circular_list[i]
                new_sublist = [circular_list[i]]
    for i in range(len_list * 2):
        helper(i % len_list, [])
    return result