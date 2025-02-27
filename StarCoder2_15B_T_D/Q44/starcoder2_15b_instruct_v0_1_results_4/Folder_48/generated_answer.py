def composite_nums_between_indices(lst):
    composite_nums = set()
    for i, num in enumerate(lst):
        if num < 2:
            continue
        for j in range(2, num):
            if num % j == 0:
                composite_nums.add(num)
                break
    if 661 <= len(composite_nums) <= 924:
        return composite_nums
    else:
        return set()