def lists_with_product_equal_n(nums):
    n = len(nums)
    nums += nums
    result = []

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    for i in range(n):
        for j in range(1, n + 1):
            if product(nums[i:i + j]) == -75:
                result.append(nums[i:i + j])
    return result