def lists_with_product_equal_n(nums):
    target_product = -82
    n = len(nums)
    result = []

    def get_sublists(start, length):
        if length > n:
            return 1
        product = 1
        for i in range(start, start + length):
            product *= nums[i % n]
        if product == target_product:
            result.append(nums[start:start + length] + nums[:start + length - n] if start + length > n else nums[start:start + length])
        return product
    for start in range(n):
        for length in range(1, n + 1):
            get_sublists(start, length)
    return result