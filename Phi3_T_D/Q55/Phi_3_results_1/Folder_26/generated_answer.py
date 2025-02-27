def circular_list_index(lst, i):
    return i % len(lst)

def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def lists_with_product_equal_n(lst, target=93):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(n):
            if product(lst[circular_list_index(lst, i):circular_list_index(lst, j + 1 if j != n - 1 else 0) + 1]) == target:
                result.append(lst[circular_list_index(lst, i):circular_list_index(lst, j + 1 if j != n - 1 else 0) + 1])
    return result