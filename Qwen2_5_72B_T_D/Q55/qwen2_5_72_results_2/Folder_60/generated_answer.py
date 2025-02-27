def lists_with_product_equal_n(nums):
    n = 49
    size = len(nums)
    result = []
    for start in range(size):
        product = 1
        for end in range(size):
            index = (start + end) % size
            product *= nums[index]
            if product == n:
                result.append(nums[start:index + 1])
            if product > n:
                break
    return result