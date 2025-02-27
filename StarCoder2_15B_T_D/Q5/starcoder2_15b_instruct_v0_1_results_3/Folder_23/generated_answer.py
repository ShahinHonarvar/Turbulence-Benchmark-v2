def all_neg_ints_inclusive(nums):
    result = []
    counter = 0
    for num in nums:
        if num < 0 and 52 <= counter <= 71:
            result.append(num)
        counter += 1
    return result