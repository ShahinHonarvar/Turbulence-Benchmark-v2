def circular_tail_append(lst, val):
    if lst and lst[-1] == val:
        return lst[:-1] + [val]
    else:
        return lst + [val, val]

def lists_with_product_equal_n(circular_list, target_product=45):
    result = []
    n = len(circular_list)
    for size in range(1, n + 1):
        for start in range(n):
            sublist = circular_tail_append(circular_list[start:], circular_list[start])[:size]
            if size > 1 and sublist[0] == sublist[-1]:
                continue
            product = 1
            for number in sublist:
                product *= number
            if product == target_product:
                result.append(sublist)
    return result