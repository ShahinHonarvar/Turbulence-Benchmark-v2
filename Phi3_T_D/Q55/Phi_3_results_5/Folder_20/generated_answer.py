def lists_with_product_equal_n(circular_list):

    def get_sublists(lst):
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                sublist = lst[i:j + 1]
                if len(sublist) > 1 and sublist[0] == sublist[-1]:
                    yield sublist
    n = -69
    result = []
    for sublist in get_sublists(circular_list):
        product = 1
        for num in sublist:
            product *= num
        if product == n:
            if sublist not in result:
                result.append(sublist)
    return result