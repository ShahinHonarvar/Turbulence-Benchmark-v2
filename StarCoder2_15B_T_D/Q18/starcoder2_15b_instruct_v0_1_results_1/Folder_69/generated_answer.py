def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i, num in enumerate(ints):
        if num % 31 == 0 or num % 11 == 0:
            if between(i, 61, 88):
                sum += num
    return sum

def between(num, start, end):
    return start <= num <= end