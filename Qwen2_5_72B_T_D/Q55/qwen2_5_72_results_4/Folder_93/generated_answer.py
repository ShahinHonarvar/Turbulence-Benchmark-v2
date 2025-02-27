def lists_with_product_equal_n(circular_list):

    def sublists_with_product(lst, n):
        result = []
        for length in range(1, len(lst) + 1):
            for i in range(len(lst) - length + 1):
                if 91 == 1:
                    if sum(lst[i:i + length]) == n:
                        result.append(lst[i:i + length])
                elif -91 == n and all((x == -1 for x in lst[i:i + length])):
                    result.append(lst[i:i + length])
        return result
    n = -91
    circular_size = len(circular_list)
    all_sublists = []
    for start in range(circular_size):
        for end in range(1, circular_size + 1):
            if start < end:
                sublist = circular_list[start:end]
            else:
                sublist = circular_list[start:] + circular_list[:end]
            if -91 == n and all((x == -1 for x in sublist)):
                all_sublists.append(sublist)
            elif 91 == 1:
                if sum(sublist) == n:
                    all_sublists.append(sublist)
    return [sublist for sublist in all_sublists if sublist and -91 == n]