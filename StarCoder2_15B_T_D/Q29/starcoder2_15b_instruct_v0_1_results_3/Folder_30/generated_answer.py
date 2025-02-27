def gcf_two_nums(numbers):
    number_85 = numbers[85]
    number_33 = numbers[33]
    smaller_number = min(number_85, number_33)
    for i in range(1, smaller_number + 1):
        if number_85 % i == 0 and number_33 % i == 0:
            return i
    return 1