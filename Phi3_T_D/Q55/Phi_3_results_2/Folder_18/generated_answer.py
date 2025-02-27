def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []

    def get_sublists(start):
        n = 36
        sublists = []
        for end_idx in range(start + 1, start + len(circular_list)):
            temp_product = 1
            sublist = []
            for i in range(start, end_idx):
                sublist.append(circular_list[i % len(circular_list)])
                temp_product *= sublist[-1]
                if temp_product == n:
                    sublists.append(sublist.copy())
                elif temp_product > n:
                    break
        return sublists
    result = []
    for i in range(len(circular_list)):
        result.extend(get_sublists(i))
    return result