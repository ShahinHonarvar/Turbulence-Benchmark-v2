def if_perfect_num(numbers):
    target = numbers[27]
    sum = 0
    for i in range(1, target):
        if target % i == 0:
            sum += i
    return sum == target