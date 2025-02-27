def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for i in range(n):
            index = (start + i) % n
            product *= nums[index]
            if product == 47:
                result.append(nums[start:index + 1])
            elif product % 47 != 0:
                break
    return result