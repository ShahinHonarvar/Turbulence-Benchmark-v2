def sum_odd_ints_inclusive(numbers):
    sum_odd = 0
    for num in numbers[62:64]:
        if num % 2 == 1:
            sum_odd += num
    return sum_odd