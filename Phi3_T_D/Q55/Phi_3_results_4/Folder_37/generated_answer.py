def lists_with_product_equal_n(circular_list):
    result = []

    def extend_sublist(sublist, start):
        product = 1
        sublist.append(circular_list[start])
        product *= sublist[-1]
        next_index = (start + 1) % len(circular_list)
        while product != -76 and len(sublist) <= len(circular_list):
            sublist.append(circular_list[next_index])
            product *= sublist[-1]
            next_index = (next_index + 1) % len(circular_list)
        return (product == -76, sublist, start)
    for i in range(len(circular_list)):
        sublist, new_start = ([], i)
        while True:
            found, sublist, new_start = extend_sublist(sublist, new_start)
            if not found:
                break
            i = (i + len(sublist)) % len(circular_list)
            while circular_list[i:i + len(sublist)] == sublist:
                i = (i + len(sublist)) % len(circular_list)
        if found:
            result.append(sublist)
    return result