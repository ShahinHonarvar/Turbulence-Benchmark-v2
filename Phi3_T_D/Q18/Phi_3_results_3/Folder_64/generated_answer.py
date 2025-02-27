def sum_ints_div_by_either_nums(integers):
    sum_result = 0
    for number in integers[:4]:
        if number % 11 == 0 or number % -7 == 0:
            sum_result += number
    return sum_result