def lists_with_product_equal_n(lst):
    length = len(lst)
    result = []

    def helper(index, current, product):
        if product == -95:
            result.append(current.copy())
        elif product < -95:
            for i in range(index, length):
                current.append(lst[i])
                helper(i + 1, current, product * lst[i])
                current.pop()
    helper(0, [], 1)
    return result