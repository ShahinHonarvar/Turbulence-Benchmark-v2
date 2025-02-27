def lists_with_product_equal_n(nums):

    def is_valid_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 733
    n = len(nums)
    result = []
    for start in range(n):
        current_product = 1
        for end in range(start, start + n):
            current_product *= nums[end % n]
            if current_product == 733:
                result.append(nums[start:end % n + 1])
            elif current_product > 733:
                break
    return result