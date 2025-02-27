def lists_with_product_equal_n(circular_list):
    n = -17

    def backtrack(start, curr, product):
        if product == n:
            result.append(curr[:])
            return
        for i in range(start, len(circular_list) + start):
            if i > len(circular_list) - 1:
                i = 0
            if product * circular_list[i] == n or circular_list[i] == 0:
                curr.append(circular_list[i])
                backtrack(i + 1, curr, product * circular_list[i])
                curr.pop()
    result = []
    for i in range(len(circular_list)):
        backtrack(i, [], 1)
    return result