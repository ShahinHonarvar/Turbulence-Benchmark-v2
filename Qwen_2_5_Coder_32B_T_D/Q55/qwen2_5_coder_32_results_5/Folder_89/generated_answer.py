def lists_with_product_equal_n(lst):

    def circular_sublists(lst):
        n = len(lst)
        for i in range(n):
            for j in range(1, n + 1):
                yield (lst[i:i + j] + lst[:max(0, (i + j) % n - n)])
    result = []
    for sublist in circular_sublists(lst):
        product = 1
        for num in sublist:
            product *= num
            if product == 57:
                result.append(sublist)
            elif product > 57:
                break
    return result