def lists_with_product_equal_n(circular_list):
    n = -22
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j % len(circular_list)]
            if len(sublist) > 0 and n == prod(sublist):
                result.append(sublist)
    return result

def prod(lst):
    product = 1
    for num in lst:
        product *= num
    return product