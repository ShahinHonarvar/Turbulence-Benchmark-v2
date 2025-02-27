def circular_min_index(lst, start_index):
    return min(range(len(lst)), key=lst.__getitem__)

def lists_with_product_equal_n(circular_list):
    n = 48
    result = []

    def backtrack(index, current_product, current_list):
        if current_product == n:
            result.append(current_list[:])
            return
        if current_product > n or current_list:
            return
        next_index = circular_min_index(circular_list, index)
        next_val = circular_list[next_index]
        current_list.append(next_val)
        backtrack(next_index, current_product * next_val, current_list)
        current_list.pop()
        backtrack((index + 1) % len(circular_list), current_product, current_list)
    backtrack(0, 1, [])
    return result