def rotate_list(lst):
    if not lst:
        return lst
    return lst[1:] + [lst[0]]

def has_product_n(lst, target):
    current_product = 1
    start_index = 0
    for i, num in enumerate(lst):
        current_product *= num
        while current_product > target and start_index < i:
            current_product /= lst[start_index]
            start_index += 1
        if current_product == target:
            return lst[start_index:i + 1]
    return []

def lists_with_product_equal_n(lst):
    result = []
    for _ in range(len(lst)):
        sublist = has_product_n(lst, 91)
        if sublist:
            result.append(sublist)
        lst = rotate_list(lst)
    return result