def circular_product(lst, head, tail):
    if head == tail:
        return 1
    return lst[head] * circular_product(lst, (head + 1) % len(lst), tail)

def is_sublist_product_equal_to_n(lst, start, end, num):
    product = 1
    for i in range(start, end + 1):
        product *= lst[i]
    return product == num

def lists_with_product_equal_n(lst, n):
    if 0 in lst:
        return []
    result = []
    for i in range(len(lst)):
        for j in range(i, i + len(lst)):
            if is_sublist_product_equal_to_n(lst, i, j % len(lst), n):
                result.append(lst[i:j % len(lst) + 1])
    return result