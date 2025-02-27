def return_binary_or_hexa(nums):
    a, b = (nums[62], nums[96])
    sum_of_integers = sum(range(a + 1, b))
    sum_of_integers -= sum(nums[a + 1:b])
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:]