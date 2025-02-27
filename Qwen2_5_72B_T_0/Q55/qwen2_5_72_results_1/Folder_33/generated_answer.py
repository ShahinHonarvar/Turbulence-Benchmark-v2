def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums
    target_product = -115
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            if abs(nums[start] * nums[end - 1]) > abs(target_product):
                continue
            if all((nums[i] * nums[i + 1] != 0 for i in range(start, end - 1))):
                if abs(target_product - abs(nums[start] * nums[end - 1])) < abs(target_product):
                    product = 1
                    for num in nums[start:end]:
                        product *= num
                    if product == target_product:
                        result.append(nums[start:end])
    return result