def sum_odd_ints_inclusive(numbers):

    def is_odd(num):
        return num % 2 != 0
    sum_of_odd_ints = 0
    for i, number in enumerate(numbers):
        if is_odd(number) and 59 <= i <= 97:
            sum_of_odd_ints += number
    return sum_of_odd_ints