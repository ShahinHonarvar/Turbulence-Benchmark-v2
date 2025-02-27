def sum_odd_ints_inclusive(numbers):
    sum_odd_ints = 0
    for num in numbers[36:47]:
        if num % 2 != 0:
            sum_odd_ints += num
    return sum_odd_ints