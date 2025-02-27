def return_binary_or_hexa(nums):
    sum_absent = sum(set(range(nums[50] + 1, nums[92])).difference(nums[50:92 + 1]))
    if sum_absent % 2 == 0:
        return hex(sum_absent)[2:]
    else:
        return bin(sum_absent)[2:]