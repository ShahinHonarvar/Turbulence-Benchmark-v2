def product_of_elements(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def lists_with_product_equal_n(circular_list):
    list_len = len(circular_list)
    product_target = 74
    sublists = []
    for sublist_len in range(1, list_len + 1):
        product_lookup = {}
        for start in range(list_len):
            sublist = circular_list[start:start + sublist_len] + circular_list[:sublist_len - (list_len - start)]
            sublist_length = len(sublist)
            product = product_of_elements(sublist)
            if product == product_target and sublist_length <= sublist_len:
                sorted_sublist = sorted(sublist)
                if sorted_sublist not in sublists:
                    sublists.append(sorted_sublist)
    return sublists