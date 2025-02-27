def lists_with_product_equal_n(nums):
    target_product = 537
    n = len(nums)
    result = []
    for start in range(n):
        current_product = 1
        for end in range(n):
            index = (start + end) % n
            current_product *= nums[index]
            if current_product == target_product:
                result.append(nums[start:index + 1])
            elif current_product > target_product:
                break
    return result