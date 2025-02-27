def lists_with_product_equal_n(nums):
    target_product = -779
    n = len(nums)
    result = []

    def check_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == target_product
    for start in range(n):
        for end in range(start, start + n):
            sublist = nums[start:] + nums[:end % n]
            if check_product(sublist):
                result.append(sublist)
    return result