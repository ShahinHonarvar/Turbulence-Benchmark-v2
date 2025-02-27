import itertools

def lists_with_product_equal_n(circular_list):
    n = -46
    m = len(circular_list)
    result = []
    extended_list = circular_list * 2
    for size in range(1, m + 1):
        for i in range(m + 1):
            sublist = extended_list[i:i + size]
            if size == 1 and sublist[0] == n:
                result.append(sublist)
            elif size > 1 and n % sublist[0] == 0:
                product = 1
                for num in sublist:
                    product *= num
                if product == n:
                    result.append(sublist)
    return result