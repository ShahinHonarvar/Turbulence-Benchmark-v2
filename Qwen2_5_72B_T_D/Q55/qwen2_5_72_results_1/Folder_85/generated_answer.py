def lists_with_product_equal_n(nums):
    target_product = -97
    n = len(nums)
    result = []

    def check_product(start, length):
        product = 1
        for i in range(length):
            product *= nums[(start + i) % n]
        return product
    for length in range(1, n + 1):
        for start in range(n):
            if check_product(start, length) == target_product:
                sublist = nums[start:start + length]
                if length + start > n:
                    sublist = nums[start:] + nums[:length - (n - start)]
                result.append(sublist)
    return result