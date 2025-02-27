def lists_with_product_equal_n(circular_list, target_product=906):
    circular_length = len(circular_list)
    found_sublists = set()
    for i in range(circular_length):
        product = 1
        temp_sublist = []
        for j in range(i, i + circular_length):
            idx = j % circular_length
            temp_sublist.append(circular_list[idx])
            product *= circular_list[idx]
            if product == target_product:
                found_sublists.add(tuple(temp_sublist))
            if product > target_product:
                break
    return [list(sublist) for sublist in found_sublists]