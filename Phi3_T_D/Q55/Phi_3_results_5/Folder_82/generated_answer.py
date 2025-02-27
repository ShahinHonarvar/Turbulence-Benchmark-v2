def circular_sliding_window(lst, target_product):
    """Generate all sublists from a circular list that match the target product."""
    size = len(lst)
    for i in range(size):
        product = 1
        sublist = []
        for j in range(size):
            index = (i + j) % size
            sublist.append(lst[index])
            product *= lst[index]
            if product == target_product:
                yield sublist
            elif product > target_product:
                break

def lists_with_product_equal_n(circular_list):
    target_product = 8
    return list(circular_sliding_window(circular_list, target_product))