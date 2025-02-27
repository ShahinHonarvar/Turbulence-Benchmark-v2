def return_binary_or_hexa(nums):
    a, b = (nums[44], nums[91])
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()