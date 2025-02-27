def sum_even_ints_inclusive(nums):
    start_idx = 56
    end_idx = 98
    total = 0
    for i, num in enumerate(nums):
        if i >= start_idx and i <= end_idx:
            if num % 2 == 0:
                total += num
    return total