def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= nums[end]
            if product == 6:
                result.append(nums[start:end + 1])
            elif product > 6:
                break
    return result