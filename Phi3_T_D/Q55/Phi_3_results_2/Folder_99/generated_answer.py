def circular_list_generator(lst):
    times_to_repeat = len(lst)
    for i in range(times_to_repeat):
        yield from (lst[i:] + lst[:i])

def sublists_product(lst, target):
    for start_index in range(len(lst)):
        product = 1
        sublist = []
        for current_index in range(start_index, len(lst) + start_index):
            index = current_index % len(lst)
            product *= lst[index]
            sublist.append(lst[index])
            if product == target:
                yield sublist.copy()
            elif product > target:
                break

def lists_with_product_equal_n(lst, n):
    results = []
    for circular_list in circular_list_generator(lst):
        results.extend(sublists_product(circular_list, n))
    return results