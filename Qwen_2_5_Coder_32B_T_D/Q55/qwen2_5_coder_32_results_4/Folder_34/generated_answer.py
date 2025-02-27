from itertools import islice

def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    target_product = -81
    for start in range(n):
        product = 1
        for i in range(start, start + n):
            index = i % n
            product *= lst[index]
            if product == target_product:
                result.append(lst[start:index + 1])
    return result