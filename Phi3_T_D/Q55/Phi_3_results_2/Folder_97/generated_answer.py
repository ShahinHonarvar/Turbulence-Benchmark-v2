def lists_with_product_equal_n(circular_list):

    def find_sublists(start, product, temp_list):
        if product % n == 0:
            if product == n:
                result.append(temp_list)
        for i in range(start, start + len(circular_list)):
            next_index = i % len(circular_list)
            find_sublists(next_index + 1, product * circular_list[next_index], temp_list + [circular_list[next_index]])
    n = -938
    result = []
    for i in range(len(circular_list)):
        find_sublists(i, circular_list[i], [circular_list[i]])
    return result