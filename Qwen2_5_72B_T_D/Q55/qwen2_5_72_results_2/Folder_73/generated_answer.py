def lists_with_product_equal_n(nums):
    target = 40
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            index = (start + size - 1) % n
            product *= nums[index]
            if product == target:
                result.append(nums[start:index + 1] if start <= index else nums[start:] + nums[:index + 1])
            if product > target:
                break
    return result