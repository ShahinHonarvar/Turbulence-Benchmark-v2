def lists_with_product_equal_n(lst):
    product = 15
    num_len = len(lst)
    subsets = []
    for i in range(num_len):
        for j in range(i, num_len * 2):
            temp_product = 1
            sublist = []
            for k in range(i, j % num_len + 1):
                sublist.append(lst[k % num_len])
                temp_product *= lst[k % num_len]
                if temp_product == product:
                    subsets.append(sublist)
    return subsets