def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if 527 <= i <= 538 and is_composite_num(num)}

def is_composite_num(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return True
    return False