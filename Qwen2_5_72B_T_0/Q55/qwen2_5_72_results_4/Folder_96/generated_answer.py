def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            real_end = (start + end) % n
            product *= nums[real_end]
            if product == 0:
                result.append(nums[start:real_end + 1])
            if product != 0:
                product = 1
    return result