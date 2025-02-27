def lists_with_product_equal_n(nums):
    target_product = -76
    n = len(nums)
    result = []

    def check_circular_subarrays(start, length):
        if start + length <= n:
            for i in range(start, start + length):
                product = 1
                for j in range(length):
                    product *= nums[(i + j) % n]
                if product == target_product:
                    result.append(nums[i:(i + length) % n] if (i + length) % n > i else nums[i:] + nums[:(i + length) % n])
        else:
            for i in range(start, n):
                product = 1
                for j in range(length):
                    product *= nums[(i + j) % n]
                if product == target_product:
                    result.append(nums[i:] + nums[:(i + length) % n])
    for length in range(1, n + 1):
        check_circular_subarrays(0, length)
    return result