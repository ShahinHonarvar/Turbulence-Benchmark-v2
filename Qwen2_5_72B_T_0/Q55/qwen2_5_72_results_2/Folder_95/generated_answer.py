def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = 28
    result = []
    for start in range(n):
        product = 1
        for i in range(n):
            index = (start + i) % n
            product *= nums[index]
            if product == target_product:
                result.append(nums[start:index + 1])
            if product > target_product:
                break
    return result