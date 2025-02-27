def lists_with_product_equal_n(nums):

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = nums[start:end % n + 1] if end < n else nums[start:] + nums[:end % n + 1]
            if product(sublist) == -46:
                result.append(sublist)
    return result