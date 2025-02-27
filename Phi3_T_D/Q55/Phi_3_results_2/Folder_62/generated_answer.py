def circular_product(lst, start, end):
    product = 1
    for i in range(start, end):
        product *= lst[i]
    if end < len(lst):
        product *= lst[end]
    return product

def lists_with_product_equal_n(lst):
    n = 100
    result = []
    for size in range(1, len(lst) + 1):
        for i in range(len(lst)):
            product = circular_product(lst, i, i + size - 1)
            if product == n:
                result.append(lst[i:i + size])
            if i + size >= len(lst):
                break
    return result