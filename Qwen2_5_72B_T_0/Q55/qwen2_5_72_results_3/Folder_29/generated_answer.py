def lists_with_product_equal_n(circular_list):

    def find_sublists(start, product, current_list):
        if product == 15:
            result.append(current_list[:])
            return
        if product > 15:
            return
        for i in range(start, start + len(circular_list)):
            num = circular_list[i % len(circular_list)]
            find_sublists(i + 1, product * num, current_list + [num])
    result = []
    find_sublists(0, 1, [])
    return result