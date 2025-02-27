def lists_with_product_equal_n(nums):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = len(nums)
    result = []
    for size in range(1, n + 1):
        for start in range(n):
            sublist = [nums[(start + i) % n] for i in range(size)]
            if product(sublist) == -83:
                result.append(sublist)
    return result