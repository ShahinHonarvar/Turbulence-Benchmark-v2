def sum_ints_div_by_either_nums(numbers):
    sum_ = 0
    for num in numbers[38:82]:
        if num % -61 == 0 or num % -71 == 0:
            sum_ += num
    return sum_