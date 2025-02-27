def lists_with_product_equal_n(nums):
    target_product = 32
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for size in range(n):
            index = (start + size) % n
            product *= nums[index]
            if product == target_product:
                result.append(nums[start:index + 1] if start <= index else nums[start:] + nums[:index + 1])
            if product > target_product:
                break
    return result