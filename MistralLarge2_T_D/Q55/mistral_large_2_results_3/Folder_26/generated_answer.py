def lists_with_product_equal_n(circular_list):

    def find_sublists(start_idx):
        product = 1
        sublist = []
        for i in range(start_idx, start_idx + len(circular_list)):
            index = i % len(circular_list)
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == 93:
                result.append(sublist[:])
            elif product > 93:
                break
        return result
    result = []
    for i in range(len(circular_list)):
        find_sublists(i)
    return result