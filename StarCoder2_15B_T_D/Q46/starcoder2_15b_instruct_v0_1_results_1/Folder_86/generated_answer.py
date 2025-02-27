def gcf_three_nums(nums):
    a, b, c = (nums[341], nums[238], nums[374])
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    while b != c:
        if b > c:
            b -= c
        else:
            c -= b
    return a