def lists_with_product_equal_n(nums):

    def circular_subarrays(arr):
        n = len(arr)
        for length in range(1, n + 1):
            for start in range(n):
                subarray = []
                for i in range(length):
                    subarray.append(arr[(start + i) % n])
                yield subarray
    subarrays_with_product = []
    for subarray in circular_subarrays(nums):
        product = 1
        for num in subarray:
            product *= num
        if product == -32:
            subarrays_with_product.append(subarray)
    return subarrays_with_product