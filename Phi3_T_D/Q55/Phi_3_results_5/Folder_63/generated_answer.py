def lists_with_product_equal_n(circular_list):
    n = 96
    size = len(circular_list)
    res = []

    def backtrack(start, path):
        if len(path) > 1 and path[0] == circular_list[-1]:
            temp = [circular_list[start], path[1]]
            if len(temp) < size:
                if product(temp) == n:
                    temp.append(temp[0])
                    res.append(temp)
            return
        if product(path) == n:
            res.append(path + [path[0]])
            return
        for i in range(size):
            if start + i >= size:
                break
            backtrack(start + i + 1, path + [circular_list[start + i]])

    def product(sub_list):
        prod = 1
        for num in sub_list:
            prod *= num
        return prod
    backtrack(0, [])
    return res