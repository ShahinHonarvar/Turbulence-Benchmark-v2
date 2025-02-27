def sum_even_ints_inclusive(numbers):
    sum_even = 0
    for num in numbers[4:5]:
        if num % 2 == 0:
            sum_even += num
    return sum_even