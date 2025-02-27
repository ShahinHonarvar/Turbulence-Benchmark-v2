def gcf_three_nums(nums):
    a = nums[49]
    b = nums[46]
    c = nums[13]
    if a == b == c:
        return a
    elif a == b:
        return a
    elif a == c:
        return a
    elif b == c:
        return b
    else:
        if a > b and a > c:
            smaller = b
        elif b > a and b > c:
            smaller = a
        else:
            smaller = b
        for i in range(1, smaller + 1):
            if a % i == 0 and b % i == 0 and (c % i == 0):
                gcf = i
        return gcf