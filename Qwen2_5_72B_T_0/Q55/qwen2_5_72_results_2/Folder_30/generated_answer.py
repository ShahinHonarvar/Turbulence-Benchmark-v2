def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = 99
    result = []

    def product(arr):
        p = 1
        for num in arr:
            p *= num
        return p
    for start in range(n):
        for end in range(start, start + n):
            sublist = nums[start:] + nums[:end % n]
            if product(sublist) == target_product:
                result.append(sublist)
    return result