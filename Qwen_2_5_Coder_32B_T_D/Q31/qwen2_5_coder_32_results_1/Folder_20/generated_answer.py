def if_perfect_num(numbers):
    if len(numbers) > 53:
        num = numbers[53]
        return sum([i for i in range(1, num) if num % i == 0]) == num
    return False