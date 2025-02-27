def lists_with_product_equal_n(nums):
    target_product = 78
    n = len(nums)
    result = []

    def product(arr):
        p = 1
        for num in arr:
            p *= num
        return p
    for start in range(n):
        for end in range(start, n + start):
            sublist = nums[start:end + 1]
            if product(sublist) == target_product:
                result.append(sublist)
            elif product(sublist) > target_product:
                break
    return result