from itertools import cycle

def lists_with_product_equal_n(circular_list, target_product=851):
    results = []
    for start in range(len(circular_list)):
        prod = 1
        current_sublist = []
        for value in cycle(circular_list):
            current_sublist.append(value)
            prod *= value
            if prod == target_product:
                results.append(current_sublist)
                break
            elif prod > target_product:
                break
            if len(current_sublist) == len(circular_list):
                current_sublist = current_sublist[1:]
        if prod == target_product:
            break
    return results