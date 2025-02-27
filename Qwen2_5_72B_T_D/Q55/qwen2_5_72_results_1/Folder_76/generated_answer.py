def lists_with_product_equal_n(nums):
    target = 247
    n = len(nums)
    result = []

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    for i in range(n):
        for j in range(1, n + 1):
            sublist = nums[i:i + j] + nums[:j - (n - i)]
            if product(sublist) == target:
                result.append(sublist)
    return result