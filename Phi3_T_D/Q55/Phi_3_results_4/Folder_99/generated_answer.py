def all_sublists(lst):
    length = len(lst)
    return [lst[i:j] for i in range(length) for j in range(i + 1, length + 1)]

def lists_with_product_equal_n(lst, target=415):
    results = []
    for sublist in all_sublists(lst):
        sublist_product = 1
        for num in sublist:
            sublist_product *= num
        if sublist_product == target:
            results.append(sublist)
    return results