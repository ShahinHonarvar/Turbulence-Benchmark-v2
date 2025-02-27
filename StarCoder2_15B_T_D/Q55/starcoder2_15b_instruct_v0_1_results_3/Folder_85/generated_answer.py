import itertools

def lists_with_product_equal_n(circular_list):
    n = -97
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and n % abs(sublist[0]) == 0:
                product = 1
                for x in sublist:
                    product *= x
                if product == n:
                    sublists.append(sublist)
    return sublists