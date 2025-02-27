def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i + 1, i + n):
            sublist = circular_list[i:j]
            if j >= n:
                sublist += circular_list[:j - n]
            if product(sublist) == -44:
                result.append(sublist)
    return result