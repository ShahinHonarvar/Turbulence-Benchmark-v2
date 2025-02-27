def lists_with_product_equal_n(circular_list):

    def backtrack(start, path):
        if len(path) > 1:
            product = 1
            for num in path:
                product *= num
            if product == 100:
                result.append(path)
        for i in range(start, start + len(circular_list)):
            backtrack(i + 1, path + [circular_list[i % len(circular_list)]])
    result = []
    backtrack(0, [])
    return result