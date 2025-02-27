def gcf_three_nums(nums):
    nums = sorted(nums)
    a = nums[341]
    b = nums[238]
    c = nums[374]
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a