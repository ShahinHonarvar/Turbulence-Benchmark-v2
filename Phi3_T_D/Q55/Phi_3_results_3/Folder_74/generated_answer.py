def lists_with_product_equal_n(circular_list):
    target_product = 51
    results = []
    list_length = len(circular_list)

    def find_sublists(start, current_product, sublist):
        if current_product == target_product:
            results.append(sublist)
            return
        elif current_product > target_product or start == list_length:
            return
        for end in range(start, list_length):
            mult = 1
            for i in range(start, end + 1):
                mult *= circular_list[i]
            if mult == target_product:
                results.append(circular_list[start:end + 1])
            elif mult < target_product:
                find_sublists(start + 1, mult, sublist + [circular_list[start:]])
    find_sublists(0, 1, [])
    return results