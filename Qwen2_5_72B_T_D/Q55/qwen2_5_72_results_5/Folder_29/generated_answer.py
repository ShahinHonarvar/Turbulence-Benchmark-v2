def lists_with_product_equal_n(nums):
    target_product = 15
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            end = (start + size) % n
            product *= nums[end - 1]
            if product == target_product:
                sublist = nums[start:end] if start < end else nums[start:] + nums[:end]
                result.append(sublist)
            if product > target_product:
                break
    return result