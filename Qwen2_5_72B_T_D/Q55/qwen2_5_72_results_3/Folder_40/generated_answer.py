def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums
    targets = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            product = 1
            for num in nums[start:end]:
                product *= num
            if product == -9:
                targets.append(nums[start:end])
    return targets