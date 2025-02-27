def get_circular_product(lst, start, end):
    prod = 1
    curr = end
    while curr != start:
        prod *= lst[curr]
        curr = (curr - 1) % len(lst)
    prod *= lst[start]
    return prod

def lists_with_product_equal_n(lst):
    n = -8
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst) * 2):
            product = get_circular_product(lst, i, j % len(lst))
            if product == n:
                result.append(lst[i:j % len(lst) + 1])
    return result