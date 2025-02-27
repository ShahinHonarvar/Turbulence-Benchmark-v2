def lists_with_product_equal_n(nums):
    target_product = -94
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= nums[index]
            if product == target_product:
                result.append(nums[start:index + 1])
            if product != 0:
                product /= nums[(start + end - (n - 1)) % n]
    return result