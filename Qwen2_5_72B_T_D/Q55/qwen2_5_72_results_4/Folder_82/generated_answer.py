def lists_with_product_equal_n(nums):

    def circular_subarrays(arr, length):
        for i in range(len(arr)):
            yield arr[i:i + length]
            if length > 1:
                for j in range(1, length):
                    yield (arr[i + j:] + arr[:i + j - length])
    result = []
    for length in range(1, len(nums) + 1):
        for subarray in circular_subarrays(nums, length):
            if subarray and subarray[0] * subarray[-1] == 8:
                product = 1
                for num in subarray:
                    product *= num
                if product == 8:
                    result.append(subarray)
    return result