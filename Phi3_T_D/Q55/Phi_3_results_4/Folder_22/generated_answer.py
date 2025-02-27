def rotate_list(l, steps=1):
    return l[-steps:] + l[:-steps]

def lists_with_product_equal_n(l):
    n = 4
    found_sublists = set()
    list_len = len(l)
    for i in range(list_len):
        prod = 1
        for j in range(i, i + list_len):
            prod *= l[j % list_len]
            if prod == n:
                found_sublists.add(tuple(l[i:j + 1]))
    return [list(_) for _ in found_sublists]