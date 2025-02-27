def lists_with_product_equal_n(nums):
    n = len(nums)
    nums += nums
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            if -17 == eval('*'.join(map(str, nums[start:end]))):
                result.append(nums[start:end])
    return result