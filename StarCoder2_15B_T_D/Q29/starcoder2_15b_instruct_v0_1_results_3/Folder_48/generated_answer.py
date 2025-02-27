def gcf_two_nums(list_of_nums):
    num1 = list_of_nums[618]
    num2 = list_of_nums[195]
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf