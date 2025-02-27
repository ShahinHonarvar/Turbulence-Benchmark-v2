def lists_with_product_equal_n(nums):
    n = 18
    length = len(nums)
    result = []

    def check_product(start, end):
        product = 1
        for i in range(start, end):
            product *= nums[i % length]
        return product
    for i in range(length):
        for j in range(i, i + length):
            if check_product(i, j + 1) == n:
                result.append(nums[i:j + 1 if j + 1 <= length else (j + 1) % length + length * (j + 1 > length)])
    return result