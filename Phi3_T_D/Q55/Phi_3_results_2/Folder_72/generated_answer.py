def lists_with_product_equal_n(numbers):
    result = []

    def helper(ind, cur_list, prod, size):
        if prod == 10:
            result.append(cur_list[:])
            return
        for i in range(ind, len(numbers) + ind):
            n = numbers[i % len(numbers)]
            if prod * n > 10:
                return
            if prod * n == 10:
                result.append(cur_list + [n])
                return
            helper(i + 1, cur_list + [n], prod * n, size)
    helper(0, [], 1, len(numbers))
    return result