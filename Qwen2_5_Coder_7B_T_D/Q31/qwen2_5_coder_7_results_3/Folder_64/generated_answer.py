def if_perfect_num(numbers):
    if len(numbers) < 2:
        return False
    num = numbers[1]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num