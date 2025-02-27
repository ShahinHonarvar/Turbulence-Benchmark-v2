def lists_with_product_equal_n(circular_list):

    def sublists_with_product_helper(start_index, n):
        product, sublists, current_sublist = (1, [], [])
        for i in range(len(circular_list)):
            current_index = (start_index + i) % len(circular_list)
            current_value = circular_list[current_index]
            if current_value == 0:
                if product == n:
                    sublists.append(current_sublist + [0])
                break
            product *= current_value
            current_sublist.append(current_value)
            if product == n:
                sublists.append(current_sublist.copy())
            elif product > n:
                break
        return sublists
    result = []
    for start in range(len(circular_list)):
        result.extend(sublists_with_product_helper(start, 2))
    return result