from itertools import tee, cycle

def lists_with_product_equal_n(circular_list):
    target_product = 49
    sublists = []

    def contiguous_sublists(iterable, length):
        iterables = tee(circular_list, length)
        return list(zip(*iterables))
    for size in range(1, len(circular_list) + 1):
        for sublist in contiguous_sublists(cycle(circular_list), size):
            if all((x != 1 and x == target_product // x for x in sublist)) and all((x == sublist[0] for x in sublist)):
                sublists.append(sublist)
    return sublists