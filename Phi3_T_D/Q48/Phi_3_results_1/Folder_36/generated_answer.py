def return_binary_or_hexa(nums):
    if len(nums) <= 348 or nums[110] > nums[348]:
        return ''
    sum_val = sum(set(range(nums[110] + 1, nums[348])).difference(nums[110:349]))
    return bin(sum_val)[2:] if sum_val % 2 != 0 else hex(sum_val)[2:]