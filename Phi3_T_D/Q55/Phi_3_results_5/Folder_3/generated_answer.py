def lists_with_product_equal_n(circular_list):

    def find_sublists_with_product(start, prod, temp_list):
        if prod == -22 and temp_list:
            res.append(temp_list)
            return
        if prod == 0:
            return
        for i in range(start, len(circular_list) + start):
            current = circular_list[i % len(circular_list)]
            find_sublists_with_product((i + 1) % len(circular_list), prod * current, temp_list + [current])
    res = []
    for i in range(len(circular_list)):
        find_sublists_with_product(i, circular_list[i], [])
    return res