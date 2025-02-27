def lists_with_product_equal_n(circular_list):
    results = []
    size = len(circular_list)
    circular_list += circular_list
    for start in range(size):
        for end in range(start, start + size):
            sublist = circular_list[start:end % size]
            if sublist and sublist.count(-5) == len(sublist) and (sublist not in results):
                results.append(sublist)
    return results