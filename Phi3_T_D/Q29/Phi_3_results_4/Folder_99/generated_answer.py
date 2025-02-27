def gcf_two_nums(numbers):
    a, b = (numbers[278], numbers[811])
    while b:
        a, b = (b, a % b)
    return a