def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = -51
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            product *= nums[(start + end) % n]
            if product == target_product:
                result.append(nums[start:(start + end + 1) % n])
                if (start + end + 1) % n == 0:
                    break
            if (start + end + 1) % n == start:
                break
    return result