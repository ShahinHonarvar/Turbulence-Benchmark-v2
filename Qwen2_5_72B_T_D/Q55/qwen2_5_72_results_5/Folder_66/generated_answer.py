def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = 78
    result = []

    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for start in range(n):
        for end in range(start, n + start):
            sublist = nums[start:end + 1]
            if len(sublist) > n:
                break
            if get_product(sublist) == target_product:
                result.append(sublist)
    return result