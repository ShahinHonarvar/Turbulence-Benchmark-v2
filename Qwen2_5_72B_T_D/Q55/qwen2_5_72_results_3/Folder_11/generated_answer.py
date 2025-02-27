def lists_with_product_equal_n(nums):

    def product(arr):
        p = 1
        for num in arr:
            p *= num
        return p
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(1, n + 1):
            sublist = nums[i:i + j] + nums[:j - (n - i) if i + j > n else 0]
            if product(sublist) == -15:
                result.append(sublist)
    return result