def lists_with_product_equal_n(nums):

    def product(arr):
        p = 1
        for num in arr:
            p *= num
        return p
    if not nums:
        return []
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = nums[start:start + end] + nums[:end] if start + end > n else nums[start:start + end]
            if product(sublist) == -95:
                result.append(sublist)
    return result