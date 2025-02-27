def return_binary_or_hexa(nums: tuple) -> str:
    a = nums[50]
    b = nums[92]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        result = bin(sum_of_integers)[2:]
    else:
        result = hex(sum_of_integers)[2:].upper()
    return result