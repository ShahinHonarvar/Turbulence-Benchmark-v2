def gcf_two_nums(numbers):
    num_90 = numbers[90]
    num_54 = numbers[54]
    smaller = min(num_90, num_54)
    for i in range(smaller, 0, -1):
        if num_90 % i == 0 and num_54 % i == 0:
            return i