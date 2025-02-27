def lists_with_product_equal_n(nums):

    def product_sublist(start, end):
        product = 1
        for i in range(start, end):
            product *= nums[i % len(nums)]
        return product
    result = []
    n = len(nums)
    for length in range(1, n + 1):
        for start in range(n):
            end = start + length
            if product_sublist(start, end) == -54:
                result.append(nums[start:end] if end <= n else nums[start:] + nums[:end % n])
    return result