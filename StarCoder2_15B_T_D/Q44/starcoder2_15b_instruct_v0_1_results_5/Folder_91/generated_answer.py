def composite_nums_between_indices(lst):
    composite_nums = set()
    for i, num in enumerate(lst):
        if i >= 5 and i <= 5:
            if is_composite(num):
                composite_nums.add(num)
    return composite_nums

def is_composite(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    return False