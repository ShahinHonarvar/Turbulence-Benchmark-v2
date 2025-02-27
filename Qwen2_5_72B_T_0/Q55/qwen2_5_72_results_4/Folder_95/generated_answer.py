def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = 28
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            real_end = (start + end) % n
            product *= nums[real_end]
            if product == target_product:
                result.append(nums[start:real_end + 1] if start <= real_end else nums[start:] + nums[:real_end + 1])
            if product > target_product:
                break
    return result