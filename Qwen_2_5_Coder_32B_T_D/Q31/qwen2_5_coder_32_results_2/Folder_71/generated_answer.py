def if_perfect_num(numbers):
    if len(numbers) > 78:
        num = numbers[78]
        return num == sum([i for i in range(1, num) if num % i == 0])
    return False