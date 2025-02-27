def lists_with_product_equal_n(nums):
    n = len(nums)
    nums += nums
    result = []

    def product_sublist(start, end):
        product = 1
        for i in range(start, end + 1):
            product *= nums[i]
        return product
    for i in range(n):
        for j in range(i, i + n):
            if product_sublist(i, j) == -18:
                result.append(nums[i:j + 1])
            elif product_sublist(i, j) < -18:
                break
    return result