def lists_with_product_equal_n(nums):
    target_product = -83
    n = len(nums)

    def find_sublists(start, length):
        sublists = []
        for size in range(1, length + 1):
            product = 1
            for i in range(start, start + size):
                product *= nums[i % n]
            if product == target_product:
                sublists.append(nums[start:(start + size) % n] if start + size < n else nums[start:] + nums[:(start + size) % n])
        return sublists
    result = []
    for i in range(n):
        result.extend(find_sublists(i, n))
    return result