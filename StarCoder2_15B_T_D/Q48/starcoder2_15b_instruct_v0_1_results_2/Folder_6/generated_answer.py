def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[93]
    sum_of_nums = sum(range(a + 1, b))
    sum_of_present_nums = sum(nums[a + 1:b])
    sum_of_missing_nums = sum_of_nums - sum_of_present_nums
    if sum_of_missing_nums % 2 == 1:
        return bin(sum_of_missing_nums)[2:]
    else:
        return hex(sum_of_missing_nums)[2:].upper()