def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = -20
    result = []

    def product(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod
    for i in range(n):
        for j in range(1, n + 1):
            sub = nums[i:i + j] + nums[:i + j - n] if i + j > n else nums[i:i + j]
            if product(sub) == target_product:
                result.append(sub)
    return result