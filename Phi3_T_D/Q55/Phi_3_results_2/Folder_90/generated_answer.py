from itertools import combinations

def find_sublists_with_product(arr, target_product):

    def product(nums):
        result = 1
        for num in nums:
            result *= num
        return result
    result = []
    for i in range(1, len(arr) + 1):
        for sublist in combinations(arr, i):
            if product(sublist) == target_product:
                result.append(list(sublist))
    return result

def lists_with_product_equal_n(arr):
    if len(arr) == 0:
        return []
    circular_list = arr + arr[:-1]
    return find_sublists_with_product(circular_list, -690)