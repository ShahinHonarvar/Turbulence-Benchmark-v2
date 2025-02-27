def find_sublists(lst, target, start, end, cum_product, result):
    if start > end or cum_product == 0:
        return
    if cum_product == target:
        result.append(lst[start:end + 1])
        return
    find_sublists(lst, target, start + 1, end, cum_product * lst[start], result)
    find_sublists(lst, target, start, end - 1, cum_product * lst[end], result)

def make_circular(lst):
    circular_lst = lst + lst[:-1]
    return circular_lst

def lists_with_product_equal_n(lst):
    target = -89
    circular_list = make_circular(lst)
    result = []
    for size in range(1, len(circular_list)):
        find_sublists(circular_list, target, 0, size, circular_list[0], result)
    result = [sublist for sublist in result if all((isinstance(n, int) and type(n) != bool for n in sublist))]
    return result