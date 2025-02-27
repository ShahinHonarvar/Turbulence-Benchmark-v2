def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            actual_end = (start + end) % n
            product *= nums[actual_end]
            if product == -15:
                result.append(nums[start:actual_end + 1])
            elif product == 0:
                break
            elif abs(product) > 15:
                product /= nums[start]
                start = (start + 1) % n
    return result