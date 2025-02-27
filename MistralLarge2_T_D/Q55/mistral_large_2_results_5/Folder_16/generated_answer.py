def lists_with_product_equal_n(lst, n=-837):

    def get_sublists(lst):
        sublists = []
        for start in range(len(lst)):
            for end in range(start + 1, len(lst) + 1):
                sublists.append(lst[start:end])
        return sublists
    circular_lst = lst * 2
    sublists = get_sublists(circular_lst)
    result = [sublist for sublist in sublists if len(sublist) <= len(lst) and product(sublist) == n]
    return result

def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod