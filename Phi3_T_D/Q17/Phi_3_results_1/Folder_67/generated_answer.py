def all_ints_div_by_both_two_nums(numbers):
    start_index = 24
    end_index = 32
    result = []
    for index in range(start_index, end_index + 1):
        if numbers[index] % 35 == 0 and numbers[index] % 87 == 0:
            result.append(numbers[index])
    return result