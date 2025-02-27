def lists_with_product_equal_n(circular_list):
    n = 54
    result = []
    length = len(circular_list)

    def find_sublists(start, product, current):
        if product == n:
            result.append(current)
            return
        if product > n:
            return
        for i in range(length):
            new_start = (start + i) % length
            find_sublists(new_start, product * circular_list[new_start], current + [circular_list[new_start]])
    for i in range(length):
        find_sublists(i, 1, [])
    return result