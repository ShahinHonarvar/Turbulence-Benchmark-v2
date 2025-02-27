def gcf_two_nums(nums):
    num1 = nums[872]
    num2 = nums[219]
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            break
        greater += 1
    return greater