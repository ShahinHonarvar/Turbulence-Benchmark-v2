def lists_with_product_equal_n(circular_list):

    def find_sublists(start, product, current_list):
        if product == 90:
            result.append(current_list[:])
            return
        if product > 90:
            return
        for i in range(start, start + len(circular_list)):
            num = circular_list[i % len(circular_list)]
            find_sublists(i + 1, product * num, current_list + [num])
    result = []
    unique_combinations = set()
    for i in range(len(circular_list)):
        find_sublists(i, 1, [])
    for r in result:
        r_tuple = tuple(r)
        if r_tuple not in unique_combinations:
            unique_combinations.add(r_tuple)
    return [list(t) for t in unique_combinations]