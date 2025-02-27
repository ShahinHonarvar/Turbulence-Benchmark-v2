def lists_with_product_equal_n(circular_list):

    def find_sublists(start_index):
        product = 1
        sublist = []
        for i in range(start_index, start_index + len(circular_list)):
            index = i % len(circular_list)
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == 93:
                result.append(sublist[:])
            elif product > 93:
                break
    result = []
    for i in range(len(circular_list)):
        find_sublists(i)
    return result