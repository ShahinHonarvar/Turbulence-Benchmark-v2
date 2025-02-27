def lists_with_product_equal_n(nums):

    def circular_slice(arr, start, length):
        return [arr[(start + i) % len(arr)] for i in range(length)]
    results = []
    n = len(nums)
    for start in range(n):
        for size in range(1, n + 1):
            product = 1
            for i in range(size):
                product *= nums[(start + i) % n]
            if product == -30:
                results.append(circular_slice(nums, start, size))
    return results