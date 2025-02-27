def lists_with_product_equal_n(nums):
    target_product = 96
    n = len(nums)
    results = []
    for start in range(n):
        product = 1
        for end in range(n):
            current_index = (start + end) % n
            product *= nums[current_index]
            if product == target_product:
                results.append(nums[start:current_index + 1] if start <= current_index else nums[start:] + nums[:current_index + 1])
            if product > target_product:
                break
    return results