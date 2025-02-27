def rotate_left(lst, k):
    return lst[k:] + lst[:k]

def product(lst):
    p = 1
    for item in lst:
        p *= item
    return p

def lists_with_product_equal_n(lst):
    target_product = 247
    found_lists = []
    n = len(lst)
    for size in range(1, n + 1):
        for start in range(n):
            divided_list = rotate_left(lst, start)[:size]
            if product(divided_list) == target_product:
                found_lists.append(divided_list)
            if len(divided_list) == n:
                break
    return found_lists