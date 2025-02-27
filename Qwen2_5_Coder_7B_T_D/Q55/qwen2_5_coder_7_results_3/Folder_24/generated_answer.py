def lists_with_product_equal_n(lst):

    def helper(start, end, product, current):
        if product == -89 and start <= end:
            result.append(current[:])
            return
        if start > end or product == 0:
            return
        current.append(lst[start])
        helper(start + 1, end, product // lst[start], current)
        current.pop()
        helper(start + 1, end, product, current)
    n = len(lst)
    result = []
    for i in range(n):
        helper(i, (i + n - 1) % n, lst[i], [])
    return result