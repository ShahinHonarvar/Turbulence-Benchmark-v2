def if_perfect_num(numbers):
    if len(numbers) < 8:
        return False
    num = numbers[7]
    return sum((i for i in range(1, num) if num % i == 0)) == num