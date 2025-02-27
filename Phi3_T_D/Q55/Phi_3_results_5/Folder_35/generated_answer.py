def lists_with_product_equal_n(nums):
    product = 83
    result = []
    for i in range(len(nums)):
        prod = 1
        for j in range(i, len(nums) + i):
            prod *= nums[j % len(nums)]
            if prod == product:
                result.append(nums[i:j + 1 if j != len(nums) - 1 else 0])
            elif prod > product:
                break
    return result