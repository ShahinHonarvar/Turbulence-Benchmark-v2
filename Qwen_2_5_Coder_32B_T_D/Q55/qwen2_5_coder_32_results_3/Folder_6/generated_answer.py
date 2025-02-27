def lists_with_product_equal_n(lst):
    n = 42
    result = []
    lst_length = len(lst)
    for start in range(lst_length):
        product = 1
        for size in range(1, lst_length + 1):
            index = (start + size - 1) % lst_length
            product *= lst[index]
            if product == n:
                sublist = [lst[(start + i) % lst_length] for i in range(size)]
                result.append(sublist)
            elif product > n:
                break
    return result