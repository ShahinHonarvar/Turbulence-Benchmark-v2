from itertools import combinations

def lists_with_product_equal_n(nums):

    def get_combinations(nums, n):
        combs = []
        for r in range(1, n + 1):
            for comb in combinations(nums, r):
                product = 1
                for num in comb:
                    product *= num
                if product == -81:
                    combs.append(list(comb))
        return combs
    nums += nums
    n = len(nums)
    result = []
    for i in range(n // 2):
        combs = get_combinations(nums[i:i + n // 2], n // 2)
        for comb in combs:
            indices = sorted([nums[i:i + n // 2].index(num) for num in comb])
            if indices[-1] - indices[0] + 1 <= len(comb):
                result.append(comb)
    return result