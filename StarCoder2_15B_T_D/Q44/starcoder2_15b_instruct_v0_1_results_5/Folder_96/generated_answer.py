def composite_nums_between_indices(nums):
    composite_nums = [n for n in nums if any((n % i == 0 for i in range(2, n)))]
    return {n for n in composite_nums if 60 <= nums.index(n) <= 200}