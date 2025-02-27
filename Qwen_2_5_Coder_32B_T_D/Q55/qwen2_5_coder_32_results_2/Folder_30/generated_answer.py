def lists_with_product_equal_n(nums):

    def product(nums):
        p = 1
        for num in nums:
            p *= num
        return p
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = [nums[i % n] for i in range(start, end)]
            if product(sublist) == 99:
                result.append(sublist)
    return result