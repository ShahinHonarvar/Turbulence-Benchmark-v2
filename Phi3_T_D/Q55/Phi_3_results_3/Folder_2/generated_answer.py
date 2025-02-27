def lists_with_product_equal_n(circular_list):
    target_product = -968
    size = len(circular_list)
    result = []
    for i in range(size):
        for j in range(i + 1, size + i + 1):
            sublist = circular_list[i:j % size]
            if len(sublist) < size and all((n != 0 for n in sublist)) and (prod(sublist) == target_product):
                product_is_zero = any((n == 0 for n in sublist))
                result.append(sublist if not product_is_zero else [])
    return result

def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result