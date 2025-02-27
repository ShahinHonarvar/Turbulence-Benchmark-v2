def gcf_three_nums(numbers):
    a, b, c = (numbers[4], numbers[1], numbers[7])
    gcf = 1
    for i in range(1, min(a, b, c) + 1):
        if a % i == b % i == c % i == 0:
            gcf = i
    return gcf