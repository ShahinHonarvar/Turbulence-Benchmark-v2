def lists_with_product_equal_n(nums):
    target_product = 851
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            product *= nums[(start + end) % n]
            if product == target_product:
                result.append(nums[start:(start + end + 1) % n] if (start + end + 1) % n > start else nums[start:n] + nums[0:(start + end + 1) % n])
            if product > target_product:
                break
    return result