def gcf_two_nums(numbers):
    a, b = (numbers[872], numbers[219])
    while b:
        a, b = (b, a % b)
    return a