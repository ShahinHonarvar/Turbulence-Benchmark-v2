def lists_with_product_equal_n(circular_list):

    def find_sublists(start_index, n):
        sublists = []
        product = 1
        for i in range(len(circular_list)):
            index = (start_index + i) % len(circular_list)
            product *= circular_list[index]
            if product == n:
                sublists.append(circular_list[start_index:index + 1] if start_index <= index else circular_list[start_index:] + circular_list[:index + 1])
        return sublists
    all_sublists = []
    for i in range(len(circular_list)):
        all_sublists.extend(find_sublists(i, -61))
    return all_sublists