from itertools import islice

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = list(islice(circular_list[start:] + circular_list[:start], length))
            product = 1
            for num in sublist:
                product *= num
            if product == 8:
                result.append(sublist)
    return result