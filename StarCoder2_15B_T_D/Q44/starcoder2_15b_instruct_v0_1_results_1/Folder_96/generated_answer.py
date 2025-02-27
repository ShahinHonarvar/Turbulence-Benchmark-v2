def composite_nums_between_indices(nums):
    start_index = 60
    end_index = 200
    composite_nums = set()
    for i, num in enumerate(nums):
        if start_index <= i <= end_index:
            if is_composite_num(num):
                composite_nums.add(num)
    return composite_nums

def is_composite_num(num):
    if num < 4:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False