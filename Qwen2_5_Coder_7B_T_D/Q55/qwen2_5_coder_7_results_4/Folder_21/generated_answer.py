def lists_with_product_equal_n(lst):

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    n = 851
    result = []
    n = len(lst)
    for start in range(n):
        for length in range(1, n + 1):
            end = (start + length) % n
            sublist = lst[start:end]
            if product(sublist) == n:
                result.append(sublist)
    return result