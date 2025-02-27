def lists_with_product_equal_n(nums):
    target_product = -7
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            real_end = (start + end) % n
            product *= nums[real_end]
            if product == target_product:
                result.append(nums[start:real_end + 1] if start <= real_end else nums[start:] + nums[:real_end + 1])
            if product == 0:
                break
    return result