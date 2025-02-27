from itertools import combinations

def lists_with_product_equal_n(nums):

    def circular_subarrays(arr):
        n = len(arr)
        subarrays = []
        for i in range(n):
            for j in range(1, n + 1):
                sub = arr[i:i + j]
                if len(sub) < j:
                    sub.extend(arr[:j - len(sub)])
                subarrays.append(sub)
        return subarrays
    subarrays = circular_subarrays(nums)
    target_product = 45
    result = [sub for sub in subarrays if len(sub) <= len(nums) and target_product == eval('*'.join(map(str, sub)))]
    return result