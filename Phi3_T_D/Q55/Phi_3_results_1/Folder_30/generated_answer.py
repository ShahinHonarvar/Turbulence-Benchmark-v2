def lists_with_product_equal_n(circular_list):

    def backtrack(start, path):
        product = 1
        temp_path = path[:]
        for i in range(start, len(circular_list) + start):
            product *= circular_list[i % len(circular_list)]
            temp_path.append(circular_list[i % len(circular_list)])
            if product == 99:
                res.append(temp_path[:])
            if product > 99:
                break
    res = []
    for i in range(len(circular_list)):
        backtrack(i, [])
    return res