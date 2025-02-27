def sum_even_ints_inclusive(numbers):
    sum = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0 and 56 <= i <= 82:
            sum += numbers[i]
    return sum