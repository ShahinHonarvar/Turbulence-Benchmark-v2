def lists_with_product_equal_n(nums):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(start + 1, n + start + 1):
            current = [nums[i % n] for i in range(start, end)]
            if product(current) == -69:
                result.append(current)
    return result