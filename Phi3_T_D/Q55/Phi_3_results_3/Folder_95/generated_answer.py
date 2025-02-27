def get_sublist(start, l, seen):
    n = len(l)
    for end in range(start + 1, len(l) + start):
        if end > n:
            end = end % n
        product = 1
        for i in range(start, end + 1):
            product *= l[i]
        if product == 28:
            sublist = tuple(l[start:i + 1])
            if sublist not in seen:
                seen.add(sublist)
                yield list(sublist)

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    seen = set()
    for i, num in enumerate(circular_list):
        if i == n - 1 or not get_sublist(i, circular_list, seen):
            continue
        yield from get_sublist(i, circular_list, seen)