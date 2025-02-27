def lists_with_product_equal_n(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if len(sublist) > 0 and len(sublist) <= len(circular_list) and (prod(sublist) == n):
                result.append(sublist)
    return result

def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result