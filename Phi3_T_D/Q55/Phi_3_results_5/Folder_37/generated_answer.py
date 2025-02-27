def circular_list_next(index, size):
    return (index + 1) % size

def lists_with_product_equal_n(circular_list):
    target_product = -76
    result = []
    n = len(circular_list)

    def search(start, prod, cur_list):
        if prod == target_product:
            result.append(cur_list)
            return
        if prod != 1 or prod > target_product or len(cur_list) > n:
            return
        for next_index in range(start, n):
            search(circular_list_next(next_index, n), prod * circular_list[next_index], cur_list + [circular_list[next_index]])
    for start_index in range(n):
        search(start_index, circular_list[start_index], [circular_list[start_index]])
    return result