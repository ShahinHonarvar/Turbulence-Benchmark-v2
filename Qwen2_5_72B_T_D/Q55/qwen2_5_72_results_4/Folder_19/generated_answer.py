def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = -54
    result = []

    def product_sublist(start, length):
        if length == 0:
            return 1
        return nums[(start + length - 1) % n] * product_sublist(start, length - 1)
    for start in range(n):
        for length in range(1, n + 1):
            if product_sublist(start, length) == target_product:
                result.append(nums[start:start + length])
                if length > 1:
                    result.append([nums[(start + i) % n] for i in range(1, length + 1)])
    return result