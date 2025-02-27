def lists_with_product_equal_n(nums):

    def get_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(nums)
    result = []
    for start in range(n):
        current_product = 1
        for end in range(start, start + n):
            current_product *= nums[end % n]
            if current_product == 537:
                result.append(nums[start % n:end % n + 1] if start <= end else nums[start % n:] + nums[:end % n + 1])
            if current_product == 0 or current_product > 537:
                break
    return result