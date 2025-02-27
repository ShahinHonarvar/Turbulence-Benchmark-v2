def lists_with_product_equal_n(circular_list):

    def find_sublists(start_index):
        product = 1
        sublist = []
        for i in range(len(circular_list)):
            current_index = (start_index + i) % len(circular_list)
            product *= circular_list[current_index]
            sublist.append(circular_list[current_index])
            if product == 3:
                result.append(sublist[:])
            elif product > 3:
                break
    result = []
    for i in range(len(circular_list)):
        find_sublists(i)
    return result