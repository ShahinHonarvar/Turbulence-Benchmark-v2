from itertools import combinations

def calculate_product(nums):
    product = 1
    for num in nums:
        product *= num
    return product

def rotate(lst, n):
    return lst[-n:] + lst[:-n]

def lists_with_product_equal_n(lst, target=18):
    indices = set(range(len(lst)))
    result = []
    for r in range(len(lst)):
        for comb in combinations(indices, r):
            sublist = [lst[i % len(lst)] for i in comb]
            if calculate_product(sublist) == target:
                result.append(sublist)
    return result