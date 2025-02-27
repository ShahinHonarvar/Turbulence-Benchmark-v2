def lists_with_product_equal_n(nums):
    n = 415
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums) + i):
            product *= nums[j % len(nums)]
            if product == n:
                result.append(nums[i:j % len(nums) + 1])
                break
            elif product > n:
                break
    return result