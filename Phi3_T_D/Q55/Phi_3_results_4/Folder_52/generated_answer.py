def rotate(nums, k):
    k = k % len(nums)
    return nums[k:] + nums[:k]

def continuous_sublists_product_equal_n(nums, n):
    sublists = []
    for i in range(len(nums)):
        product = 1
        for num in nums[i:]:
            product *= num
            if product == n:
                sublists.append(nums[i:nums.index(num) + 1])
        for j in range(1, len(nums)):
            if i + j < len(nums):
                product = 1
                for num in nums[i:i + j]:
                    product *= num
                if product == n:
                    sublists.append(nums[i:i + j])
    return sublists

def lists_with_product_equal_n(circular_list):
    n = 37
    sublists = []
    for _ in range(len(circular_list)):
        sublists.extend(continuous_sublists_product_equal_n(circular_list, n))
        circular_list = rotate(circular_list, 1)
    return list(set(map(tuple, sublists)))