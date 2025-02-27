from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def circular_subarrays(arr):
        n = len(arr)
        for length in range(1, n + 1):
            for start in range(n):
                end = start + length
                yield (arr[start:] + arr[:end] if end <= n else arr[start:n] + arr[0:end - n])
    target_product = 25
    result = []
    for subarray in circular_subarrays(circular_list):
        if len(subarray) <= len(circular_list) and all((x * y == target_product for x, y in zip([1] + subarray, subarray))):
            result.append(subarray)
    return result