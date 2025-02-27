def lists_with_product_equal_n(nums):
    target_product = -938
    n = len(nums)
    results = []
    for start in range(n):
        current_product = 1
        for end in range(n):
            real_end = (start + end) % n
            current_product *= nums[real_end]
            if current_product == target_product:
                results.append(nums[start:real_end + 1])
            if current_product != 0:
                current_product /= nums[start + (end - n + 1) % n]
    return results