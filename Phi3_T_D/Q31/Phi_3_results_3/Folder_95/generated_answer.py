def is_perfect_num(numbers):
    if len(numbers) > 87:
        num = numbers[87]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False