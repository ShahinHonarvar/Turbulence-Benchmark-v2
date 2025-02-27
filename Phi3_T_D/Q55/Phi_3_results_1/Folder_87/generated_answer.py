def lists_with_product_equal_n(circular_list):
    target_product = 27
    n = len(circular_list)
    result = []

    def find_sublists(start, end, path):
        if start > end:
            if len(path) > 0 and target_product % (path[0] * path[-1]) == 0:
                possible_product = 1
                for i in path:
                    possible_product *= i
                if possible_product == target_product:
                    result.append(path)
            return
        find_sublists(start + 1, end, path + [circular_list[start]])
        find_sublists(start, end - 1, path)
    for i in range(n):
        find_sublists(i, (i + n - 1) % n, [])
    return result