def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    result = []
    for i in range(size):
        for j in range(i + 1, size + i):
            sublist = circular_list[i:j]
            if len(sublist) <= size and product(sublist) == -15:
                result.append(sublist)
    return result

def product(iterable):
    result = 1
    for item in iterable:
        result *= item
    return result