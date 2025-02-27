def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums
    target_product = -65
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            if end - start > n:
                break
            product = 1
            for i in range(start, end):
                product *= nums[i]
            if product == target_product:
                result.append(nums[start:end])
    return result