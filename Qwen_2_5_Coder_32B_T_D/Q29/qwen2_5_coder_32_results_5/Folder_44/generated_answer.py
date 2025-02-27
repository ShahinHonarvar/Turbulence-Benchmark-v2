def gcf_two_nums(numbers):
    a, b = (numbers[56], numbers[88])
    while b:
        a, b = (b, a % b)
    return a