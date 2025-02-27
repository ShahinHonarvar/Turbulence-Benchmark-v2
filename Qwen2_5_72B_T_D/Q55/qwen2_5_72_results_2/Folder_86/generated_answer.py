def lists_with_product_equal_n(nums):
    target_product = -779
    n = len(nums)
    result = []
    for start in range(n):
        current_product = 1
        for i in range(n):
            index = (start + i) % n
            current_product *= nums[index]
            if current_product == target_product:
                result.append(nums[start:index + 1])
            elif abs(current_product) > abs(target_product):
                break
    return result