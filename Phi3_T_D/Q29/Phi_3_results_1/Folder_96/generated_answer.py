def gcf_two_nums(numbers):
    a, b = (numbers[95], numbers[73])
    while b:
        a, b = (b, a % b)
    return a