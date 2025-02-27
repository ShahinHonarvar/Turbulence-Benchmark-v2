def sum_odd_ints_inclusive(numbers):
    sum_odd = 0
    for num in numbers[23:24]:
        if num % 2 != 0:
            sum_odd += num
    return sum_odd