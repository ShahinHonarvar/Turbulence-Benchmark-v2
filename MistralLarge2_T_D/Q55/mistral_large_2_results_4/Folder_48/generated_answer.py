def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def product(lst):
        prod = 1
        for x in lst:
            prod *= x
        return prod
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = circular_list[i:j]
            if product(sublist) == 990:
                result.append(sublist)
            if i != 0 and j == n:
                sublist = circular_list[i:] + circular_list[:j - n]
                if product(sublist) == 990:
                    result.append(sublist)
    return result