def lists_with_product_equal_n(lst, n):

    def helper(lst, n, sublst, result):
        if not lst or n == 1:
            if sublst and n == 1:
                result.append(sublst)
            return
        helper(lst[1:], n // lst[0], sublst + [lst[0]], result)
        helper(lst[1:], n, sublst, result)
    result = []
    helper(lst + lst, n, [], result)
    return result