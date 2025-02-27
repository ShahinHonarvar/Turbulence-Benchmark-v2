def composite_nums_between_indices(lst):
    composite_nums = set()
    for num in lst:
        if is_composite(num) and 66 <= lst.index(num) <= 93:
            composite_nums.add(num)
    return composite_nums

def is_composite(num):
    for i in range(2, num):
        if num % i == 0:
            return True
    return False