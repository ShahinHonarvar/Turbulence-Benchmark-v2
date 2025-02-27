def lists_with_product_equal_n(lst):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = lst[i:j + 1]
            if j >= n:
                sublist = lst[i:n] + lst[:j % n + 1]
            if product(sublist) == 36:
                result.append(sublist)
    return result