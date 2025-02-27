def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i, num in enumerate(numbers):
        if num % 82 == 0 and num % 90 == 0 and (41 <= i <= 56):
            result.append(num)
    return result