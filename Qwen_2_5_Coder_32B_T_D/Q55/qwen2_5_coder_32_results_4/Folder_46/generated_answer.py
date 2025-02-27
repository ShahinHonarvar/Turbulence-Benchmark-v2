def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            index = (start + length - 1) % n
            product *= nums[index]
            if product == 53:
                result.append(nums[start:index + 1] if start <= index else nums[start:] + nums[:index + 1])
            elif product % 53 != 0:
                break
    return result