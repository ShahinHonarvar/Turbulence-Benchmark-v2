def lists_with_product_equal_n(nums):
    target_product = 76
    n = len(nums)
    result = []

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    for i in range(n):
        for j in range(1, n + 1):
            subarr = nums[i:i + j] + nums[:j - (n - i) % n] if i + j > n else nums[i:i + j]
            if product(subarr) == target_product:
                result.append(subarr)
    return result