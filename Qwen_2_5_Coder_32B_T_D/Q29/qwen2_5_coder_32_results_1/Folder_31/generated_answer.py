def gcf_two_nums(numbers):
    a, b = (numbers[87], numbers[95])
    while b:
        a, b = (b, a % b)
    return a