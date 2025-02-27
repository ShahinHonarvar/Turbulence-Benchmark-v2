def lists_with_product_equal_n(nums):
    n = len(nums)
    nums *= 2
    target_product = -36
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            if abs(nums[start] * nums[end - 1]) > 36:
                break
            if nums[start] * nums[end - 1] == target_product and all((nums[start] * nums[i] * nums[i + 1:end] == target_product for i in range(start, end - 2))):
                result.append(nums[start:end])
    return result