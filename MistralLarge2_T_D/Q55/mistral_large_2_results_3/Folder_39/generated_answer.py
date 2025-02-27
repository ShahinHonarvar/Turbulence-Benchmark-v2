def lists_with_product_equal_n(lst, n=-46):

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    result = []
    length = len(lst)
    for start in range(length):
        for end in range(start + 1, length * 2):
            sublist = lst[start:end]
            if end >= length:
                sublist += lst[:end - length]
            if product(sublist) == n:
                result.append(sublist)
    return result