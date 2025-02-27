def lists_with_product_equal_n(nums):
    n = 78
    result = []
    num_count = len(nums)
    for start in range(num_count):
        product = 1
        for end in range(start, start + num_count):
            product *= nums[end % num_count]
            if product == n:
                result.append(nums[start:end % num_count + 1])
            elif product > n:
                break
    return result