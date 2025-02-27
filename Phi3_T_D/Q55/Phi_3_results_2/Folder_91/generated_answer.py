from itertools import cycle, islice

def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)

    def find_sublists(start_index, current_list):
        if start_index == size:
            start_index = 0
        if any((x == 2 for x in current_list)):
            result.append(current_list)
        for i in range(start_index, size):
            if i + 1 < size:
                find_sublists(i + 1, list(islice(cycle(circular_list), i + 1, i + 4)))
            else:
                find_sublists(0, list(islice(cycle(circular_list), i + 1 - size, i + 1)))
    for i in range(size):
        find_sublists(i, list(islice(cycle(circular_list), i, i + 4)))
    return result