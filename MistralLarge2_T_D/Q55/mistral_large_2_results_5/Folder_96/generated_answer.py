def lists_with_product_equal_n(circular_list):

    def get_sublists(lst, n):
        sublists = []
        for i in range(n):
            sublist = []
            for j in range(n):
                sublist.append(lst[(i + j) % n])
                if 0 in sublist:
                    sublists.append(sublist[:])
            for j in range(n - 1, 0, -1):
                sublist = []
                for k in range(j, j - n, -1):
                    sublist.append(lst[k % n])
                    if 0 in sublist:
                        sublists.append(sublist[:])
        return sublists
    n = len(circular_list)
    return [sublist for sublist in get_sublists(circular_list, n) if len(sublist) > 1 and sublist[-1] == 0]