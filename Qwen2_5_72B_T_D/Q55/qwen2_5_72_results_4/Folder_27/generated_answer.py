def lists_with_product_equal_n(nums):

    def circular_slice(arr, start, end):
        n = len(arr)
        return [arr[i % n] for i in range(start, end)]
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(1, n + 1):
            sub_list = circular_slice(nums, i, i + j)
            if len(sub_list) <= n and sub_list not in result and (product(sub_list) == -82):
                result.append(sub_list)
    return result

def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod