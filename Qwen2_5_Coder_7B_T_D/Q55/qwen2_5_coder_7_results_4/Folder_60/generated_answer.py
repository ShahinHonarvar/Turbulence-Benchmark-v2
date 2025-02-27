def lists_with_product_equal_n(nums):
    n = 49
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(i, i + len(nums)):
            product *= nums[j % len(nums)]
            if product == n:
                result.append(nums[i:j % len(nums) + 1])
            elif product > n:
                break
    return result