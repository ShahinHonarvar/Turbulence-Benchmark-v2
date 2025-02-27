def lists_with_product_equal_n(nums):
    target_product = 47
    n = len(nums)
    result = []
    for start in range(n):
        current_product = 1
        for end in range(n):
            current_product *= nums[(start + end) % n]
            if current_product == target_product:
                result.append(nums[start:(start + end + 1) % n] if (start + end) % n > start else nums[start:] + nums[:end + 1])
            elif current_product > target_product:
                break
    return result