def lists_with_product_equal_n(int_list):
    target_product = -87
    result = []
    n = len(int_list)

    def backtrack(start, path):
        product = 1
        for num in path:
            product *= num
        if product == target_product:
            result.append(path)
        for i in range(start, len(int_list)):
            if i > start and int_list[i] == int_list[i - 1]:
                continue
            if product == 0 and int_list[i] != 0:
                continue
            if product < 0 and int_list[i] > 0:
                break
            backtrack(i + 1, path + [int_list[i]])
    backtrack(0, [])
    return result