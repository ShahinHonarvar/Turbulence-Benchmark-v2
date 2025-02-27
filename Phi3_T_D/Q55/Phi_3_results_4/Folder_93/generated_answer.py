from itertools import cycle

def lists_with_product_equal_n(circular_list):
    N = -91
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if j + 1 == len(circular_list):
                sublist += circular_list[:i]
            product = 1
            for number in sublist:
                product *= number
            if product == N:
                result.append(sublist)
    return result