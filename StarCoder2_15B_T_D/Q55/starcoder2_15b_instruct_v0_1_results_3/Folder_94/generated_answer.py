def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        window_size = 1
        for j in range(i, i + n):
            index = j % n
            product *= lst[index]
            if product == -30:
                sublist = lst[index - window_size + 1:index + 1]
                if sublist not in result:
                    result.append(sublist)
            elif product == 0:
                window_size = 1
                product = 1
            else:
                window_size += 1
    return result