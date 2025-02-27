def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    n = len(circular_list)
    prod = -5
    index = 0
    found_sublists = set()
    while index < n:
        current_prod = 1
        j = index
        current_sublist = []
        while current_prod != prod:
            current_prod *= circular_list[j % n]
            current_sublist.append(circular_list[j % n])
            if current_prod == prod:
                found_sublists.add(tuple(current_sublist))
            if current_sublist and current_sublist[0] * current_sublist[-1] > 0:
                break
            j += 1
        index += 1
    return [list(sublist) for sublist in found_sublists]