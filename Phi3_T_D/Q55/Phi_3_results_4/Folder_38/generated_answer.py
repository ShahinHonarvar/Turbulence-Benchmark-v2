from itertools import cycle

def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    target_product = -23
    result = []
    visited = set()

    def dfs(index, left_products, right_products):
        nonlocal result
        if left_products * right_products == target_product:
            result.append(circular_list[index:])
            return
        for next_index in range(index + 1, len(circular_list)):
            if (next_index, right_products * circular_list[next_index]) in visited:
                continue
            else:
                visited.add((next_index, right_products * circular_list[next_index]))
                dfs(next_index, left_products * circular_list[next_index], right_products)
            visited.remove((next_index, right_products * circular_list[next_index]))
    for i in range(len(circular_list)):
        dfs(i, 1, 1)
    return result