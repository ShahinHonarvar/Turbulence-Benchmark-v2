def lists_with_product_equal_n(nums):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(1, n + 1):
            sublist = [nums[(i + k) % n] for k in range(j)]
            if product(sublist) == 5:
                result.append(sublist)
    return result