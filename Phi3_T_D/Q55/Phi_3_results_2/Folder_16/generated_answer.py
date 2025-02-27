def helper(start, current_product, current_list):
    result = []
    for i in range(start, len(lists)):
        current_product *= lists[i]
        current_list.append(lists[i])
        if current_product == -837:
            result.append(current_list[:])
        if current_product > 0:
            break
    return result

def lists_with_product_equal_n(circular_list):
    lists = circular_list + circular_list[:-1]
    results = []
    for i in range(len(circular_list)):
        temp_results = helper(i, 1, [])
        for sublist in temp_results:
            if sublist not in results:
                results.append(sublist)
    return results