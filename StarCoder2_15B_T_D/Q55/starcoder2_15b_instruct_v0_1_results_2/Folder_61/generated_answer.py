def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and prod(sublist) == -10:
                sublists.append(sublist)
    return sublists

def prod(iterable):
    return 1 if not iterable else iterable[0] * prod(iterable[1:])