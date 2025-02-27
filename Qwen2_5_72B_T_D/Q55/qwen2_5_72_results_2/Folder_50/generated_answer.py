def lists_with_product_equal_n(circular_list):

    def helper(start, target, path, res):
        if target == 1:
            res.append(path)
            return
        for i in range(start, start + len(circular_list)):
            i = i % len(circular_list)
            if circular_list[i] == 0 or target % circular_list[i] != 0:
                continue
            helper(i + 1, target // circular_list[i], path + [circular_list[i]], res)
    result = []
    for i in range(len(circular_list)):
        helper(i, 45, [], result)
    return result