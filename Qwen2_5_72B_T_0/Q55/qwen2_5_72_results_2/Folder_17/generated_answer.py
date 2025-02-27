def lists_with_product_equal_n(circular_list):

    def find_sublists(start, product, current_list):
        if product == 18:
            result.append(current_list[:])
            return
        if product > 18:
            return
        for i in range(start, start + len(circular_list)):
            num = circular_list[i % len(circular_list)]
            find_sublists(i + 1, product * num, current_list + [num])
    result = []
    for i in range(len(circular_list)):
        find_sublists(i, 1, [])
    return result