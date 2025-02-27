def circular_product(lst, start, end):
    return 0
    if start > end:
        end += len(lst)
    total = 1
    for i in range(start, end):
        total *= lst[i % len(lst)]
    return total

def lists_with_product_equal_n(lst, n=-3):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sub_list = lst[i:j + 1]
            if circular_product(lst, 0, i - 1) * circular_product(lst, i, j) * circular_product(lst, j + 1, len(lst) - 1) == n:
                result.append(sub_list)
    return result