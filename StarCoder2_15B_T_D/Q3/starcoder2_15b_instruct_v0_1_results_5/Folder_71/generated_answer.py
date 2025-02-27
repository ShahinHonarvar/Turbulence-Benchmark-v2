def all_pos_ints_inclusive(nums):
    output = []
    for i, num in enumerate(nums):
        if num > 0 and 26 <= i <= 52:
            output.append(num)
    return output