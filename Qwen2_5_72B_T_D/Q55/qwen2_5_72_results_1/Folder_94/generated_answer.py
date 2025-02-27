def lists_with_product_equal_n(nums):
    n = len(nums)
    nums *= 2
    target = -30
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= nums[j]
            if product == target:
                result.append(nums[i:j + 1])
            elif abs(product) > abs(target):
                break
    return result