def lists_with_product_equal_n(circular_list):
    n = 733
    result = []

    def backtrack(path, start, prod):
        if prod == n:
            result.append(path)
            return
        if prod > n:
            return
        for i in range(len(circular_list)):
            if i == start or circular_list[i] == 0:
                continue
            backtrack(path + [circular_list[i]], (start + i) % len(circular_list), prod * circular_list[i])
    for i, num in enumerate(circular_list):
        backtrack([num], i, num)
    return result