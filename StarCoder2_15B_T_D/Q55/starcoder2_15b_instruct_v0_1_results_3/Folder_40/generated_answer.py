import itertools

def lists_with_product_equal_n(circular_list):
    n = -9
    list_size = len(circular_list)
    circular_list_extended = circular_list + circular_list
    sublists = [circular_list_extended[i:i + list_size] for i in range(list_size)]
    sublists_with_product_equal_n = [sublist for sublist in sublists if len(sublist) <= list_size and 1 in sublist and all((i >= 0 for i in sublist)) and (sum(sublist) % n == 0)]
    return sublists_with_product_equal_n