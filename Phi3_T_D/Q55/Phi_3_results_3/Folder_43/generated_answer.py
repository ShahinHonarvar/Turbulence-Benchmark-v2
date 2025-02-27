def lists_with_product_equal_n(lst):
    circular_lst = lst + lst[:-1]
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for value in circular_lst[i:i + len(lst)]:
            sublist.append(value)
            product *= value
            if product == -26:
                result.append(sublist)
                break
            elif product > -26:
                break
    return result