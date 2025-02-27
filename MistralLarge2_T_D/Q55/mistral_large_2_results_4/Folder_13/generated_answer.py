def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j % n]
            if j >= n:
                sublist += circular_list[:j % n]
            if product(sublist) == 54:
                result.append(sublist)
    return result