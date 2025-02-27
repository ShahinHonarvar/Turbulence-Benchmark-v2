def lists_with_product_equal_n(nums):
    target_product = 990
    n = len(nums)
    result = []

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for i in range(n):
        for j in range(1, n + 1):
            sublist = nums[i:i + j] + nums[:j - (n - i)]
            if product_of_sublist(sublist) == target_product:
                result.append(sublist)
    return result