def lists_with_product_equal_n(lst):
    n = -32
    result = []
    len_lst = len(lst)
    for i in range(len_lst):
        for j in range(i, len_lst):
            sublist = lst[i:j + 1]
            if len(sublist) <= len_lst and (len(sublist) == len_lst or sublist == lst[j + 1:] + lst[:i]):
                product = 1
                for num in sublist:
                    product *= num
                if product == n:
                    result.append(sublist)
    return result