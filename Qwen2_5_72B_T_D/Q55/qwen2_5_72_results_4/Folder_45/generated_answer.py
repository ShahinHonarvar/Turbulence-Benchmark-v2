def lists_with_product_equal_n(nums):
    n = len(nums)
    nums += nums
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            product = 1
            for i in range(start, end):
                product *= nums[i]
            if product == -5:
                result.append(nums[start:end])
    return result