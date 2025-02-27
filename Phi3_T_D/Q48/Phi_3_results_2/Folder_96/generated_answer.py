def return_binary_or_hexa(nums):
    sum_missing = sum(set(range(nums[50] + 1, nums[200])) - set(nums[50:200]))
    if sum_missing % 2 == 0:
        hex_repr = hex(sum_missing)[2:].upper()
    else:
        bin_repr = format(sum_missing, 'b')
        hex_repr = None
    return hex_repr if hex_repr else bin_repr