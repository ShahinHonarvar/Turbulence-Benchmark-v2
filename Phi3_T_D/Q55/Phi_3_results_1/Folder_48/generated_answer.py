def lists_with_product_equal_n(nums):
    target = 990
    circular_nums = nums + nums
    sublists = []
    for length in range(1, len(nums) + 1):
        for start in range(len(nums)):
            product = 1
            for end in range(start, start + length):
                product *= circular_nums[end]
                if product > target:
                    break
                if product == target:
                    sublists.append(circular_nums[start:start + length])
    return sublists