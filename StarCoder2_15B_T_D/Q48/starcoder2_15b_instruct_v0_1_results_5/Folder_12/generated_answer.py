from itertools import chain

def return_binary_or_hexa(nums):
    a = nums[16]
    b = nums[87]
    sum_of_integers = sum(range(a + 1, b))
    sum_of_missing_integers = sum(set(range(a + 1, b)) - set(nums))
    sum_of_integers += sum_of_missing_integers
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()