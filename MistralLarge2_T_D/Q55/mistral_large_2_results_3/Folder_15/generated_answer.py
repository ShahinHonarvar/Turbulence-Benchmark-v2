def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        result = []
        length = len(lst)
        for start in range(length):
            for end in range(start, length):
                sublist = lst[start:end + 1]
                if len(sublist) > 0:
                    product = 1
                    for num in sublist:
                        product *= num
                    if product == n:
                        result.append(sublist)
        return result
    n = -7
    return sublists_with_product_equal_n(lst + lst, n)