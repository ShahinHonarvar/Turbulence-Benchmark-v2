def lists_with_product_equal_n(circular_list, n=-15):
    result = []
    for i in range(len(circular_list)):
        sublist = [circular_list[i]]
        for j in range(i + 1, len(circular_list)):
            sublist.append(circular_list[j])
            if len(sublist) <= len(circular_list) and product(sublist) == n:
                result.append(sublist)
    return result

def product(iterable):
    return 1 if not iterable else iterable[0] * product(iterable[1:])