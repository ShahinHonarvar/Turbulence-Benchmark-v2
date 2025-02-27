def lists_with_product_equal_n(nums):
    target_product = -75
    length = len(nums)
    result = []
    for start in range(length):
        product = 1
        for end in range(length):
            real_end = (start + end) % length
            product *= nums[real_end]
            if product == target_product:
                result.append(nums[start:real_end + 1] if start <= real_end else nums[start:] + nums[:real_end + 1])
            if abs(product) > abs(target_product):
                break
    return result