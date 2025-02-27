def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            index = (start + length - 1) % n
            product *= lst[index]
            if product == 40:
                sublist = [lst[(start + i) % n] for i in range(length)]
                result.append(sublist)
            elif product > 40:
                break
    return result