def lists_with_product_equal_n(nums):
    target_product = 100
    n = len(nums)
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