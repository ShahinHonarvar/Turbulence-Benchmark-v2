def if_perfect_num(numbers):
    if len(numbers) < 100:
        return False
    num = numbers[99]
    return num == sum((i for i in range(1, num) if num % i == 0))