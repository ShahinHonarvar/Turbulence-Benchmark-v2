def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    target = 6
    result = set()

    def find_sublists(start, end, product):
        if product == target:
            result.add(tuple(circular_list[start:end]))
        if product * circular_list[end % size] == target:
            find_sublists(start, end + 1, product * circular_list[end % size])
        else:
            find_sublists(start, end + 1, target)
    for i in range(size):
        find_sublists(i, i, circular_list[i])
    return [list(sublist) for sublist in result]